import cv2
import datetime
import os
import pathlib

def cropImg(img):
    """checkposition"""
    acne_cascade = cv2.CascadeClassifier('cascade/cascade.xml')
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faceDetected, rejectLevels, levelWeights = acne_cascade.detectMultiScale3(gray_img, outputRejectLevels = 1)
    for i in range(len(faceDetected)):
        (x, y, w, h) = faceDetected[i]
        cropped_image = img[y:y+h, x:x+w]
        cv2.imwrite('detected/%s%d.jpg' % (datetime.datetime.now().strftime("%f"), i), cropped_image)

img1 = cv2.imread('image\picture\istockphoto-174763312-612x612.jpg')
if not pathlib.Path("detected").exists():
    print("No")
    os.mkdir("detected")
cropImg(img1)
