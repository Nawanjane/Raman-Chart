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
        files = request.files.getlist('file')  # Get a list of files
        filenames = []
        for file in files:
            if file and '.' in file.filename and file.filename.rsplit('.', 1)[1].lower() == 'asc':
                filename = file.filename
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)
                filenames.append(filename)
        return redirect(url_for('chart', filenames=','.join(filenames)))
    return render_template('index.html')


@app.route('/chart/<filenames>')
def chart(filenames):
    filenames = filenames.split(',')
    datasets = []
    for filename in filenames:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        shifts, intensities = read_asc_file(file_path)
        datasets.append({'shifts': shifts, 'intensities': intensities, 'label': filename})
    return render_template('chart.html', datasets=datasets)


if __name__ == '__main__':
    app.run(debug=True)
