import streamlit as st
import numpy as np
from PIL import Image
import gdown
import os
import tensorflow as tf

st.set_page_config(page_title="Durian AI", layout="centered")

st.title("🍈 Deteksi Kematangan Durian AI")

MODEL_PATH = "model.keras"

# =========================
# DOWNLOAD MODEL
# =========================
if not os.path.exists(MODEL_PATH):
    url = "https://drive.google.com/uc?id=1-gTWOCSauzsXtjRWI3Yd-6lrEzaDbXe0"
    gdown.download(url, MODEL_PATH, quiet=False)

# =========================
# LOAD MODEL (SAFE)
# =========================
@st.cache_resource
def load_model():
    return tf.keras.models.load_model(MODEL_PATH)

model = load_model()

# =========================
# UI UPLOAD
# =========================
uploaded_file = st.file_uploader("📤 Upload gambar durian", type=["jpg", "png", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Gambar yang diupload", use_container_width=True)

    # preprocess
    img = img.resize((150, 150))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)

    # predict
    pred = model.predict(img)
    kelas = np.argmax(pred)

    # label (ubah sesuai dataset kamu)
    label = ["mentah", "matang", "busuk"]

    st.success(f"🍈 Hasil Prediksi: **{label[kelas]}**")

    st.write("Probabilitas:", pred)
