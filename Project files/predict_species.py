import numpy as np
from keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

# Load the trained model
model = load_model("butterfly_vgg16.h5")

# Class label mapping (must match your training classes order)
class_labels = sorted(os.listdir("data/test"))  # assumes one folder per species

def predict_butterfly_species(img_path):
    # Load and preprocess the image
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0

    # Predict
    prediction = model.predict(img_array)
    predicted_index = np.argmax(prediction)
    predicted_species = class_labels[predicted_index]

    return predicted_species
