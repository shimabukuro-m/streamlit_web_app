import streamlit as st # type: ignore
from PIL import Image # type: ignore
import pandas as pd # type: ignore
import datetime
import io

st.page_link("main_app.py", label="Home", icon="🏠")

# セッションステート初期化
if "records" not in st.session_state:
    st.session_state.records = []

if "edit_index" not in st.session_state:
    st.session_state.edit_index = None

if "delete_index" not in st.session_state:
    st.session_state.delete_index = None

st.title("あせも記録アプリ")

# 編集中のデータ取得
editing = st.session_state.edit_index is not None
edit_data = st.session_state.records[st.session_state.edit_index] if editing else {}

# 🔁 削除が指定されていたら実行してリセット
if st.session_state.delete_index is not None:
    del st.session_state.records[st.session_state.delete_index]
    st.session_state.delete_index = None
    st.success("記録を削除しました ✅")

# 🔽 入力フォーム
with st.form("entry_form"):
    name = st.text_input("名前", value=edit_data.get("名前", ""))
    age = st.number_input("年齢", min_value=0, max_value=120, value=edit_data.get("年齢", 0))  # 年齢追加
    diary = st.text_input("My diary", value=edit_data.get("日記", ""))
    bui = st.multiselect(
        '部位',
        ('頭皮', '顔', '首', '背中', 'おなか', '小股', 'お尻', '腕', '脚'),
        default=edit_data.get("部位", "").split(", ") if editing else []
    )
    kayumi = st.slider("かゆみ", 0, 10, value=edit_data.get("かゆみレベル", 0))
    akami = st.slider("発赤", 0, 10, value=edit_data.get("発赤レベル", 0))
    date = st.date_input("日付", value=edit_data.get("日付", datetime.date.today()))
    uploaded_file = st.file_uploader("症状の写真", type=["jpg", "jpeg", "png"])

    submit = st.form_submit_button("保存")
    cancel = st.form_submit_button("キャンセル")

    if cancel:
        st.session_state.edit_index = None

    if submit:
        image_bytes = uploaded_file.read() if uploaded_file else (edit_data.get("画像") if editing else None)
        new_record = {
            "名前": name,
            "年齢": age,  # 年齢を記録に追加
            "日記": diary,
            "部位": ", ".join(bui),
            "かゆみレベル": kayumi,
            "発赤レベル": akami,
            "日付": date,
            "画像": image_bytes
        }

        if editing:
            st.session_state.records[st.session_state.edit_index] = new_record
            st.success("記録を更新しました ✅")
            st.session_state.edit_index = None
        else:
            st.session_state.records.append(new_record)
            st.success("記録を追加しました ✅")

# 表・グラフ・画像付き記録
if st.session_state.records:
    # DataFrameのインデックスを日付に変更
    df = pd.DataFrame([{
        k: v for k, v in rec.items() if k != "画像"
    } for rec in st.session_state.records])

    df["日付"] = pd.to_datetime(df["日付"], errors="coerce")
    df_sorted = df.sort_values("日付")

    # インデックスを日付に設定
    df_sorted.set_index("日付", inplace=True)

    st.subheader("📈 かゆみ・発赤レベルの推移")
    try:
        chart_df = df_sorted[["かゆみレベル", "発赤レベル"]]
        st.line_chart(chart_df)
    except Exception as e:
        st.error(f"グラフの描画中にエラーが発生しました: {e}")

    st.subheader("📋 記録一覧")
    df_sorted.rename(columns={"日記": "My Diary"}, inplace=True)  # 列名変更
    st.dataframe(df_sorted)

    st.subheader("🖼 写真一覧と操作")
    for idx, rec in enumerate(st.session_state.records):
        st.write(f"📅 {rec['日付']} - 👤 {rec['名前']} - 年齢: {rec['年齢']}歳")  # 年齢も表示
        st.write(f"📝 {rec['日記']}")
        if rec["画像"]:
            image = Image.open(io.BytesIO(rec["画像"]))
            st.image(image, caption="症状写真", width=300)
        else:
            st.write("（画像なし）")

        col1, col2 = st.columns(2)
        if col1.button(f"✏️ 編集する", key=f"edit_{idx}"):
            st.session_state.edit_index = idx
        if col2.button(f"🗑️ 削除する", key=f"delete_{idx}"):
            st.session_state.delete_index = idx

        st.markdown("---")

else:
    st.info("まだ記録がありません。")
