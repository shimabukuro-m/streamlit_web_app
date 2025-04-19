import streamlit as st # type: ignore

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

import streamlit as st

# あせもとは？
st.title("あせもの豆知識")
st.subheader("""
あせもとは、汗の通り道である **汗管** が詰まることで炎症を起こし、皮膚に発疹やかゆみが生じる皮膚疾患です。医学的には **「汗疹（かんしん）」** と呼ばれます。
""")

# あせもの種類
st.header("🔎 あせもの種類")
st.write("""
あせもには **3つのタイプ** があります:\n
        
1️⃣ **水晶様汗疹**（すいしょうようかんしん） → 透明な小さな水疱ができるが、かゆみはほぼなし。乳幼児に多い。\n
2️⃣ **紅色汗疹**（こうしょくかんしん） → 赤い発疹ができ、かゆみやヒリヒリ感を伴う。最も一般的なタイプ。\n
3️⃣ **深在性汗疹**（しんざいせいかんしん） → 皮膚の深い部分で汗管が詰まり、赤い丘疹ができる。重症化しやすい。\n
""")

# 科学的に証明された予防法
st.header("💡 予防法")
st.write("""
✅ **汗をこまめに拭く** → 汗に含まれる塩分が汗管を塞ぐのを防ぐ。\n
✅ **通気性の良い服を着る** → 汗の蒸発を促し、皮膚のムレを防ぐ。\n
✅ **適度なシャワーで皮膚を清潔に保つ** → 石鹸の使いすぎは逆効果なので注意。\n
✅ **エアコンや扇風機で環境を調整** → 高温多湿を避けることで発症リスクを低減。
""")

# 皮膚科受診の目安
st.header("🧑‍⚕️ 皮膚科受診の目安")
st.write("""
🚨 **かゆみが強く、掻きむしってしまう** → 細菌感染のリスクあり。\n
🚨 **発疹が化膿している** → 皮膚炎やとびひの可能性。\n
🚨 **セルフケアをしても改善しない** → 専門的な治療が必要。\n
""")

# 参考エビデンス
st.header("📚 参考エビデンス")
st.write("""
- [メディカルノート：あせもの原因と治し方](https://medicalnote.jp/diseases/%E3%81%82%E3%81%9B%E3%82%82/contents/210128-005-JU)
- [大正製薬：あせもの予防と対策](https://www.taisho-kenko.com/disease/631/)
- [青島周一：汗疹治療のエビデンスとOTC医薬品](https://note.com/syuichiao/n/n15f4d3f2552a)
""")

# フッター
st.write("---")
st.write("⚕️ 症状が改善されない場合は、自己判断せず医療機関に相談してください。")


st.subheader('一人で悩まないで')
st.text('これって汗疹かな？病院行った方が良いかな？悩んだ時は・・')


st.link_button("専門家に相談", "https://www.justanswer.jp/medical/")