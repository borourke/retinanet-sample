# Run this script then type in:
# retinanet-train --weights resnet50_coco_best_v2.1.0.h5 --batch-size 8 --steps 7248 --epochs 20 --snapshot-path snapshots --tensorboard-dir tensorboard csv dataset/train.csv dataset/classes.csv

from config import bryan_retinanet_config as config
import os
from os import listdir
import cv2
import csv

CLASSES = set()

MAX_TRAINING_DATA = 10000
MAX_TESTING_DATA = 3000

#
# TRAINING DATA
#
train_images_path = config.TRAIN_IMAGES
train_images_directories = listdir(train_images_path)
train_images_directories.remove('.DS_Store')

print("[INFO] Train Images Path: '{}'".format(train_images_path))
print("[INFO] Train Images Files: '{}'".format(train_images_directories))

training_data = []

for directory in train_images_directories:
    print("[INFO] - current directory: '{}'".format(directory))
    image_path = os.path.sep.join([train_images_path, directory])
    for filename in listdir(image_path):
        if(filename == ".DS_Store"):
            next
        elif('.txt' in filename):
            image_name = filename.replace('.txt', '')
            absolute_image_location = "images/train/"+directory+"/"+image_name+".jpg"
            with open(os.path.sep.join([image_path, filename]), "r") as ifile:
                for line in ifile:
                    annotations = line.split()
                    label = annotations[0]
                    x_offset = float(annotations[3])/2*256
                    y_offset = float(annotations[4])/2*256
                    xmin = float(annotations[1])*256-x_offset
                    ymin = float(annotations[2])*256-y_offset
                    xmax = float(annotations[1])*256+x_offset
                    ymax = float(annotations[2])*256+y_offset
                    if(xmin > 256 or xmin < 1 or ymin > 256 or ymin < 1 or xmax > 256 or xmax < 1 or ymax > 256 or ymax < 1):
                        next
                    elif(len(training_data) > MAX_TRAINING_DATA):
                        next
                    else:
                        training_data.append([absolute_image_location, int(xmin), int(ymin), int(xmax), int(ymax), int(label)])
                        CLASSES.add(label)
        else:
            next

with open('dataset/train.csv','w') as f:
    writer = csv.writer(f)
    writer.writerows(training_data)

#
# TESTING DATA
#

test_images_path = config.TEST_IMAGES
test_images_directories = listdir(test_images_path)
if ('.DS_Store' in test_images_directories):
    test_images_directories.remove('.DS_Store')

print("[INFO] Test Images Path: '{}'".format(test_images_path))
print("[INFO] Test Images Files: '{}'".format(test_images_directories))

testing_data = []

for directory in test_images_directories:
    print("[INFO] - current directory: '{}'".format(directory))
    image_path = os.path.sep.join([test_images_path, directory])
    for filename in listdir(image_path):
        if(filename == ".DS_Store"):
            next
        elif('.txt' in filename):
            image_name = filename.replace('.txt', '')
            absolute_image_location = "images/test/"+directory+"/"+image_name+".jpg"
            with open(os.path.sep.join([image_path, filename]), "r") as ifile:
                for line in ifile:
                    annotations = line.split()
                    label = annotations[0]
                    x_offset = float(annotations[3])/2*256
                    y_offset = float(annotations[4])/2*256
                    xmin = float(annotations[1])*256-x_offset
                    ymin = float(annotations[2])*256-y_offset
                    xmax = float(annotations[1])*256+x_offset
                    ymax = float(annotations[2])*256+y_offset
                    if(xmin > 256 or xmin < 1 or ymin > 256 or ymin < 1 or xmax > 256 or xmax < 1 or ymax > 256 or ymax < 1):
                        next
                    elif(len(testing_data) > MAX_TESTING_DATA):
                        next
                    else:
                        testing_data.append([absolute_image_location, int(xmin), int(ymin), int(xmax), int(ymax), int(label)])
                        CLASSES.add(label)
        else:
            next

with open('dataset/test.csv','w') as f:
    writer = csv.writer(f)
    writer.writerows(testing_data)

print("TRAINING DATA LENGTH: '{}'".format(len(training_data)))
print("TEST DATA LENGTH: '{}'".format(len(testing_data)))

