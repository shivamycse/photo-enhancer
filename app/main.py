from flask import Flask, request, render_template, send_file, jsonify
from app.enhance_image import enhance_image
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.config['UPLOAD_FOLDER'] = os.path.join(BASE_DIR, 'static', 'uploads')
app.config['PROCESSED_FOLDER'] = os.path.join(BASE_DIR, 'static', 'processed')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        file = request.files['file']
        if file:
            upload_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            processed_path = os.path.join(app.config['PROCESSED_FOLDER'], file.filename)

            file.save(upload_path)
            print(f"Uploaded Path: {upload_path}")

            enhanced_image = enhance_image(upload_path)
            enhanced_image.save(processed_path)
            print(f"Processed Path: {processed_path}")

            # Return URL for download
            file_url = os.path.join('static', 'processed', file.filename)
            return jsonify({"url": '/' + file_url})
        else:
            return jsonify({"error": "No file uploaded"}), 400
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
