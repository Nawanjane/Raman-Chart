# app.py
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
from scripts.process_file import read_asc_file

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('file')
        if file and '.' in file.filename and file.filename.rsplit('.', 1)[1].lower() == 'asc':
            filename = file.filename
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            return redirect(url_for('chart', filename=filename))
    return render_template('index.html')

@app.route('/chart/<filename>')
def chart(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    shifts, intensities = read_asc_file(file_path)
    return render_template('chart.html', shifts=shifts, intensities=intensities)

if __name__ == '__main__':
    app.run(debug=True)
