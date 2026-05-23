import streamlit as st
from PIL import Image
import numpy as np

st.title("🍈 Deteksi Kematangan Durian AINali")

uploaded_file = st.file_uploader("Upload gambar durian", type=["jpg", "png", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Gambar masuk")

    st.write("🔍 Analisis AINali sedang berjalan...")

    # simulasi AI
    score = np.random.rand()

    if score < 0.33:
        hasil = "Mentah"
        estimasi_hari = np.random.randint(3, 7)
        status = f"Perkiraan matang dalam ± {estimasi_hari} hari"
    elif score < 0.66:
        hasil = "Matang"
        status = "Sudah siap dikonsumsi 🍈"
    else:
        hasil = "Busuk"
        status = "Tidak layak konsumsi ❌"

    # OUTPUT (HARUS DI LUAR IF/ELSE)
    st.success(f"Hasil Prediksi: {hasil}")
    st.info(status)
    st.write("Confidence:", round(score, 2))
