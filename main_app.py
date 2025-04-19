import streamlit as st 
from PIL import Image 
import pandas as pd 
import datetime

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

st.title('kanacare')
st.subheader('あせもに悩むあなたのお助けアプリです')

st.subheader('・つぶやき記録')
col1, col2 = st.columns(2)
with col1:
    st.text('気になるお肌のトラブル、あせものお悩み記録')
with col2:
    st.page_link("pages/page_1.py", label="Page 1", icon="1⃣")

st.subheader('・お医者さんリスト')
col1, col2 = st.columns(2)
with col1:
    st.text('頼りになるお近くの皮膚科、オンライン診療')
with col2:
    st.page_link("pages/page_2.py", label="Page 2", icon="2⃣")

st.subheader('・あせもの豆知識')
col1, col2 = st.columns(2)
with col1:
    st.text('予防法や受診の判断基準に')
with col2:
    st.page_link("pages/page_3.py", label="Page 3", icon="3⃣")

st.subheader('・市販薬リスト')
col1, col2 = st.columns(2)
with col1:
    st.text('みんながお薦めする市販薬、紹介します')
with col2:
    st.page_link("pages/page_4.py", label="Page 4", icon="4⃣")

st.subheader('・予防に役立つグッズ紹介')
col1, col2 = st.columns(2)
with col1:
    st.text('あせもの予防に役立つグッズ、紹介します')
with col2:
    st.page_link("pages/page_5.py", label="Page 5", icon="5⃣")

#画像表示
image = Image.open('./data/child1.png')
st.image(image, width=600)