import os
# Python program to read and write an image

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.utils import secure_filename


#Configuer application
app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def index():
        if request.method == 'POST':
                f = request.files['input-file']
                filename = secure_filename(f.filename)
                f.save(os.path.join(app.config['UPLOAD_IMG'], filename))
                return render_template("uploaded.html", uploaded_image = filename)
        else:
                return render_template("index.html")
        
@app.route("/uploaded", methods = ['GET', 'POST'])
def uploaded():
    return render_template("/uploaded.html")

@app.route('/uploads/<filename>')
def send_uploaded_file(filename=''):
    from flask import send_from_directory
    return send_from_directory(app.config["IMAGE_UPLOADS"], filename)

if __name__ == '__main__':
    app.run(host='localhost', port=9874)