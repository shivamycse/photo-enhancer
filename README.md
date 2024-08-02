# Photo Enhancer Application

## Overview

This project is a Flask-based web application that allows users to upload blurry and noisy photos for enhancement. The application uses a pre-trained Super-Resolution Generative Adversarial Network (SRGAN) model to enhance the clarity and quality of the uploaded images. The enhanced images can then be downloaded in full quality.

## Features

- Upload blurry or noisy photos.
- Enhance the photos using an SRGAN model.
- Download the processed images in full quality.

## Project Structure

- `run.py`: Entry point for running the Flask application.
- `app/`: Directory containing the main application code.
  - `main.py`: Contains the Flask application and routing logic.
  - `enhance_image.py`: Contains the image enhancement logic using SRGAN.
  - `static/`: Contains static files such as CSS, JavaScript, and images.
    - `processed/`: Directory where processed images are saved.
  - `templates/`: Contains HTML templates.
    - `index.html`: Main user interface for uploading and displaying images.
  - `models/`: Directory for storing pre-trained models (e.g., `SRGAN.h5`).
  - `wsgi.py`: WSGI entry point for the Flask application.
- `requirements.txt`: Lists the Python dependencies for the project.

## Setup and Installation

### Prerequisites

- Python 3.x
- Flask
- TensorFlow
- Other Python dependencies listed in `requirements.txt`

### Installation Steps

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd photo-enhancer

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt

4. **Download and Place SRGAN Model**
   
 - Download the SRGAN model file (SRGAN.h5) from this link or another source.
 - Place the model file in the app/models/ directory.

5. **Run the Application**
   
   ```bash
   python run.py

  **The application will be available at http://127.0.0.1:5000**

## Usage

1. **Upload a Photo**
   - Go to the application URL.
   - Click the "Choose File" button to select a photo.
   - Click "Enhance" to process the photo.

2. **Download the Processed Photo**
   - After enhancement, you will see a link to download the processed image.

## Troubleshooting

- **Model Loading Issues**: Verify the path to the SRGAN model file is correct in `app/enhance_image.py`.
- **File Not Found Errors**: Check paths for static files and processed images.
- **Internal Server Errors**: Review Flask logs for detailed error messages.

## Contribution

If you want to contribute to this project, please fork the repository, make changes, and submit a pull request.


## Contact

For questions or issues, contact [shivamycse@gmail.com](mailto:shivamycse@gmail.com).



