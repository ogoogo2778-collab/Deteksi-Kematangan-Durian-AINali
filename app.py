import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

st.title("Deteksi Kematangan Durian AI")

model = tf.keras.models.load_model("model.keras")

uploaded_file = st.file_uploader("Upload gambar durian")

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img)

    img = img.resize((150,150))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)

    pred = model.predict(img)
    st.write("Hasil prediksi:", pred)
