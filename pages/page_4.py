import streamlit as st

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

# タイトルと説明
st.title("あせもに効く市販薬リスト")
st.subheader("みんながおすすめする市販薬を、紹介します")

# ステロイド配合の市販薬
st.subheader("✅ ステロイド配合の市販薬（炎症が強い場合）")
st.markdown("""
- **[オイラックスPZリペアクリーム](https://www.daiichisankyo-hc.co.jp/products/details/eurax_pz_repair_cream/)** → 炎症を抑え、かゆみを軽減。
- **[近江兄弟社メンタームペンソールSP](http://www.omibh.co.jp/products/medical/pensole_sp.html)** → 液体タイプで広範囲に塗りやすい。
- **[ウナコーワエースG](https://hc.kowa.co.jp/otc/23560)** → ゲルタイプで伸びが良く、かゆみを素早く鎮める。
""")

# ステロイド無配合の市販薬
st.subheader("✅ ステロイド無配合の市販薬（軽度の症状向け）")
st.markdown("""
- **[デリナースクール](https://item.rakuten.co.jp/minacolor/m-4956622110527/)** → 清涼感のあるクリームタイプで、かゆみを抑える。
- **[アセモアパウダースプレー](https://www.kobayashi.co.jp/seihin/ama/index.html)** → 背中など広範囲に塗りやすいスプレータイプ。
- **[タクトローション](https://www.e-welcia.com/product/95153)** → べたつかず、さっぱりしたローションタイプ。
""")

# 参考エビデンス
st.header("📚 参考エビデンス")
st.write("""
- [ミナカラ：あせもに効く市販薬](https://minacolor.com/articles/6252)
- [ミナカラ：大人のあせもに効く市販薬](https://www.minacolor.com/articles/5511)
- [ミナカラ：ステロイド配合・無配合の市販薬](https://minacolor.com/articles/7702)
""")

# フッター
st.write("---")
st.write("⚕️ 本ページはエビデンスに基づいた情報を提供しています。自己判断せず、必要な場合は医療機関に相談してください。")

