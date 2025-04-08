import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
import datetime

st.title('kanacare')
st.caption('あせもに悩むあなたやあなたの大事な人のお助けアプリです')
st.subheader('page_1　つぶやき記録')
st.text('気になるお肌のトラブル、あせものお悩み記録はこちらに。')
st.subheader('page_2　お医者さんリスト')
st.text('頼りになるお近くの皮膚科、オンライン診療のリストです。')
st.subheader('page_3　あせもの豆知識')
st.text('そのあせも、ホームケアだけで大丈夫？？受診の判断基準に。')
st.subheader('page_4　市販薬リスト')
st.text('みんながお薦めする市販薬、紹介します')
st.subheader('page_5　予防グッズ')
st.text('あせもの予防に役立つグッズ、紹介します')

#画像表示
image = Image.open('./data/child1.png')
st.image(image, width=600)