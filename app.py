import streamlit as st
from PIL import Image, ImageDraw
import pandas as pd
import random
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="RuiruBiz SUPER APP", page_icon="🚀", layout="wide")
st.title("🚀 RUIRUBIZ SUPER APP - Ruiru's Hustle OS")
st.caption("Poster Genie + Bei Predictor + Map + WhatsApp + M-Pesa + Leaderboard")

tab1, tab2, tab3, tab4 = st.tabs(["🎨 POSTER GENIE", "💰 BEI PREDICTOR", "🗺️ RUIRU MAP + WhatsApp", "🔥 HUSTLE FINDER & LEADERBOARD"])

with tab1:
    st.header("Tengeneza Poster in 10 Sec")
    biashara = st.selectbox("Biashara ni?", ["Food / Chips", "Salon", "Boutique", "Supermarket", "Phone Accessories", "M-Pesa Shop"])
    offer = st.text_input("Offer yako", "Chips + Kuku 350 tu leo Ruiru Bypass!")
    color = st.color_picker("Chagua Rangi", "#FF4500")
    phone = st.text_input("WhatsApp Number", "254712345678")
    if st.button("Tengeneza Poster CRAZY"):
        img = Image.new('RGB', (1080, 1350), color="white")
        draw = ImageDraw.Draw(img)
        draw.rectangle([0,0,1080,350], fill=color)
        draw.rectangle([50,1200,1030,1300], fill="#25D366")
        # Note: Real text needs font, this is simple demo
        draw.text((60,80), biashara.upper(), fill="white")
        draw.text((60,500), offer, fill="black")
        draw.text((60,1220), f"WhatsApp: {phone}", fill="white")
        draw.text((60,1300), "RUIRUBIZ.CO.KE | Ruiru Bypass", fill="gray")
        st.image(img)
        st.success("Poster Tayari! Download hapo juu ⬆️")
        st.link_button("📲 Share kwa WhatsApp", f"https://wa.me/{phone}?text=Nimeona offer yako {offer} RuiruBiz!")

with tab2:
    st.header("💰 Bei Poa - LIVE")
    data = {
        "Bidhaa": ["Unga 2kg", "Mafuta 1L", "Maziwa 500ml", "Sugar 2kg", "TV 32 inch", "Gas 6kg"],
        "Carrefour": [189, 320, 65, 310, 18999, 3500],
        "Naivas": [195, 310, 62, 305, 19500, 3450],
        "Quickmart": [185, 315, 60, 308, 19200, 3400],
        "China Square": [180, 305, 58, 300, 17500, 3350],
        "AI Prediction": ["Shuka Ijumaa", "Panda Jumatatu", "Same", "Shuka 20", "Nunua leo!", "Quickmart best"]
    }
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Best Saver Leo", "China Square", "- Ksh 145")
    with col2:
        st.metric("M-Pesa Cashback", "Ksh 35", "RuiruBiz Deal")
    st.info("Lipa na M-Pesa Till: 5432198 - RuiruBiz")
    if st.button("💳 Lipa na M-Pesa (DEMO)"):
        st.balloons()
        st.success("STK Push sent! Check your phone 2547... (Demo)")

with tab3:
    st.header("🗺️ Ruiru Biashara Map - Live Pins")
    m = folium.Map(location=[-1.148, 36.963], zoom_start=14)
    businesses = [
        ["Ruiru Bypass Chips", -1.148, 36.963, "Chips 350"],
        ["Tatu City Salon", -1.15, 36.97, "Braids 1500"],
        ["Ruiru Market Boutique", -1.145, 36.96, "Dress 1200"],
    ]
    for name, lat, lon, offer in businesses:
        folium.Marker([lat, lon], popup=f"<b>{name}</b><br>{offer}<br><a href='https://wa.me/254712345678' target='_blank'>WhatsApp</a>", tooltip=name).add_to(m)
    st_folium(m, width=700, height=400)
    st.write("📍 Click any pin to WhatsApp the hustle directly!")

with tab4:
    st.header("🔥 AI Hustle Finder - I have X, what business?")
    budget = st.slider("Niko na ngapi?", 1000, 100000, 5000, step=1000)
    skill = st.selectbox("Skill yako?", ["Kupika", "Kuongea na wateja", "Mitandao", "Driving", "Beauty"])
    if st.button("NIAMBIE AI"):
        ideas = {
            "Kupika": f"Na {budget}: Anza chips + mayai kando ya Ruiru Bypass. Profit Ksh {budget//5}/day",
            "Kuongea na wateja": f"Na {budget}: M-Pesa + airtime shop. Commission Ksh {budget//10}/day",
            "Mitandao": f"Na {budget}: Manage posters for 10 shops @500 each. RuiruBiz Genie!",
            "Driving": f"Na {budget}: Boda boda delivery for RuiruBiz shops",
            "Beauty": f"Na {budget}: Mini salon kwa plot, braids 800 bob"
        }
        st.success(ideas[skill])
        st.balloons()

    st.divider()
    st.subheader("🏆 Ruiru Hustle Leaderboard TODAY")
    leaderboard = pd.DataFrame({
        "Biashara": ["Mama Mboga Bypass", "Fix-Phone Ruiru", "Shawarma Point", "Salon Neema"],
        "Votes": [234, 189, 156, 120],
        "Trend": ["🔥", "📈", "⭐", "💅"]
    })
    st.table(leaderboard)
    vote = st.selectbox("Pigia kura yako", leaderboard["Biashara"])
    if st.button("Vote 🔥"):
        st.success(f"Umevote {vote}! Imeenda #1!")