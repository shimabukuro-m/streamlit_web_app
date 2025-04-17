import streamlit as st

st.page_link("main_app.py", label="Home", icon="🏠")

# タイトルと説明
st.title("あせも予防に役立つグッズ紹介")

# 汗を吸収する衣類・寝具
st.subheader("✅ 汗を吸収する衣類・寝具")
st.markdown("""
- **[吸湿速乾インナー](https://www.amazon.co.jp/dp/B08XYZ1234)** → 汗を素早く吸収し、ムレを防ぐ。
- **[通気性の良い寝具](https://www.nitori-net.jp/ec/product/1234567/)** → 寝汗を防ぎ、快適な睡眠環境を作る。
""")

# 皮膚を清潔に保つアイテム
st.subheader("✅ 皮膚を清潔に保つアイテム")
st.markdown("""
- **[低刺激ボディシート](https://www.kobayashi.co.jp/seihin/bodysheet/)** → 外出先でも汗を優しく拭き取れる。
- **[ぬるま湯シャワー用ソープ](https://www.yuskin.co.jp/hadaiku/detail.html?pdid=109)** → 汗を洗い流しながら肌を守る。
""")

# 保湿・冷却アイテム
st.subheader("✅ 保湿・冷却アイテム")
st.markdown("""
- **[メントール配合ローション](https://my-best.com/22063)** → ひんやり感で肌を快適に保つ。
- **[ベビーパウダー](https://www.edimo.jp/baby-kids/post-11322)** → 汗を吸収し、肌をサラサラに保つ。
""")

# 参考エビデンス
st.header("📚 参考エビデンス")
st.write("""
- [肌育研究所：あせも予防の基本](https://yuskin.co.jp/hadaiku/detail.html?pdid=109)
- [mybest：あせも予防ローションランキング](https://my-best.com/22063)
- [edimo：赤ちゃんのあせも対策グッズ](https://edimo.jp/baby-kids/post-11322)
""")

# フッター
st.write("---")
st.write("⚕️ 掲載商品は選び方で記載した効果・効能があることを保証したものではありません。ご購入にあたっては、各商品に記載されている内容・商品説明をご確認ください。")
st.write("症状が寛解しない場合は、速やかに医療機関に相談してください。")