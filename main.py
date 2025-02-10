from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect
from upload import *
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')
csrf = CSRFProtect(app)

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])

def home():
    return render_template('index.html')

UPLOAD_FOLDER=os.environ.get('UPLOAD_FOLDER')
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload():
    return upload_file(app)

if __name__=='__main__':
    app.run(debug=True)