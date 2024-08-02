import tensorflow as tf
import numpy as np
from PIL import Image

def load_model(model_path):
    model = tf.keras.models.load_model(model_path)
    return model

def enhance_image_with_srgan(model, image_path):
    # Load and preprocess the image
    image = Image.open(image_path).resize((64, 64))  # Resize if necessary
    image_np = np.array(image) / 255.0
    image_np = np.expand_dims(image_np, axis=0)
    
    # Run inference
    enhanced_image_np = model.predict(image_np)[0]
    
    # Post-process the image
    enhanced_image = Image.fromarray((enhanced_image_np * 255).astype(np.uint8))
    
    return enhanced_image

# Load the model
srgan_model = load_model('app/models/SRGAN.h5')  # Replace with the path to your SRGAN model

# Example usage
def enhance_image(image_path):
    return enhance_image_with_srgan(srgan_model, image_path)
