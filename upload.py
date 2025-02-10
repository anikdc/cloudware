import os
import re
from main import *
from flask import flash, redirect, url_for, request, app, jsonify

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'rar'}

def __init__(self, app):
    self.app = app
    
def sanitize_filename(filename):
    filename = filename.replace('\0', '')
    filename = re.sub(r'[<>:"/\\|?*]', '', filename)
    filename = filename.lstrip('.')
    return filename

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_file(app):
    uploaded_files=[]
    if request.method == 'POST':
        files = request.files.getlist("file")
        for index, file in enumerate(files, start=-1):
            if file == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                directory = os.path.dirname(file.filename)
                filename = os.path.basename(file.filename)
                filename = sanitize_filename(filename)
                if directory:
                    full_directory = os.path.join(app.config['UPLOAD_FOLDER'], directory)
                    os.makedirs(full_directory, exist_ok=True)
                    file.save(os.path.join(full_directory, filename))
                else: 
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                uploaded_files.append(filename)
    return jsonify({
        'message': 'Files uploaded successfully',
        'files': uploaded_files
    })