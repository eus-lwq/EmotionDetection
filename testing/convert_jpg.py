import os
import csv
import cv2
import argparse
import numpy as np 
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', required=True, help="path of the csv file")
parser.add_argument('-o', '--output', required=True, help="path of the output directory")
args = parser.parse_args()
w, h = 48, 48
image = np.zeros((h, w), dtype=np.uint8)
id = 1
with open(args.file, 'r') as csvfile:
    datareader = csv.reader(csvfile, delimiter =',')

    headers = next(datareader)
    print (headers)

    for row in datareader: 
        emotion = row[0]
        #print(row[1])
        pixels = map(int, row[2].split()) # create object if int from each pixel number 
        pixel_list = list(pixels)
        usage = row[1]
        print (emotion, type(pixel_list[0]), usage)
        pixels_array = np.asarray(pixel_list)
        image = pixels_array.reshape(w, h)
        #print image.shape
        stacked_image = np.dstack((image,) * 3)
        # print (stacked_image.shape)
        image_folder = os.path.join(args.output, usage, emotion)
        if not os.path.exists(image_folder):
            os.makedirs(image_folder)
        image_file =  os.path.join(image_folder , str(id) + '.jpg')
        print (image_file)
        sig = cv2.imwrite(image_file,stacked_image)
        id += 1 
        if id % 100 == 0:
            print('Processed {} images'.format(id))

print("Finished processing {} images".format(id))
