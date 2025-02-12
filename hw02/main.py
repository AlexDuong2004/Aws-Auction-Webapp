import os
from fileinput import filename 
from flask import *  
import datetime
app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
@app.route('/')   
def main():   
    return render_template("upload-button.html")   

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)
  
@app.route('/success', methods = ['POST'])   
def success():   
    if request.method == 'POST':   
        f = request.files['file'] 
        file_path = os.path.join(UPLOAD_FOLDER, f.filename)
        f.save(file_path)   
        return render_template("success.html", name = f.filename)   
    
@app.route('/return', methods = ['GET'])
def return_files():
    if request.method == 'GET':
        file_info = []
        uploaded_files = os.listdir(UPLOAD_FOLDER)
        for file in uploaded_files:
            file_path = os.path.join(UPLOAD_FOLDER, file)
            size = os.path.getsize(file_path)
            modified_time = os.path.getmtime(file_path)  
            modified_date = datetime.datetime.fromtimestamp(modified_time).strftime('%Y-%m-%d %H:%M:%S')
            file_info.append({
                'name': file,
                'size': size,
                'modified_date': modified_date,
                'url': f'/uploads/{file}'
            })
        return render_template("return.html", files=file_info)

  
if __name__ == '__main__':   
    app.run(host='0.0.0.0', port=5000)