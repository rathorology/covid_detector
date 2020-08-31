import os

import cv2
import argparse
from imutils import paths

import numpy as np
from tensorflow.keras.models import load_model

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
                help="path to input image directory")
ap.add_argument("-m", "--model", type=str, default="model.h5",
                help="path to trained model")
args = vars(ap.parse_args())
# load the image, swap color channels, and resize it to be a fixed
# 224x224 pixels while ignoring aspect ratio
imagePaths = list(paths.list_images(args["dataset"]))
data = []

# loop over the image paths
for imagePath in imagePaths:
    # extract the class label from the filename
    label = imagePath.split(os.path.sep)[-2]

    # load the image, swap color channels, and resize it to be a fixed
    # 224x224 pixels while ignoring aspect ratio
    image = cv2.imread(imagePath)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (224, 224))

    # update the data and labels lists, respectively
    data.append(image)

# convert the data and labels to NumPy arrays while scaling the pixel
# intensities to the range [0, 255]
data = np.array(data) / 255.0
model = load_model(args['model'])
# make predictions on the testing set
predIdxs = model.predict(data)

predIdxs = np.argmax(predIdxs, axis=1)
print(predIdxs)

# label 0 = covid
# lable 1  = normal
