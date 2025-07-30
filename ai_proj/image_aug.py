from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt
from PIL import Image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np 


def rotate_img(img_name, folder_path):
    img_path = join(folder_path, img_name)
    # Maximum Rotation
    max_rot = 60
    # ImageDataGenerator
    datagen = ImageDataGenerator(rotation_range=max_rot, fill_mode='nearest')

    # Load Image
    img = Image.open(img_path)
    img = np.asarray(img)
    img = np.expand_dims(img, axis=0)

    # Iterator
    aug_iter = datagen.flow(img, batch_size=1)

    # Generate batch of images
    for i in range(6):
      # Convert to unsigned integers
      image = next(aug_iter)[0].astype('uint8')
      new_image_name = img_name.split('.')[0] + '00' + str(i) + '.jpg'
      n_img = Image.fromarray(image)
      n_img.save(join(folder_path, new_image_name))
      
    print('image rotation done for ' + img_name)


def random_brightness(img_name, folder_path):
    img_path = join(folder_path, img_name)
    # ImageDataGenerator rotation
    datagen = ImageDataGenerator(brightness_range=[0.4,1.9], fill_mode='nearest')
    # Load Image
    img = Image.open(img_path)
    img = np.asarray(img)
    img = np.expand_dims(img, axis=0)

    # iterator
    aug_iter = datagen.flow(img, batch_size=1)

    # generate batch of images
    for i in range(6):

      # convert to unsigned integers
      image = next(aug_iter)[0].astype('uint8')
      new_image_name = img_name.split('.')[0] + '000' + str(i) + '.jpg'
      n_img = Image.fromarray(image)
      n_img.save(join(folder_path, new_image_name))

    print('random brightness done for ' + img_name)

def random_shift(img_name, folder_path):
    img_path = join(folder_path, img_name)
    # ImageDataGenerator rotation
    datagen = ImageDataGenerator(width_shift_range=0.45, height_shift_range=0.45)
    
    # Load Image
    img = Image.open(img_path)
    img = np.asarray(img)
    img = np.expand_dims(img, axis=0)
    
    # iterator
    aug_iter = datagen.flow(img, batch_size=1)
    
    # generate batch of images
    for i in range(6):
      # convert to unsigned integers
      image = next(aug_iter)[0].astype('uint8')
      new_image_name = img_name.split('.')[0] + '0000' + str(i) + '.jpg'
      n_img = Image.fromarray(image)
      n_img.save(join(folder_path, new_image_name))

    print('random shift done for ' + img_name)

def random_flip(img_name, folder_path):
    img_path = join(folder_path, img_name)
    # ImageDataGenerator rotation
    datagen = ImageDataGenerator(horizontal_flip=True, vertical_flip=True)
    
    # Load Image
    img = Image.open(img_path)
    img = np.asarray(img)
    img = np.expand_dims(img, axis=0)
    
    # iterator
    aug_iter = datagen.flow(img, batch_size=1)
    
    # generate batch of images
    for i in range(6):
      # convert to unsigned integers
      image = next(aug_iter)[0].astype('uint8')
      new_image_name = img_name.split('.')[0] + '00000' + str(i) + '.jpg'
      n_img = Image.fromarray(image)
      n_img.save(join(folder_path, new_image_name))

    print('random flip done for ' + img_name)

def random_zoom(img_name, folder_path):
    img_path = join(folder_path, img_name)
    # ImageDataGenerator rotation
    datagen = ImageDataGenerator(zoom_range=[0.3,1.2])
    # Load Image
    img = Image.open(img_path)
    img = np.asarray(img)
    img = np.expand_dims(img, axis=0)
    
    # iterator
    aug_iter = datagen.flow(img, batch_size=1)
    
    # generate batch of images
    for i in range(6):
      # convert to unsigned integers
      image = next(aug_iter)[0].astype('uint8')
      new_image_name = img_name.split('.')[0] + '000000' + str(i) + '.jpg'
      n_img = Image.fromarray(image)
      n_img.save(join(folder_path, new_image_name))

    print('random zoom done for ' + img_name)

image_path = '/home/user/Downloads/ai_proj/data/train/temitope/'
all_images = [f for f in listdir(image_path) if isfile(join(image_path, f))]

# Test Image
for img in all_images:
    print(img)
    rotate_img(img, image_path)
    random_brightness(img, image_path)
    random_shift(img, image_path)
    random_flip(img, image_path)
    random_zoom(img, image_path)
print('Image Augumentation done successfully')






