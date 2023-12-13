import os
# Python program to read and write an image

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, send_from_directory
from flask_session import Session
from werkzeug.utils import secure_filename


#Configuer application
app = Flask(__name__)

# Defining upload folder path
upload_folder = os.path.join('static', 'Image')

app.config['UPLOAD_IMG'] = upload_folder

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/uploaded", methods = ['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        elif request.files:
            f = request.files("input-file")
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_IMG'], filename))
            session['f_file_path'] = os.path.join(app.config['UPLOAD_IMG'], filename)
            return render_template("uploaded.html", uploaded_image = filename)
        else:
            return "uploadfail"
        

@app.route("/uploads/<filename>", methods = ['GET', 'POST'])
def send_uploaded_file(filename=''):
    from flask import send_from_directory
    return send_from_directory(app.config["UPLOAD_IMG"], filename)

if __name__ == '__main__':
    app.run(host='localhost', port=9874)