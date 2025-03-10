'''API Routes'''
from flask import request, render_template
import resource_s3

# TODO: Replace with your bucket name
BUCKET_NAME = "hw06-ald21039-1"

def configure_routes(app):
    '''Setup all the API routes'''

    @app.route('/')
    def homepage():
        '''Show the main screen. This is the main entry point for the webapp'''
        return render_template("index.html")

    @app.route('/list_objects')
    def list_files():
        '''Show the main screen'''
        return resource_s3.list_objects(BUCKET_NAME)

    @app.route('/upload', methods = ['POST'])
    def success():
        '''Process the file upload and navigate back to the main screen'''
        if request.method == 'POST':
            file = request.files['file']
            resource_s3.upload_file_to_s3(file, BUCKET_NAME)
            return list_files()
        return "Operation not supported"