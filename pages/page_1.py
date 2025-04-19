import streamlit as st
from PIL import Image
import pandas as pd
import datetime
import io
import sqlite3
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager
import os
from openai import OpenAI
from st_audiorec import st_audiorec

col1, col2, col3, col4, col5, col6 = st.columns(6)
with col1:
    st.page_link("main_app.py", label="Home", icon="🏠")
with col2:
    st.page_link("pages/page_1.py", label="diary", icon="1⃣")
with col3:
    st.page_link("pages/page_2.py", label="hospitals", icon="2⃣")
with col4:
    st.page_link("pages/page_3.py", label="trivia", icon="3⃣")
with col5:
    st.page_link("pages/page_4.py", label="medicine", icon="4⃣")
with col6:
    st.page_link("pages/page_5.py", label="goods", icon="5⃣")

# --- 日本語フォント設定（Meiryo） ---
if os.name == 'nt':
    font_path = "C:/Windows/Fonts/meiryo.ttc"
else:
    font_path = "/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc"
jp_font = font_manager.FontProperties(fname=font_path)

# --- Whisper設定（新API） ---
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def transcribe_audio(file_bytes):
    response = client.audio.transcriptions.create(
        model="whisper-1",
        file=("recorded.wav", io.BytesIO(file_bytes)),
        response_format="text"
    )
    return response

st.title("つぶやき記録")
st.subheader('あせも記録アプリ（音声入力対応）')

# --- SQLite接続 ---
DB_FILE = "rash_records.db"
conn = sqlite3.connect(DB_FILE)
c = conn.cursor()

# --- テーブル作成 ---
c.execute('''
    CREATE TABLE IF NOT EXISTS records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        diary TEXT,
        bui TEXT,
        itch INTEGER,
        redness INTEGER,
        date TEXT,
        image BLOB
    )
''')
conn.commit()

# --- 音声録音と文字変換 ---
st.write("🎤 下記ボタンから音声入力でMy Diaryが入力可能です")
wav_audio_data = st_audiorec()
transcribed_text = ""
if wav_audio_data:
    with st.spinner("音声を文字に変換中..."):
        transcribed_text = transcribe_audio(wav_audio_data)
        st.success("音声の変換が完了しました ✅")

# --- セッションステートで日付と時間を保持 ---
if "selected_date" not in st.session_state:
    st.session_state.selected_date = datetime.date.today()
if "selected_time" not in st.session_state:
    st.session_state.selected_time = datetime.datetime.now().time()

# --- 入力フォーム ---
with st.form("entry_form"):
    name = st.text_input("名前")
    age = st.number_input("年齢", min_value=0, max_value=120)
    diary = st.text_input("My diary", value=transcribed_text)
    bui = st.multiselect('部位', ('頭皮', '顔', '首', '背中', 'おなか', '小股', 'お尻', '腕', '脚'))
    kayumi = st.slider("かゆみレベル", 0, 10, 0)
    akami = st.slider("発赤レベル", 0, 10, 0)
    date_input = st.date_input("日付", value=st.session_state.selected_date, key="date_input")
    time_input = st.time_input("時間", value=st.session_state.selected_time, key="time_input")
    date_time = datetime.datetime.combine(date_input, time_input)
    uploaded_file = st.file_uploader("症状の写真", type=["jpg", "jpeg", "png"], key="image")
    submit = st.form_submit_button("保存")

    if submit:
        image_bytes = uploaded_file.read() if uploaded_file else None
        c.execute('''
            INSERT INTO records (name, age, diary, bui, itch, redness, date, image)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (name, age, diary, ", ".join(bui), kayumi, akami, date_time.isoformat(), image_bytes))
        conn.commit()
        st.success("記録が保存されました ✅")

# --- データ読み込み ---
df = pd.read_sql_query("SELECT * FROM records", conn)
df['date'] = pd.to_datetime(df['date'], format='mixed')
df_sorted = df.sort_values("date")
df_sorted.set_index("date", inplace=True)

if not df_sorted.empty:
    st.subheader("📈 かゆみ・発赤レベルの推移")
    try:
        fig, ax = plt.subplots(figsize=(10, 5))
        df_sorted[["itch", "redness"]].plot(ax=ax, marker='o')
        ax.set_ylabel("レベル", fontproperties=jp_font)
        ax.set_xlabel("日時", fontproperties=jp_font)
        ax.set_title("かゆみ・発赤の推移", fontproperties=jp_font)
        ax.legend(["かゆみレベル", "発赤レベル"], prop=jp_font)
        ax.grid(True)
        ax.set_xticks(df_sorted.index)
        ax.set_xticklabels([dt.strftime("%m/%d（%a）%H:%M") for dt in df_sorted.index], rotation=45, ha="right", fontproperties=jp_font)
        st.pyplot(fig)

        img_buf = io.BytesIO()
        fig.savefig(img_buf, format='png')
        st.download_button("📷 グラフ画像をダウンロード", img_buf.getvalue(), file_name="rash_graph.png", mime="image/png")
    except Exception as e:
        st.error(f"グラフ描画エラー: {e}")

    st.subheader("📋 記録一覧")
    df_display = df_sorted.copy()
    df_display.index = df_display.index.strftime("%Y-%m-%d %H:%M")
    df_display.rename(columns={"diary": "My Diary", "itch": "かゆみレベル", "redness": "発赤レベル"}, inplace=True)
    st.dataframe(df_display.drop(columns=["image"]))

    csv = df_display.drop(columns=["image"]).to_csv(index=True, encoding='utf-8-sig')
    st.download_button("📄 CSVをダウンロード", data=csv.encode("utf-8-sig"), file_name="ase_records.csv", mime="text/csv")

    st.subheader("🖼 写真一覧と操作")
    for idx, row in df_sorted.iterrows():
        date_str = row.name.strftime('%Y-%m-%d %H:%M') if isinstance(row.name, datetime.datetime) else str(row.name)
        st.write(f"📅 {date_str} - 👤 {row['name']} - 年齢: {row['age']}歳")
        st.write(f"📝 {row['diary']}")
        if row['image']:
            st.image(Image.open(io.BytesIO(row['image'])), caption="症状写真", width=300)
        else:
            st.write("（画像なし）")

        if st.button("🗑️ この記録を削除", key=f"delete_{row['id']}"):
            c.execute("DELETE FROM records WHERE id = ?", (row['id'],))
            conn.commit()
            st.success("記録を削除しました ✅")
            st.rerun()

        st.markdown("---")
else:
    st.info("まだ記録がありません。")