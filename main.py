import cv2
import math

def getAvgColor(img, position, rlong, num, channel):
    """get average color""" # this function you can fix point in circle for avg !!
    posi_x, posi_y = position # position of img you want to average
    step, degree = 360 / num, 0
    all_color = [] # keep all color around circle <-(length of this list == num)
    for _ in range(num): # this loop add color point around img https://bit.ly/3qbZGSA (number of circle point is up to num)
        radian = math.radians(degree) # degee to radian
        all_color.append(int(img[int(posi_y + rlong * math.sin(radian)), \
        int(posi_x + rlong * math.cos(radian)), channel])) # get color from img (1 channel)
        degree += step
    return sum(all_color) // num

def clearAcne(img):
    """checkposition"""
    acne_cascade = cv2.CascadeClassifier('cascade/acneCascade.xml')
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faceDetected, rejectLevels, levelWeights = acne_cascade.detectMultiScale3(gray_img, 4, 3, outputRejectLevels = 1)
    margin = 2 # margin between detect and remove
    for i in range(len(faceDetected)):
        (x, y, w, h) = faceDetected[i] # face position
        if levelWeights[i] >= 2: # check confidence
            posi_x, posi_y, rad = x + (w//2), y + (h//2), w//2 # this position use for clear ance
            BGR = tuple(getAvgColor(img, (posi_x, posi_y), rad - margin, 8, i) for i in range(3)) # this line return BGR Color (0, 0, 0)
            cv2.circle(img, (posi_x, posi_y), rad - margin, BGR, -1) # use circle to replace avg color!

            # cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2) # if you want to debug -> Ctrl + /
            # cv2.putText(img, "%.5f" % levelWeights[count], (x, y-5), cv2.FONT_ITALIC, 0.5, (255, 0, 0), 1) # if you want to debug -> Ctrl + /

img1 = cv2.imread('image/sample1.jpg')
img2 = img1.copy()
clearAcne(img1)
cv2.imshow('Before', img2)
cv2.imshow('After', img1)
cv2.waitKey(0)
# cv2.imwrite('Image.jpg', img1)
cv2.destroyAllWindows()
