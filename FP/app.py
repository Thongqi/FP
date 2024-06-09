import os
# Python program to read and write an image

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, send_from_directory
from flask_session import Session
from werkzeug.utils import secure_filename

from helpers import largestWord


#Configuer application
app = Flask(__name__)
app.secret_key = "asds"

# Defining upload folder path
upload_folder = os.path.join('static', 'Image')

app.config['UPLOAD_IMG'] = upload_folder

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/uploaded", methods = ['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if request.files:
            f = request.files["input-file"]
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_IMG'], filename))
            session['f_file_path'] = os.path.join(app.config['UPLOAD_IMG'], filename)
            d = largestWord(session.get('f_file_path'))
            return render_template("uploaded.html", uploaded_image = filename, d = d)
        else:
            return "uploadfail"
        

@app.route("/uploads/<filename>", methods = ['GET', 'POST'])
def send_uploaded_file(filename=''):
    from flask import send_from_directory
    return send_from_directory(app.config["UPLOAD_IMG"], filename)



if __name__ == '__main__':
    app.run(host='localhost', port=9874)
    app.debug = True
    app.run()
    app.run(debug = True)