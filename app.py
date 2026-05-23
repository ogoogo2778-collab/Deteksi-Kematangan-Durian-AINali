import streamlit as st
from PIL import Image
import numpy as np

st.title("🍈 Deteksi Kematangan Durian AI")

uploaded_file = st.file_uploader("Upload gambar durian", type=["jpg", "png", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Gambar masuk")

    st.write("🔍 Analisis AI sedang berjalan...")

    # simulasi hasil (biar tetap ada output)
    score = np.random.rand()

    if score < 0.33:
        hasil = "Mentah"
    elif score < 0.66:
        hasil = "Matang"
    else:
        hasil = "Busuk"

    st.success(f"Hasil Prediksi: {hasil}")
    st.write("Confidence:", round(score, 2))
