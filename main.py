import cv2

img1 = cv2.imread('image/BTsample1.jpg')
img2 = img1

rad = int(input()) + 1
cossin = int(rad*(2**0.5/2))
def checkposition(event, x, y, flags, param):
    """checkposition"""
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = int((int(img1[y+rad, x, 0]) + int(img1[y-rad, x, 0]) + int(img1[y, x-rad, 0]) + int(img1[y, x+rad, 0]) + int(img1[y+cossin, x+cossin, 0]) + int(img1[y+cossin, x-cossin, 0]) + int(img1[y-cossin, x+cossin, 0]) + int(img1[y-cossin, x-cossin, 0]))/8)
        green = int((int(img1[y+rad, x, 1]) + int(img1[y-rad, x, 1]) + int(img1[y, x-rad, 1]) + int(img1[y, x+rad, 1]) + int(img1[y+cossin, x+cossin, 1]) + int(img1[y+cossin, x-cossin, 1]) + int(img1[y-cossin, x+cossin, 1]) + int(img1[y-cossin, x-cossin, 1]))/8)
        red = int((int(img1[y+rad, x, 2]) + int(img1[y-rad, x, 2]) + int(img1[y, x-rad, 2]) + int(img1[y, x+rad, 2]) + int(img1[y+cossin, x+cossin, 2]) + int(img1[y+cossin, x-cossin, 2]) + int(img1[y-cossin, x+cossin, 2]) + int(img1[y-cossin, x-cossin, 2]))/8)
        cv2.circle(img1, (x, y), rad - 1, (int(blue), int(green), int(red)), -1)
        cv2.imshow('After', img1)

cv2.imshow('Before', img2)
cv2.imshow('After', img1)
cv2.setMouseCallback('After', checkposition)
cv2.waitKey(0)
cv2.imwrite('Image.jpg', img1)
cv2.destroyAllWindows()
