import cv2
import numpy as np
import dlib

# module สำหรับ การทำ virtual lips

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("predictor/shape_predictor_68_face_landmarks.dat") #Eyes, Eyebrows, Nose, Lips/mouth, Jawline

def the_box(image, points, scale=5, masked = False, cropped = True):
    """Crop จุดที่เราสนใจบนใบหน้ามาปรับแต่ง"""
    if masked:
        mask = np.zeros_like(image)
        mask = cv2.fillPoly(mask, [points], (255, 255, 255))
        image = cv2.bitwise_and(image, mask)
    #cv2.imshow('Mask', image)
    if cropped:
        bbox = cv2.boundingRect(points)
        x, y, w, h = bbox
        img_crop = image[y:y+h,x:x+w]
        img_crop = cv2.resize(img_crop, (0, 0), None, scale, scale)
        return img_crop
    else:
        return mask

def trackfunc(a):
    """trackfunc"""
    pass

cv2.namedWindow("BGR")
cv2.resizeWindow("BGR", 640, 240)
cv2.createTrackbar("Blue", 'BGR', 0, 255, trackfunc)
cv2.createTrackbar("Green", 'BGR', 0, 255, trackfunc)
cv2.createTrackbar("Red", 'BGR', 0, 255, trackfunc)

"""!!!!!!!!!! กด q เพื่อหยุดโปรแกรม"""
while True:
    img = cv2.imread('image/pho1.jpg')
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    img = cv2.resize(img, (0, 0), None, 0.5, 0.5)
    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector(grayscale)
    for face in faces:
        x1, y1 = face.left(), face.top()
        x2, y2 = face.right(), face.bottom()
        #face recognition
        #img = cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
        landmarks = predictor(grayscale, face) #find all landmarks
        pointlist = []
        """draw"""
        for n in range(68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            pointlist.append([x, y])
            #cv2.circle(img, (x, y), 5, (50, 50, 255), cv2.FILLED)
            #show position
            #cv2.putText(img, str(n), (x, y - 10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (0, 0, 255), 1)
        pointlist = np.array(pointlist)
        #img_lefteye = the_box(img, pointlist[36:42])
        #cv2.imshow('LeftEye', img_lefteye)
        """lips"""
        img_lips = the_box(img, pointlist[49: 61], 3, masked=True, cropped=False)
        img_colorlips = np.zeros_like(img_lips)
        """for color track bar"""
        blue = cv2.getTrackbarPos('Blue', 'BGR')
        green = cv2.getTrackbarPos('Green', 'BGR')
        red = cv2.getTrackbarPos('Red', 'BGR')
        """for color track bar"""
        img_colorlips[:] = blue, green, red
        img_colorlips = cv2.bitwise_and(img_lips, img_colorlips)
        img_colorlips = cv2.GaussianBlur(img_colorlips, (7, 7), 10)
        """for color track bar"""
        #grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #grayscale = cv2.cvtColor(grayscale, cv2.COLOR_GRAY2BGR)
        """for color track bar"""
        img_colorlips = cv2.addWeighted(img, 1, img_colorlips, 0.4, 0)
        """for color track bar"""
        cv2.imshow('BGR', img_colorlips)
        """for color track bar"""
        #cv2.imshow('Lips', img_lips)
        #cv2.imshow('before', img)
    cv2.imwrite('test.jpg', img_colorlips)