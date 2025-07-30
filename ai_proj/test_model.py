from os import listdir
from os.path import isfile, join
import numpy as np
import keras
from keras import layers
import matplotlib.pyplot as plt
from PIL import Image
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img


image_path = '/home/user/Downloads/ai_proj/test/d33.jpg'
test_image = Image.open(image_path)
test_image = test_image.resize((200, 200))
test_image = np.asarray(test_image)
test_image = np.expand_dims(test_image, axis = 0)

model_path = '/home/user/Downloads/ai_proj/model/new_model/my_face_classifier_model'
new_model = keras.models.load_model(model_path)

new_model.summary()
result = new_model.predict(test_image)
print(result)
