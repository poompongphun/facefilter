import cv2
import numpy as np

img1 = cv2.imread('image/sample2.png')
mask = np.zeros_like(img1)

rad = int(input()) + 1
def checkposition(event, x, y, flags, param):
    """checkposition"""
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(mask, (x, y), rad - 1, (255, 255, 255), -1)
        cv2.circle(img1, (x, y), rad - 1, (0, 0, 0), -1)
        cv2.imshow('test' ,img1)
        cv2.imshow('mask', mask)

cv2.imshow('test', img1)
cv2.imshow('mask', mask)
cv2.setMouseCallback('test', checkposition)
cv2.waitKey(0)
cv2.destroyAllWindows()
mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
dst = cv2.inpaint(img1, mask, 3, cv2.INPAINT_NS)
cv2.imshow('out', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
