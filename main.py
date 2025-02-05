import os
from flask import Flask, flash, request, redirect, url_for,render_template
from werkzeug.utils import secure_filename

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

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_folder_structure(file_list):
    print(str(file_list))
    file_list= file_list[1:]
    folder_paths = list()
    for file_storage in file_list:
        file_path = str(file_storage).split("'")[1]
        path_parts = file_path.split('/')
        current_path = ""
        for part in path_parts[:-1]:  # Exclude the file name (last part)
            if current_path:
                current_path = f"{current_path}/{part}"
            else:
                current_path = part
            folder_paths.append(current_path)
    return folder_paths

@app.route('/upload', methods=['POST'])
def upload_file():
    files=[]
    i=-1
    if request.method == 'POST':
        files = request.files.getlist("file")
        folders = extract_folder_structure(files)

        for index, file in enumerate(files, start=-1):
            print (file)
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                print("PRINT STATEMENT: ", file.filename)
                filename = secure_filename(file.filename)
                if folders!=[]:
                    os.chdir(app.config['UPLOAD_FOLDER'])
                    os.makedirs(folders[index],exist_ok=True)
                    os.chdir(folders[index])
                    file.save(filename)
                else: 
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))         
                #Commented out for now: return redirect(url_for('home'))
    return redirect(url_for('home'))

if __name__=='__main__':
    app.run(debug=True)