print("[INFO] writing classes...")
csv = open('dataset/classes.csv', "w")
rows = [",".join([c, str(i)]) for (i,c) in enumerate(CLASSES)]
csv.write("\n".join(rows))
csv.close()

# im = training_data[-1]
# print(im)
# top_left = (im[1], im[4])
# bottom_right = (im[3], im[2])
# img = cv2.imread(im[0])
# img = cv2.rectangle(img, top_left, bottom_right, (0,255,0), 2)

# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
            
# # import the necessary packages
# from os import listdir
# from config import bryan_retinanet_config as config
# from bs4 import BeautifulSoup
# from imutils import paths
# import argparse
# import random
# import os

# # Create easy variable names for all the arguments
# annot_path = config.ANNOT_PATH
# images_path = config.IMAGES_PATH
# test_images_path = config.TEST_IMAGES
# train_images_path = config.TRAIN_IMAGES
# train_csv = config.TRAIN_CSV
# test_csv = config.TEST_CSV
# classes_csv = config.CLASSES_CSV

# print ("[INFO] Annotation Path: '{}'".format(annot_path))
# print ("[INFO] Images Path: '{}'".format(images_path))
# print ("[INFO] Test Images Path: '{}'".format(test_images_path))
# print ("[INFO] Train Images Path: '{}'".format(train_images_path))
# print ("[INFO] Train CSV: '{}'".format(train_csv))
# print ("[INFO] Test CSV: '{}'".format(test_csv))
# print ("[INFO] Classes CSV: '{}'".format(classes_csv))

# # create the list of datasets to build
# dataset = [ ("train", train_images_path, train_csv),
#             ("test", test_images_path, test_csv)]

# # initialize the set of classes we have
# CLASSES = set()

# # loop over the datasets
# for (dType, imagePaths, outputCSV) in dataset:
#     # load the contents
#     print ("[INFO] creating '{}' set...".format(dType))
#     print ("[INFO] looking in '{}' for images".format(imagePaths))
#     print ("[INFO] {} total images in '{}' set".format(len(listdir(imagePaths)), dType))

#     # open the output CSV file
#     csv = open(outputCSV, "w")

#     # loop over the image paths
#     for filename in listdir(imagePaths):
#         # build the corresponding annotation path
#         print ("[INFO] looking at filename: '{}' ".format(filename))
#         fname = imagePath.split(os.path.sep)[-1]
#         print ("[INFO] looking at filename: '{}' ".format(fname))
#         fname = "{}.xml".format(fname[:fname.rfind(".")])
#         annotPath = os.path.sep.join([annot_path, fname])

#         # load the contents of the annotation file and buid the soup
#         contents = open(annotPath).read()
#         soup = BeautifulSoup(contents, "html.parser")

#         # extract the image dimensions
#         w = int(soup.find("width").string)
#         h = int(soup.find("height").string)

#         # loop over all object elements
#         for o in soup.find_all("object"):
#             #extract the label and bounding box coordinates
#             label = o.find("name").string
#             xMin = int(float(o.find("xmin").string))
#             yMin = int(float(o.find("ymin").string))
#             xMax = int(float(o.find("xmax").string))
#             yMax = int(float(o.find("ymax").string))

#             # truncate any bounding box coordinates that fall outside
#             # the boundaries of the image
#             xMin = max(0, xMin)
#             yMin = max(0, yMin)
#             xMax = min(w, xMax)
#             yMax = min(h, yMax)

#             # ignore the bounding boxes where the minimum values are larger
#             # than the maximum values and vice-versa due to annotation errors
#             if xMin >= xMax or yMin >= yMax:
#                 continue
#             elif xMax <= xMin or yMax <= yMin:
#                 continue

#             # write the image path, bb coordinates, label to the output CSV
#             row = [os.path.abspath(imagePath),str(xMin), str(yMin), str(xMax),
#                     str(yMax), str(label)]
#             csv.write("{}\n".format(",".join(row)))

#             # update the set of unique class labels
#             CLASSES.add(label)

#     # close the CSV file
#     csv.close()

# # write the classes to file
# print("[INFO] writing classes...")
# csv = open(classes_csv, "w")
# rows = [",".join([c, str(i)]) for (i,c) in enumerate(CLASSES)]
# csv.write("\n".join(rows))
# csv.close()