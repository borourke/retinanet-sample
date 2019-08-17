import os
from os import listdir
import cv2

real_images_path = "dataset/images/real"
predictions_path = "dataset/predictions"

real_images = listdir(real_images_path)
real_images.remove(".DS_Store")

for image in real_images:
    text_name = image.replace('.jpg', '.txt')
    text_name = text_name.replace('.png', '.txt')
    img = cv2.imread(os.path.sep.join([real_images_path, image]))
    with open(os.path.sep.join([predictions_path, text_name]), "r") as ifile:
        for line in ifile:
            # <classname>-0 <confidence>-1 <ymin>-2 <xmin>-3 <ymax>-4 <xmax>-5
            annotations = line.split()
            top_left = (int(annotations[3]), int(annotations[4]))
            bottom_right = (int(annotations[5]), int(annotations[2]))
            img = cv2.rectangle(img, top_left, bottom_right, (0,255,0), 2)
    cv2.imwrite(os.path.sep.join([predictions_path, image]), img)
