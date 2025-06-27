from flask import Flask, render_template, request
import os
from predict_species import predict_butterfly_species

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return "No file part", 400
    file = request.files['image']
    if file.filename == '':
        return "No selected file", 400

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    # Use your model to predict species
    predicted_species = predict_butterfly_species(filepath)

    return render_template('output.html', species=predicted_species, img_path=filepath)

if __name__ == '__main__':
    app.run(debug=True)
