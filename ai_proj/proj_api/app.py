from flask import Flask, request, Response
from flask_cors import CORS
import numpy as np
import keras
import base64
from io import BytesIO
from PIL import Image

ALLOWED_EXTENSIONS = {'jpg', 'jpeg'}

app = Flask(__name__)
CORS(app)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.post('/predict-image')
def upload_file():
    try:
        if 'file' not in request.files:
            return Response("No file was uploaded", status=400)
        file = request.files['file']
        if file.filename == '':
            return Response('No file was selected', status=400)
        if not allowed_file(file.filename):
            return Response('Invalid extension - upload jpeg', status=400)
        return Response(str(test_image(file.stream)), status=200)
    except Exception as e:
        message = str(e)
        return Response(message, status=400)
    
@app.post('/predict-base64-image')
def predict_base64():
    try:
        b64_string = request.form['base64_img']
        if ',' in b64_string:
            b64_string = b64_string.split(',')[1]
        img_data = base64.b64decode(b64_string)
        img_stream = BytesIO(img_data)
        
        return Response(str(test_image(img_stream)), status=200)
    except Exception as e:
        message = str(e)
        return Response(message, status=400)


def test_image(filestream) -> float:
    test_image = Image.open(filestream)
    if test_image.format != 'JPEG':
        raise Exception('Invalid format - only JPEG is allowed')
    test_image = test_image.resize((200, 200))
    test_image = np.asarray(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    model_path = '../model/new_model/my_face_classifier_model'
    new_model = keras.models.load_model(model_path)
    result = new_model.predict(test_image)
    app.logger.debug(f'result is: {result[0][0]}')
    return result[0][0]

if __name__ == '__main__':
    app.run(debug=True)