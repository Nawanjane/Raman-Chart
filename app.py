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
        files = request.files.getlist('file')
        stack = 'stack' in request.form  # Check if the stack checkbox is checked
        filenames = []
        for file in files:
            if file and '.' in file.filename and file.filename.rsplit('.', 1)[1].lower() == 'asc':
                filename = file.filename
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)
                filenames.append(filename)
        return redirect(url_for('chart', filenames=','.join(filenames), stack=stack))
    return render_template('index.html')


@app.route('/chart/<filenames>')
def chart(filenames):
    stack = request.args.get('stack') == 'True'
    filenames = filenames.split(',')
    datasets = []
    all_intensities = []  # List to hold all intensity lists

    # Read and store intensities from all files
    for filename in filenames:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        shifts, intensities = read_asc_file(file_path)
        all_intensities.append(intensities)

    if stack:
        # Calculate the average intensity for each shift
        # This assumes all files have the same number of data points and corresponding shifts
        averaged_intensities = [sum(x) / len(x) for x in zip(*all_intensities)]
        datasets = [{'shifts': shifts, 'intensities': averaged_intensities, 'label': 'Averaged Data'}]
    else:
        for filename, (shifts, intensities) in zip(filenames, all_intensities):
            datasets.append({'shifts': shifts, 'intensities': intensities, 'label': filename})

    return render_template('chart.html', datasets=datasets)



if __name__ == '__main__':
    app.run(debug=True)
