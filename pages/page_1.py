import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
import datetime

# 記録保存用のセッションステート
if "records" not in st.session_state:
    st.session_state.records = []

with st.form(key='profile_form'):

    #テキストボックス
    name = st.text_input('誰の肌トラブルですか？名前を入力してください。')
    diary = st.text_input('My diary')

    #複数選択
    bui = st.multiselect(
        '部位',
        ('頭皮', '顔', '首', '背中', 'おなか', '小股', 'お尻', '腕', '脚'))
    
    #スライダー
    kayumi = st.slider('かゆみレベル', min_value=0, max_value=10, step=1)
    akami = st.slider('発赤レベル', min_value=0, max_value=10, step=1)

    #日付
    start_date = st.date_input(
        '開始日',
        datetime.date(2025,4,1))


    #ボタン
    submit_btn = st.form_submit_button('登録')
    cancel_btn = st.form_submit_button('キャンセル')
    if submit_btn:
       
        st.session_state.records.append({
            "日付": start_date,
            "名前": name,
            "日記": diary,
            "部位": ", ".join(bui),
            "かゆみレベル": kayumi,
            "発赤レベル": akami
        })
        st.success("記録が保存されました ✅")
# 記録がある場合、表示・グラフ化
if st.session_state.records:
    df = pd.DataFrame(st.session_state.records)
    df = df.sort_values("日付")

    st.subheader("📈 かゆみ・発赤レベルの推移")

    # グラフ表示
    st.line_chart(df.set_index("日付")[["かゆみレベル", "発赤レベル"]])

    st.subheader("📋 記録一覧")
    st.dataframe(df)
else:
    st.info("まだ記録がありません。")   