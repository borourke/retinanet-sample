# import the necessary packages
import os

# initialize the base path for the logos dataset
BASE_PATH = "dataset"

# build the path to the annotations and input images
ANNOT_PATH = os.path.sep.join([BASE_PATH, 'annotations'])
IMAGES_PATH = os.path.sep.join([BASE_PATH, 'images'])
TEST_IMAGES = os.path.sep.join([IMAGES_PATH, 'test'])
TRAIN_IMAGES = os.path.sep.join([IMAGES_PATH, 'train'])

#  build the path to the output training and test .csv files
TRAIN_CSV = os.path.sep.join([BASE_PATH, 'train.csv'])
TEST_CSV = os.path.sep.join([BASE_PATH, 'test.csv'])

# build the path to the output classes CSV files
CLASSES_CSV = os.path.sep.join([BASE_PATH, 'classes.csv'])

# build the path to the output predictions dir
OUTPUT_DIR = os.path.sep.join([BASE_PATH, 'predictions'])