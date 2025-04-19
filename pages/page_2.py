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

import pandas as pd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut


# アプリのタイトルと説明
st.title("お医者さんリスト")

st.subheader('皮膚科専門医検索アプリ with 位置情報')
st.caption("都道府県や市町村を入力して、該当する医師情報と位置情報を表示します。")

# 検索窓（上部に配置）
query = st.text_input("都道府県または市町村を入力してください")

# CSVファイルを読み込む
df = pd.read_csv("pages/dermatology_specialists.csv")

# Geopyのジオロケーター設定
geolocator = Nominatim(user_agent="kanacare_geopy")

# 検索クエリがない場合は医師情報の一覧を非表示
if query:
    # 検索結果をフィルタリング
    results = df[df.apply(lambda row: query in row.to_string(), axis=1)]
    
    if not results.empty:
        st.write(f"検索結果: {len(results)} 件")
        st.dataframe(results)
        
        # 位置情報の取得
        locations = []
        for index, row in results.iterrows():
            # 勤務先や都道府県、市町村をアドレスとして利用
            address = row.get("勤務先") or query
            try:
                location = geolocator.geocode(address, timeout=10)
                if location:
                    locations.append({
                        "住所": address,
                        "緯度": location.latitude,
                        "経度": location.longitude,
                        "Googleマップリンク": f"https://www.google.com/maps?q={location.latitude},{location.longitude}"
                    })
            except GeocoderTimedOut:
                st.write(f"⚠️ Geocodingタイムアウト: {address}")

        # 位置情報をデータフレームで表示
        if locations:
            loc_df = pd.DataFrame(locations)
            st.write("位置情報（緯度・経度）:")
            st.dataframe(loc_df)

            # Googleマップリンクを表示
            st.write("Googleマップへのリンク:")
            for _, loc in loc_df.iterrows():
                st.markdown(f"[{loc['住所']} の位置をGoogleマップで開く]({loc['Googleマップリンク']})", unsafe_allow_html=True)
            
            # 地図に位置をプロット
            st.map(loc_df.rename(columns={"緯度": "lat", "経度": "lon"}))
        else:
            st.write("⚠️ 位置情報が見つかりませんでした。")
    else:
        st.write("⚠️ 該当するデータが見つかりませんでした。")
else:
    st.write("検索を行うと結果が表示されます。")

st.write("---")
st.subheader('オンライン診療')
st.text('気軽にオンラインで診療したい時は・・')

col1, col2 = st.columns(2)
with col1:
    st.link_button("ファストドクター", "https://fastdoctor.jp/online-consultation/#symptoms")
with col2:
    st.link_button("CLINIC　FOR", "https://www.clinicfor.life/telemedicine/")