import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image
import matplotlib.pyplot as plt

# Load a pre-trained OCR model (for example, a CRNN model)
# You can use a trained model from sources like Keras or TensorFlow Hub
# model = load_model('your_ocr_model.h5')

# Load the image
image_path = "image.jpg"
image = Image.open(image_path).convert("L")  # Convert to grayscale
image = image.resize((128, 32))  # Resize to fit the model's input shape

# Normalize and reshape
image = np.array(image) / 255.0  # Normalize pixel values
image = np.expand_dims(image, axis=[0, -1])  # Add batch and channel dimensions

# Predict using the model
# prediction = model.predict(image)

# Dummy output (since we don't have a trained model here)
prediction_text = "Example Text"

# Display result
plt.imshow(Image.open(image_path))
plt.title(f"Extracted Text: {prediction_text}")
plt.axis("off")
plt.show()
