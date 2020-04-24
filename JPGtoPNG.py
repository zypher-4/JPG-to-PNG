import sys
import os
from PIL import Image

curent_path = './Photos'
new_path = './Photos/Photos_PNG'

Image.MAX_IMAGE_PIXELS = None


def make_dir():
    try:
        os.mkdir(new_path)
    except FileExistsError:
        pass


def check_files():
    for filename in os.listdir(curent_path):
        if filename.endswith('.jpg') or filename.endswith('.JPG'):
            convert_file(filename)
        else:
            continue


def convert_file(filename):
    global curent_path
    new_filename = ''
    img = Image.open(f'./{curent_path}/{filename}')
    ctr = 0
    for temp in filename:
        if temp == '.':
            break
        ctr += 1
    new_filename = filename[:ctr]
    img.save(f'./{new_path}/{new_filename}.png', 'png')


make_dir()
check_files()
