import cv2
import numpy as np
import dlib

img = cv2.imread('image/BTsample1.jpg')
img = cv2.resize(img, (0, 0), None, 0.5, 0.5)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("predictor/shape_predictor_68_face_landmarks.dat") #Eyes, Eyebrows, Nose, Lips/mouth, Jawline

grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = detector(grayscale)

for face in faces:
    x1, y1 = face.left(), face.top()
    x2, y2 = face.right(), face.bottom()
    #face recognition
    img = cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
    landmarks = predictor(grayscale, face) #find all landmarks
    pointlist = []
    #draw
    for n in range(68):
        x = landmarks.part(n).x
        y = landmarks.part(n).y
        pointlist.append((x, y))
        cv2.circle(img, (x, y), 5, (50, 50, 255), cv2.FILLED)
        #show position
        #cv2.putText(img, str(n), (x, y - 10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (0, 0, 255), 1)

cv2.imshow('Before', img)
cv2.waitKey(0)
cv2.destroyAllWindows()