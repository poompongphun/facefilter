import cv2
import math

def getAvgColor(img, position, rlong, num, channel):
    """get average color"""
    posi_x, posi_y = position
    step, degree = 360 / num, 0
    all_color = []
    for _ in range(num):
        radian = math.radians(degree)
        all_color.append(int(img[int(posi_y + rlong * math.sin(radian)), int(posi_x + rlong * math.cos(radian)), channel]))
        degree += step
    return sum(all_color) // num

def clearAcne(img):
    """checkposition"""
    # if event == cv2.EVENT_LBUTTONDOWN:
    acne_cascade = cv2.CascadeClassifier('cascade/acneCascade.xml')
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faceDetected, rejectLevels, levelWeights = acne_cascade.detectMultiScale3(gray_img, 4, 3, outputRejectLevels = 1)
    margin = 2
    count = 0
    for (x, y, w, h) in faceDetected: # face position
        if levelWeights[count] >= 2:
            posi_x, posi_y, rad = x + (w//2), y + (h//2), w//2
            BGR = tuple(getAvgColor(img, (posi_x, posi_y), rad - margin, 8, i) for i in range(3))
            cv2.circle(img, (posi_x, posi_y), rad - margin, BGR, -1)
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            # cv2.putText(img, "%.5f" % levelWeights[count], (x, y-5), cv2.FONT_ITALIC, 0.5, (255, 0, 0), 1)
            # cv2.imshow('After', img)
        count += 1

img1 = cv2.imread('image/pho1.jpg')
img2 = img1.copy()
clearAcne(img1)
cv2.imshow('Before', img2)
cv2.imshow('After', img1)
# cv2.setMouseCallback('After', checkposition)
cv2.waitKey(0)
# cv2.imwrite('Image.jpg', img1)
cv2.destroyAllWindows()
