# import the necessary packages
from PIL import Image
import pytesseract
import argparse
import cv2
import os
import numpy as np
import datetime
from numpy import genfromtxt


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image to be OCR'd")
ap.add_argument("-p", "--preprocess", type=str, default="thresh",
	help="type of preprocessing to be done")
args = vars(ap.parse_args())


# load the example image and convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# check to see if we should apply thresholding to preprocess the
# image
if args["preprocess"] == "thresh":
	gray = cv2.threshold(gray, 0, 255,
		cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
# make a check to see if median blurring should be done to remove
# noise
elif args["preprocess"] == "blur":
	gray = cv2.medianBlur(gray, 3)
# write the grayscale image to disk as a temporary file so we can
# apply OCR to it
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)

# load the image as a PIL/Pillow image, apply OCR, and then delete
# the temporary file
text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)


list = text.split('\n')
print(len(list))
print('    ------    ')
cleanlist = [x for x in list if (any(c == '£' for c in x) and ("VISA" not in x) and ("DUE" not in x))]
print(cleanlist)

names = ["Name of Item"]
price = ["Price of Item"]
for item in cleanlist:
	nameprice = item.split()
	name = ""
	for x in range(0,len(nameprice)-1):
		name = name + nameprice[x]+ " "
	names.append(name)
	price.append(nameprice[-1])
npname = np.array(names).reshape(-1, 1)
npprice = np.array(price).reshape(-1, 1)
print(npname)
separated = np.concatenate((npname, npprice), axis=1)
print(separated)
today = datetime.datetime.now()
dateFormat = "week " + today.strftime("%U") + ".csv"
if(os.path.isfile(dateFormat)):
	loadedData = genfromtxt(dateFormat, delimiter=',',dtype=None,encoding="utf8" )
	print(loadedData)
	newdata = np.concatenate((loadedData, separated), axis=1)
	np.savetxt(dateFormat, newdata, delimiter=",",fmt='%s')
else:
	np.savetxt(dateFormat, separated, delimiter=",",fmt='%s')
