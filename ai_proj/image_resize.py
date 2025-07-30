from os import listdir
from os.path import isfile, join
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def resize(img_name, folder_path):
    img_path = join(folder_path, img_name)
    test_image = Image.open(img_path)
    test_image = test_image.resize((200, 200))
    test_image = np.asarray(test_image)
    n_img = Image.fromarray(test_image)
    n_img.save(join(folder_path, img_name))

image_path = '/home/user/Downloads/ai_proj/data/train/temitope/'
all_images = [f for f in listdir(image_path) if isfile(join(image_path, f))]

# Test Image
for img in all_images:
    print(img)
    resize(img, image_path)