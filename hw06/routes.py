'''API Routes for the web app'''
from flask import request, render_template, Flask, Response, jsonify
import resource_s3

# TODO: Replace with your bucket name
BUCKET_NAME = "hw06-ald21039-1"
app = Flask(__name__)


##def configure_routes(app):
    ##'''Setup all the API routes'''

@app.route('/')
def homepage():
    '''Show the main screen. This is the main entry point for the webapp'''
    print("Booting up the homepage")
    return render_template("index.html")

@app.route('/list_objects')
def list_files():
    '''Show the main screen'''
    print("attemptiing to show list of objects")
    return resource_s3.list_objects(BUCKET_NAME)

@app.route('/upload', methods = ['POST'])
def success():
    '''Process the file upload and navigate back to the main screen'''
    if request.method == 'POST':
        file = request.files['file']
        resource_s3.upload_file_to_s3(file, BUCKET_NAME)
        print("File successfully uploaded")
        return list_files()
    return "Operation not supported"

@app.route('/get_thumbnail')
def get_thumbnail():
    '''Returns the thumb_nail'''
    obj_key = request.args.get('obj')

    if not obj_key:
        return jsonify({'error': 'Missing object key'}), 400
    thumbnail = resource_s3.generate_thumbnail(BUCKET_NAME, obj_key)

    if thumbnail:   
        print("successfully got the thumbnail")
        return Response(thumbnail, content_type='image/jpeg')  
    else:
        return jsonify({'error': 'Object not found'}), 404
    
#configure_routes(app)
if __name__ == '__main__':
    #configure_routes(app)
    #app.run(host="0.0.0.0", port=5000)
    app.run()
