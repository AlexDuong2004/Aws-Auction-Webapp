import logging
import os
from fileinput import filename 
from flask import *  
app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
@app.route('/')   
def main():   
    return render_template("upload-button.html")   
  
@app.route('/success', methods = ['POST'])   
def success():   
    if request.method == 'POST':   
        f = request.files['file'] 
        file_path = os.path.join(UPLOAD_FOLDER, f.filename)
        f.save(file_path)   
        return render_template("success.html", name = f.filename)   
  
if __name__ == '__main__':   
    app.run(debug=True)