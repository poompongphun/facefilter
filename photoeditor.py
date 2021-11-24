"""edit photo"""

from PIL import Image, ImageEnhance
import os

def formatindustry(path, lastnamefile):
    """factory"""
    for item in os.listdir('%s' %path):
        if item.endswith('.jpg'):
            img1 = Image.open('edit/input/%s' %item)
            img1.save('%s.%s' %(item, lastnamefile))

# formatindustry('edit/input/')

def sharpness(imagepath, sharpn):
    """sharpness function"""
    img1 = Image.open(imagepath)
    enhancer = ImageEnhance.Sharpness(img1)
    enhancer.enhance(sharpn).save('edit/output/2.jpg')

# sharpness('edit/input/acne1.jpg', 3)
    # Sharpn
    # 0 : blurry
    # 1 : original image
    # 2 : increased sharpness
    # 3 : increased more sharpness