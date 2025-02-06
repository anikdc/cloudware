import os
import re
from flask import Flask, flash, request, redirect, url_for,render_template

app = Flask(__name__)
app.secret_key = 'aiwillkillme'

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    form=upload_file()
    return render_template('index.html', form=form)

UPLOAD_FOLDER="C:\\Users\\anik2\\OneDrive\\Documents\\College"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'rar'}
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER

def sanitize_filename(filename):
    filename = filename.replace('\0', '')
    filename = re.sub(r'[<>:"/\\|?*]', '', filename)
    filename = filename.lstrip('.')
    return filename

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
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
                    os.chdir(app.config['UPLOAD_FOLDER'])
                    os.makedirs(directory,exist_ok=True)
                    os.chdir(directory)
                    file.save(filename)
                else: 
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return redirect(url_for('home'))

if __name__=='__main__':
    app.run(debug=True)