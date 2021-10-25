import cv2

img1 = cv2.imread('image/sample2.png')
img2 = img1

rad = int(input())
def checkposition(event, x, y, flags, param):
    """checkposition"""
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = int((int(img1[y+(rad + 1), x, 0]) + int(img1[y-(rad + 1), x, 0]) + int(img1[y, x-(rad + 1), 0]) + int(img1[y, x+(rad + 1), 0]))/4)
        green = int((int(img1[y+(rad + 1), x, 1]) + int(img1[y-(rad + 1), x, 1]) + int(img1[y, x-(rad + 1), 1]) + int(img1[y, x+(rad + 1), 1]))/4)
        red = int((int(img1[y+(rad + 1), x, 2]) + int(img1[y-(rad + 1), x, 2]) + int(img1[y, x-(rad + 1), 2]) + int(img1[y, x+(rad + 1), 2]))/4)
        cv2.circle(img1, (x, y), rad, (int(blue), int(green), int(red)), -1)
        cv2.imshow('After', img1)

cv2.imshow('Before', img2)
cv2.imshow('After', img1)
cv2.setMouseCallback('After', checkposition)
cv2.waitKey(0)
cv2.imwrite('Image.jpg', img1)
cv2.destroyAllWindows()