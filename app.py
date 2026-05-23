import streamlit as st
from PIL import Image
import numpy as np

st.title("Deteksi Kematangan Durian AI")

st.write("Web sudah online (mode demo)")

uploaded_file = st.file_uploader("Upload gambar durian")

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Gambar diterima")
    st.write("Mode AI sementara dimatikan agar web stabil")
