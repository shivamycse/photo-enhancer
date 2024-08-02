import cv2
import numpy as np
from PIL import Image

def enhance_image(image_path):
    # Load the image
    image = cv2.imread(image_path)
    
    # Convert to RGB (OpenCV uses BGR by default)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Apply Gaussian Blur for denoising
    denoised_image = cv2.fastNlMeansDenoisingColored(image_rgb, None, 10, 10, 7, 21)
    
    # Apply sharpening filter
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    sharpened_image = cv2.filter2D(denoised_image, -1, kernel)
    
    # Convert back to PIL image
    pil_image = Image.fromarray(sharpened_image)
    
    return pil_image
