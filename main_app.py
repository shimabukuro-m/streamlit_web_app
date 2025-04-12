import streamlit as st # type: ignore
from PIL import Image # type: ignore
import pandas as pd # type: ignore
import matplotlib.pyplot as plt # type: ignore
import datetime

st.page_link("main_app.py", label="Home", icon="🏠")
st.title('kanacare')
st.caption('あせもに悩むあなたやあなたの大事な人のお助けアプリです')
st.page_link("pages/page_1.py", label="Page 1", icon="1⃣")
st.subheader('・つぶやき記録')
st.text('気になるお肌のトラブル、あせものお悩み記録はこちらに。')
st.page_link("pages/page_2.py", label="Page 2", icon="2⃣")
st.subheader('・お医者さんリスト')
st.text('頼りになるお近くの皮膚科、オンライン診療のリストです。')
st.page_link("pages/page_3.py", label="Page 3", icon="3⃣")
st.subheader('・あせもの豆知識')
st.text('そのあせも、ホームケアだけで大丈夫？？受診の判断基準に。')
st.page_link("pages/page_4.py", label="Page 4", icon="4⃣")
st.subheader('・市販薬リスト')
st.text('みんながお薦めする市販薬、紹介します')
st.page_link("pages/page_5.py", label="Page 5", icon="5⃣")
st.subheader('・予防グッズ')
st.text('あせもの予防に役立つグッズ、紹介します')

#画像表示
image = Image.open('./data/child1.png')
st.image(image, width=600)