import os
from flask import Flask, render_template, jsonify, request
from flask_uploads import UploadSet, configure_uploads, IMAGES
from deal import dealPicture

icon = UploadSet('PICTURE')

app = Flask(__name__)
app.config['UPLOADED_PICTURE_DEST']='static/uploadPic'
app.config['UPLOADED_PICTURE_ALLOWED']=IMAGES
configure_uploads(app, icon)

@app.route('/', methods=['GET'])
def picture():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    result_json = {
        'status': 'success',
        'error info': ''
    }
    # print(request.files)
    request_json = request.files['file']
    filename = request_json.filename
    path = os.path.join(os.getcwd(), 'static/uploadPic')
    url = os.path.join(path, filename)
    if os.path.exists(url):
        os.remove(url)
    # store picture
    icon.save(request_json, name=filename)
    # deal with the picture in deal.py
    newpicture = dealPicture(filename)
    result_json['src'] = 'static/createPic/'+newpicture
    return jsonify(result_json)


if __name__ == '__main__':
    app.run(debug=True)
