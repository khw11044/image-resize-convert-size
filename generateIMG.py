import numpy as np
import os
from os import listdir
from os.path import isfile, join
from PIL import Image
import argparse
 
 
np.random.seed(3)
 
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img


parser = argparse.ArgumentParser(description="generate images")
parser.add_argument('-d', '--directory', type=str, required=True, help='Directory containing the images')
parser.add_argument('-s', '--savedirectory', type=str, required=True, help='Directory savingthe images')
args = parser.parse_args()

 
data_datagen = ImageDataGenerator(rescale=1./255)
 
data_datagen = ImageDataGenerator(rescale=1./255,
                                   rotation_range=30, 
                                   shear_range=5.5,  
                                   width_shift_range=0.1,
                                   height_shift_range=0.1,
                                   zoom_range=0.2,
                                   horizontal_flip=True,
                                   vertical_flip=True,
                                   fill_mode='nearest') 
 

filename_in_dir = []
filename = './' + args.directory
savefilename = './'+ args.savedirectory
counts= 0
for root, dirs, files in os.walk(filename ): #하위폴더
    for  fname in files:
        full_fname = os.path.join(root, fname)
        filename_in_dir.append(full_fname)
 
for file_image in filename_in_dir:
    counts += 1
    print(file_image, counts)
    img = load_img(file_image) 
    x = img_to_array(img)
    x = x.reshape((1,) + x.shape)
 
    i = 0
 
    for batch in data_datagen.flow(x,save_to_dir=savefilename, save_prefix='dronesa', save_format='jpg'):
        i += 1
        if i > 3:
            break
