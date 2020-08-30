# import the necessary packages
from imutils import paths
import argparse
import random
import shutil
import os

if not os.path.exists("../keras-covid-19/data"):
    os.makedirs("../keras-covid-19/data")
if not os.path.exists("../keras-covid-19/data/normal"):
    os.makedirs("../keras-covid-19/data/normal")
imagePaths = list(paths.list_images("../chest_xray/train/NORMAL"))

# randomly sample the image paths
random.seed(42)
random.shuffle(imagePaths)
imagePaths = imagePaths[:200]

# loop over the image paths
for (i, imagePath) in enumerate(imagePaths):
    # extract the filename from the image path and then construct the
    # path to the copied image file
    filename = imagePath.split(os.path.sep)[-1]
    outputPath = os.path.sep.join(["../data/normal/", filename])

    # copy the image
    shutil.copy2(imagePath, outputPath)
