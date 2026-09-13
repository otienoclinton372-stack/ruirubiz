import streamlit as st
from PIL import Image, ImageDraw
import pandas as pd
import random

st.set_page_config(page_title="RuiruBiz AI", page_icon="🛒")
st.title("🛒 RUIRU BIZ - 2-in-1 GENIE")
st.write("Poster + Bei Predictor")

tab1, tab2 = st.tabs(["🎨 POSTER GENIE", "💰 BEI PREDICTOR"])

with tab1:
    st.header("Tengeneza Poster in 10 Sec")
    biashara = st.selectbox("Biashara ni?", ["Food / Chips", "Salon", "Boutique", "Supermarket"])
    offer = st.text_input("Offer yako", "Chips + Kuku 350 tu leo Ruiru Bypass!")
    color = st.color_picker("Chagua Rangi", "#FF4500")
    if st.button("Tengeneza Poster"):
        img = Image.new('RGB', (800, 1000), color="white")
        draw = ImageDraw.Draw(img)
        draw.rectangle([0,0,800,200], fill=color)
        draw.text((50,50), biashara, fill="white")
        draw.text((50,300), offer, fill="black")
        draw.text((50,900), "RuiruBiz.co.ke", fill="gray")
        st.image(img)
        st.success("Poster Tayari!")

with tab2:
    st.header("💰 Bei Poa - Fake Sample")
    data = {
        "Bidhaa": ["Unga 2kg", "Mafuta 1L", "Maziwa 500ml", "Sugar 2kg", "TV 32 inch", "Gas 6kg"],
        "Carrefour": [189, 320, 65, 310, 18999, 3500],
        "Naivas": [195, 310, 62, 305, 19500, 3450],
        "Quickmart": [185, 315, 60, 308, 19200, 3400],
        "China Square": [180, 305, 58, 300, 17500, 3350],
        "AI Prediction": ["Shuka Ijumaa", "Panda Jumatatu", "Same", "Shuka 20", "Nunua leo!", "Quickmart best"]
    }
    df = pd.DataFrame(data)
    st.table(df)
    st.info("Ukitaka Unga + Mafuta + Sugar, AI: Nunua China Square na Quickmart - Save 35 bob!")
    item = st.selectbox("Tafuta bidhaa", data["Bidhaa"])
    st.success(f"AI kwa {item}: {random.choice(['Nunua LEO!', 'Ngoja Ijumaa', 'China Square cheapest'])}")