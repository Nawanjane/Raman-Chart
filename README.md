# Raman Data Analysis Application

## Introduction
This application, created by Nimendra Nawanjana, is designed to facilitate the analysis of Raman spectroscopy raw data. 
Users can upload `.asc` files, and the application will display a chart comparing the Raman shifts and intensities from the uploaded files.

## Features
- Upload and analyze `.asc` files containing Raman spectroscopy data.
- View and compare multiple Raman shift charts on a single graph.
- Interactive chart with zoom and pan capabilities.

## Installation Guide

### Prerequisites
Before you begin, ensure you have the following installed on your system:
- Python 3.6 or higher
- pip (Python package installer)

### Clone the Repository
First, clone the repository to your local machine using Git:

```bash
git clone git@github.com:Nawanjane/Raman-Chart.git
cd raman-data-analysis
```

### Set Up a Virtual Environment (Optional but Recommended)
It is a good practice to create a virtual environment for your project to manage dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### Install Dependencies
Install the required Python packages using pip:
```bash
pip install -r requirements.txt
```

### Run the Application
Start the Flask application with the following command:
```bash
export FLASK_APP=app.py
flask run
```
The application should now be running on http://localhost:5000/. Open this URL in a web browser to use the application.


### Usage
To analyze your Raman data:

Navigate to http://localhost:5000/ in your web browser.
Click the "Choose File" button and select one or more .asc files to upload.
Click the "Upload and Analyze" button to view the Raman shift chart(s) for the uploaded file(s).

### Contributing
Contributions to the Raman Data Analysis application are welcome. Please feel free to fork the repository, make changes, and submit pull requests.

### License
This project is licensed under the MIT License - see the LICENSE file for details.







