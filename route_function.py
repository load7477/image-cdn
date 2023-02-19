from flask import Flask, request, session, send_file, render_template, redirect
import database 
from werkzeug.utils import secure_filename


def main(token):
    try:
        cdn = database.getcdnfile(token)
        filename = cdn['filename']
        print(filename)
        with open(f"cdn/{filename}") as file:
            return send_file(f'cdn/{filename}', mimetype='image/gif')
    except:
        return send_file('cdn/error.png', mimetype='image/gif')

def upload():
    try:
        return render_template('index.html')
    except:
        return send_file('cdn/error.png', mimetype='image/gif')


def uploadapi():
    try:
        f = request.files['file']
        print(f)
        f.save('cdn/' + secure_filename(f.filename))
        token = database.addcdn(f.filename)
        return redirect(f'cdn/{token}')
    except:
        return send_file('cdn/error.png', mimetype='image/gif')