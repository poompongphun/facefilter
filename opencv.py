import cv2
# img = cv2.imread("learn_project\images\shark.jpg", 0)
# cv2.imshow("Image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.imwrite("learn_project/images/result.jpg", img)


# cap = cv2.VideoCapture("learn_project/video/vdo.mp4")
# while True:
#     ret, frame = cap.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     cv2.imshow("Frame", gray)
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break
# cap.release()
# cv2.destroyAllWindows()

# img = cv2.imread("learn_project\images\shark.jpg")
# img = cv2.line(img, (0, 0), (255, 255), (0, 255, 0), 10)
# img = cv2.arrowedLine(img, (0, 0), (400, 400), (255, 0, 0), 10)
# img = cv2.rectangle(img, (384, 0), (510, 128), (255, 0, 0), 10)
# img = cv2.circle(img, (400, 80), 63, (255, 0, 0), 1)
# img = cv2.putText(img, "Hello World", (100, 400), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 0, 0), 10)
# cv2.imshow("Image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eyeCascade = cv2.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")
mouthCascade = cv2.CascadeClassifier("Mouth.xml")
glasses = cv2.imread("images\glasses.png")
# noseCascade = cv2.CascadeClassifier("learn_project/Nariz.xml")
def draw_boundary(img, classifier, scaleFacetor, minNeighbors, color, text):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale(gray, scaleFacetor, minNeighbors)
    coords = []
    for x, y, w, h in features:
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
        cv2.putText(img, text, (x, y-5), cv2.FONT_ITALIC, 1, color, 1)
        coords = [x, y, w, h]
    return img, coords
def detect(img, faceCascade, eyeCascade, mouthCascade):
    img, coords = draw_boundary(img, faceCascade, 1.1, 10, (255, 0, 0), "Face")
    img, coords = draw_boundary(img, eyeCascade, 1.1, 10, (0, 255, 0), "Eye")
    img, coords = draw_boundary(img, mouthCascade, 1.1, 25, (0, 0, 255), "Mouth")
    return img
cap = cv2.VideoCapture(0)

original_glasses_h, original_glasses_w, glasses_channels = glasses.shape
glasses_gray = cv2.cvtColor(glasses, cv2.COLOR_BGR2GRAY)
ret, original_mask = cv2.threshold(glasses_gray, 10, 255, cv2.THRESH_BINARY_INV)
original_mask_inv = cv2.bitwise_not(original_mask)
while True:
    ret, frame = cap.read()
    frame = detect(frame, faceCascade, eyeCascade, mouthCascade)
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()