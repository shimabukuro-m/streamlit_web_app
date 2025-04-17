import streamlit as st

st.page_link("main_app.py", label="Home", icon="🏠")

# タイトルと説明
st.title("汗疹(あせも)に効く市販薬リスト")
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

