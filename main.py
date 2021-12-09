import cv2
import math

import numpy as np
from typing import Optional
from fastapi import FastAPI, File, UploadFile, Response, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
origins = ["*"]

app.mount("/static", StaticFiles(directory="docs/static"), name="static") # set path for static file
templates = Jinja2Templates(directory="docs") # choose directory to view webpage

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
) # allow all request

@app.get("/", response_class=HTMLResponse) # make route / to show webpage
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request}) # response index.html to client

@app.post("/acne") # this route is for clear acne
async def read_root(img: UploadFile = File(...), debug: Optional[bool] = False, conf: Optional[float] = 1, width: Optional[int] = 30):
    # this route receive key: img, debug, conf, width
    contents = await img.read() # read file from req
    if contents: # check is contents ready to process???
        nparr = np.fromstring(contents, np.uint8) # convert image to uint8
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR) # decode img uint8 format to numpy array
        img_byte = bytes(cv2.imencode('.png', clearAcne(img, debug, conf, width))[1]) # return clean face image then convert to bytes format
        return Response(content=img_byte, media_type="image/webp") # response image type webp to client
    else:
        raise HTTPException(status_code=400, detail="Please select images") # if no file in 'img' key will response error

def clearAcne(img, debug=False, conf=1, width=30):
    """checkposition"""
    acne_cascade = cv2.CascadeClassifier('cascade/5000cascade.xml') # get cascade file
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert img to gray color
    mask = np.zeros_like(img) # convert img to black color for mask!!!
    faceDetected, rejectLevels, levelWeights = acne_cascade.detectMultiScale3(gray_img, 4, 3, outputRejectLevels = 1) # call cascade to detect acne
    margin = 5 # margin between detect and remove
    for i in range(len(faceDetected)):
        (x, y, w, h) = faceDetected[i] # face position
        if levelWeights[i] >= conf and w <= width: # check confidence
            posi_x, posi_y, rad = x + (w//2), y + (h//2), w//2 # this position use for clear ance
            cv2.circle(mask, (posi_x, posi_y), w//2 - margin, (255, 255, 255), -1)
            # BGR = tuple(getAvgColor(img, (posi_x, posi_y), rad - margin, 8, i) for i in range(3)) # this line return BGR Color (0, 0, 0)
            # cv2.circle(img, (posi_x, posi_y), rad - margin, BGR, -1) # use circle to replace avg color!
    removed_acne = cv2.inpaint(img, cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY), 3, cv2.INPAINT_NS)
    # if you want to debug -> Ctrl + /
    if debug:
        for i in range(len(faceDetected)): # loop all detected position
            (x, y, w, h) = faceDetected[i]
            color = (255, 0, 0) if levelWeights[i] >= conf and w <= width else (0, 0, 255) # if low confidense color will change to red
            cv2.rectangle(removed_acne, (x, y), (x + w, y + h), color, 2) # create reatangle around detected area
            cv2.putText(removed_acne, "Cfd: %.5f" % levelWeights[i], (x, y-5), cv2.FONT_ITALIC, 0.3, color, 1) # show confidense text
            cv2.putText(removed_acne, "Wdt: %d" % w, (x, y + h + 10), cv2.FONT_ITALIC, 0.3, color, 1) # show size text
    return removed_acne

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

# img1 = cv2.imread('image/sample2.png')
# img2 = img1.copy()
# cv2.imshow('Before', img2)
# cv2.imshow('After', clearAcne(img1, True))
# cv2.waitKey(0)
# cv2.destroyAllWindows()