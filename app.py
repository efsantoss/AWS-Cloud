import os
import cv2
from datetime import datetime
from flask import Flask, render_template, request, jsonify, send_file
from werkzeug.utils import secure_filename

app = Flask(__name__)  # CORRIGIDO: __name__ (não _name_)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# ROTA 1 - Página inicial
@app.route('/')
def index():
    return render_template('index.html')

# ROTA 3 - Acessar imagem original ou processada
@app.route('/image/<filename>')
def uploaded_file(filename):
    file = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    return send_file(file)

# ROTA 2 - Upload e processamento da imagem
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file uploaded'}), 400

    image = request.files['image']

    if image.filename == '':
        return jsonify({'error': 'Empty filename'}), 400

    filename = secure_filename(image.filename)
    original_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    image.save(original_path)

    # --- PROCESSAMENTO COM FILTRO DE CANNY (OpenCV) ---
    img = cv2.imread(original_path, cv2.IMREAD_GRAYSCALE)
    edges = cv2.Canny(img, 100, 200)

    processed_filename = f"processed_{filename}"
    processed_path = os.path.join(app.config['UPLOAD_FOLDER'], processed_filename)
    cv2.imwrite(processed_path, edges)

    # --- JSON DE RETORNO (TO DO – PT2) ---
    return jsonify({
        "datetime": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "image": f"/image/{filename}",
        "image_proc": f"/image/{processed_filename}",
        "ip": request.remote_addr
    })

# Execução da aplicação
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
