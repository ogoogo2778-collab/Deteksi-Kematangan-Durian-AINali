import gdown
import os
import tensorflow as tf

MODEL_PATH = "model.keras"

if not os.path.exists(MODEL_PATH):
    url = "https://drive.google.com/uc?id=1-gTWOCSauzsXtjRWI3Yd-6lrEzaDbXe0"
    gdown.download(url, MODEL_PATH, quiet=False)

model = tf.keras.models.load_model(MODEL_PATH)
