import streamlit as st
import numpy as np
from PIL import Image
import gdown
import os
import tensorflow as tf

st.title("Deteksi Kematangan Durian AI")

MODEL_PATH = "model.keras"

# download model jika belum ada
if not os.path.exists(MODEL_PATH):
    url = "https://drive.google.com/uc?id=1-gTWOCSauzsXtjRWI3Yd-6lrEzaDbXe0"
    gdown.download(url, MODEL_PATH, quiet=False)

# load model SEKALI saja
model = tf.keras.models.load_model(MODEL_PATH)

uploaded_file = st.file_uploader("Upload gambar durian")

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img)

    img = img.resize((150, 150))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)

    pred = model.predict(img)
    st.write("Hasil prediksi:", pred)
