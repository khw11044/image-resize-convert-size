import numpy as np
import os
from os import listdir
from os.path import isfile, join
from PIL import Image
import argparse
import cv2 
 
np.random.seed(3)
 

parser = argparse.ArgumentParser(description="generate images")
parser.add_argument('-d', '--directory', type=str, required=True, help='Directory containing the images')
parser.add_argument('-s', '--savedirectory', type=str, required=True, help='Directory savingthe images')
args = parser.parse_args()


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
    #print(imagename, counts)
    img = cv2.imread(file_image)
    h, w = img.shape[:2]
    M = cv2.getRotationMatrix2D((w/2, h/2), -90, 1)
    Rotatedimg = cv2.warpAffine(img, M, (w, h))
    imagename=file_image.split('\\')[-1]
    cv2.imwrite(savefilename+'/'+imagename,Rotatedimg)
    print(savefilename+'/'+imagename)