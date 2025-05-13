import os
import cv2
import sqlite3
from datetime import datetime
from flask import Flask, render_template, request, jsonify, send_file

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
DATABASE = 'database/db_cloud.db'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

if not os.path.exists('database'):
    os.makedirs('database')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Criação da tabela no banco de dados
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS imagens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            processed_filename TEXT,
            datetime TEXT,
            ip TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/image/<filename>')
def uploaded_file(filename):
    file = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    return send_file(file)

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file uploaded'}), 400

    image = request.files['image']
    if image.filename == '':
        return jsonify({'error': 'Empty filename'}), 400

    filename = image.filename
    original_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    image.save(original_path)

    # Processamento com OpenCV
    img = cv2.imread(original_path, cv2.IMREAD_GRAYSCALE)
    edges = cv2.Canny(img, 100, 200)

    processed_filename = f"processed_{filename}"
    processed_path = os.path.join(app.config['UPLOAD_FOLDER'], processed_filename)
    cv2.imwrite(processed_path, edges)

    # Salva no banco
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO imagens (filename, processed_filename, datetime, ip)
        VALUES (?, ?, ?, ?)
    ''', (filename, processed_filename, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), request.remote_addr))
    conn.commit()
    conn.close()

    return render_template('index.html', image_proc=f"/image/{processed_filename}")
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
