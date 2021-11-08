import cv2
import math

import numpy as np
from typing import Optional
from fastapi import FastAPI, File, UploadFile, Response, HTTPException
app = FastAPI()

@app.post("/")
async def read_root(img: UploadFile = File(...), debug: Optional[str] = None):
    contents = await img.read()
    if contents:
        nparr = np.fromstring(contents, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        clearAcne(img, str(debug).lower() == "true")
        img_byte = bytes(cv2.imencode('.png', img)[1])
        return Response(content=img_byte, media_type="image/webp")
    else:
        raise HTTPException(status_code=400, detail="Please select images")

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

def clearAcne(img, debug=False):
    """checkposition"""
    acne_cascade = cv2.CascadeClassifier('cascade/cascade.xml')
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faceDetected, rejectLevels, levelWeights = acne_cascade.detectMultiScale3(gray_img, 4, 3, outputRejectLevels = 1)
    margin = 1 # margin between detect and remove
    for i in range(len(faceDetected)):
        (x, y, w, h) = faceDetected[i] # face position
        if levelWeights[i] >= 1: # check confidence
            posi_x, posi_y, rad = x + (w//2), y + (h//2), w//2 # this position use for clear ance
            BGR = tuple(getAvgColor(img, (posi_x, posi_y), rad - margin, 8, i) for i in range(3)) # this line return BGR Color (0, 0, 0)
            cv2.circle(img, (posi_x, posi_y), rad - margin, BGR, -1) # use circle to replace avg color!
    # if you want to debug -> Ctrl + /
    if debug:
        for i in range(len(faceDetected)):
            (x, y, w, h) = faceDetected[i]
            color = (255, 0, 0) if levelWeights[i] >= 1 else (0, 0, 255)
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            cv2.putText(img, "%.5f" % levelWeights[i], (x, y-5), cv2.FONT_ITALIC, 0.5, color, 1)

