#!/usr/bin/env bash

# Install the required libraries
pip3 install numpy scipy h5py
pip3 install scikit-learn Pillow imutils
pip3 install beautifulsoup4
pip3 install tensorflow-gpu
pip3 install keras
pip3 install opencv-contrib-python

# Install Retinanet
cd ~
git clone https://github.com/fizyr/keras-retinanet
cd keras-retinanet
git checkout 42068ef9e406602d92a1afe2ee7d470f7e9860df
python setup.py install