import streamlit as st
from PIL import Image
import pandas as pd
import datetime
import io
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager

st.page_link("main_app.py", label="Home", icon="🏠")

# Meiryoフォント設定（Windows/Mac対応）
if matplotlib.get_backend() != 'agg':
    font_path = "C:/Windows/Fonts/meiryo.ttc"  # Windows用
else:
    font_path = "/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc"  # Mac用の一例
jp_font = font_manager.FontProperties(fname=font_path)

st.title("あせも記録アプリ")

# セッションステート初期化
if "records" not in st.session_state:
    st.session_state.records = []

if "edit_index" not in st.session_state:
    st.session_state.edit_index = None

if "delete_index" not in st.session_state:
    st.session_state.delete_index = None

# 削除処理
if st.session_state.delete_index is not None:
    del st.session_state.records[st.session_state.delete_index]
    st.session_state.delete_index = None
    st.success("記録を削除しました ✅")

# 編集モード取得
editing = st.session_state.edit_index is not None
edit_data = st.session_state.records[st.session_state.edit_index] if editing else {}

# 入力フォーム
with st.form("entry_form"):
    name = st.text_input("名前", value=edit_data.get("名前", ""))
    age = st.number_input("年齢", min_value=0, max_value=120, value=edit_data.get("年齢", 0))
    diary = st.text_input("My diary", value=edit_data.get("日記", ""))
    bui = st.multiselect(
        '部位',
        ('頭皮', '顔', '首', '背中', 'おなか', '小股', 'お尻', '腕', '脚'),
        default=edit_data.get("部位", "").split(", ") if editing else []
    )
    kayumi = st.slider("かゆみレベル", 0, 10, value=edit_data.get("かゆみレベル", 0))
    akami = st.slider("発赤レベル", 0, 10, value=edit_data.get("発赤レベル", 0))

    default_datetime = edit_data.get("日付", datetime.datetime.now())
    date_input = st.date_input("日付", value=default_datetime.date())
    time_input = st.time_input("時間", value=default_datetime.time())
    date_time = datetime.datetime.combine(date_input, time_input)

    uploaded_file = st.file_uploader("症状の写真", type=["jpg", "jpeg", "png"])

    submit = st.form_submit_button("保存")
    cancel = st.form_submit_button("キャンセル")

    if cancel:
        st.session_state.edit_index = None

    if submit:
        image_bytes = uploaded_file.read() if uploaded_file else (edit_data.get("画像") if editing else None)
        new_record = {
            "名前": name,
            "年齢": age,
            "日記": diary,
            "部位": ", ".join(bui),
            "かゆみレベル": kayumi,
            "発赤レベル": akami,
            "日付": date_time,
            "画像": image_bytes
        }

        if editing:
            st.session_state.records[st.session_state.edit_index] = new_record
            st.success("記録を更新しました ✅")
            st.session_state.edit_index = None
        else:
            st.session_state.records.append(new_record)
            st.success("記録を追加しました ✅")

# 表・グラフ・ダウンロード表示
if st.session_state.records:
    df = pd.DataFrame([{
        k: v for k, v in rec.items() if k != "画像"
    } for rec in st.session_state.records])

    df["日付"] = pd.to_datetime(df["日付"], errors="coerce")
    df_sorted = df.sort_values("日付")
    df_sorted.set_index("日付", inplace=True)

    # グラフ描画と画像保存
    st.subheader("📈 かゆみ・発赤レベルの推移")
    try:
        fig, ax = plt.subplots(figsize=(10, 5))
        df_sorted[["かゆみレベル", "発赤レベル"]].plot(ax=ax, marker='o')
        ax.set_ylabel("レベル", fontproperties=jp_font)
        ax.set_xlabel("日時", fontproperties=jp_font)
        ax.set_title("かゆみ・発赤の推移", fontproperties=jp_font)
        ax.legend(prop=jp_font)
        ax.grid(True)
        ax.set_xticks(df_sorted.index)
        ax.set_xticklabels([dt.strftime("%m/%d（%a）%H:%M") for dt in df_sorted.index], rotation=45, ha="right", fontproperties=jp_font)
        st.pyplot(fig)

        # グラフ画像保存
        img_buf = io.BytesIO()
        fig.savefig(img_buf, format='png')
        st.download_button("📷 グラフ画像をダウンロード", img_buf.getvalue(), file_name="rash_graph.png", mime="image/png")

    except Exception as e:
        st.error(f"グラフ描画エラー: {e}")

    # 記録一覧とCSV
    st.subheader("📋 記録一覧")
    df_display = df_sorted.copy()
    df_display.index = df_display.index.strftime("%Y-%m-%d %H:%M")
    df_display.rename(columns={"日記": "My Diary"}, inplace=True)
    st.dataframe(df_display)

    csv = df_display.to_csv(index=True, encoding='utf-8-sig')
    st.download_button("📄 CSVをダウンロード", data=csv.encode("utf-8-sig"), file_name="ase_records.csv", mime="text/csv")

    # 画像表示と編集削除
    st.subheader("🖼 写真一覧と操作")
    for idx, rec in enumerate(st.session_state.records):
        st.write(f"📅 {rec['日付'].strftime('%Y-%m-%d %H:%M')} - 👤 {rec['名前']} - 年齢: {rec['年齢']}歳")
        st.write(f"📝 {rec['日記']}")
        if rec["画像"]:
            image = Image.open(io.BytesIO(rec["画像"]))
            st.image(image, caption="症状写真", width=300)
        else:
            st.write("（画像なし）")

        col1, col2 = st.columns(2)
        if col1.button("✏️ 編集する", key=f"edit_{idx}"):
            st.session_state.edit_index = idx
        if col2.button("🗑️ 削除する", key=f"delete_{idx}"):
            st.session_state.delete_index = idx

        st.markdown("---")
else:
    st.info("まだ記録がありません。")