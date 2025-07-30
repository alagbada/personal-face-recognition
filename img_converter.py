from os import listdir
from os.path import isfile, join
from PIL import Image

def convert_to_jpg(png_path, jpg_path):
    try:
        img = Image.open(png_path)
        img = img.convert('RGB')
        img.save(jpg_path, 'jpeg')
        print('successfully convert to JPEG')
    except FileNotFoundError:
        print(f'Error: PNG file not found at {png_path}')
    except Exception as e:
        print(f'an error occured: {e}')

image_path = '/put-the-right-path-here/default/'
new_image_path = '/put-the-right-path-here/data/train/class1/'
all_images = [f for f in listdir(image_path) if isfile(join(image_path, f))]

# Test Image
for img in all_images:
    convert_to_jpg(join(image_path,img), join(new_image_path, (img.split('.')[0] + '.jpg')))
