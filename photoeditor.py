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
    enhancer.enhance(sharpn).save('edit/output/sharpnesssample/10.jpg')

# sharpness('edit/input/acne1.jpg', 10)
    # Sharpn
    # 0 : blurry
    # 1 : original image
    # 2 : increased sharpness
    # 3-n : increased more sharpness

def brightness(imagepath, brightn=1):
    """brightness function"""
    img1 = Image.open(imagepath)
    enhancer = ImageEnhance.Brightness(img1)
    enhancer.enhance(brightn).save('edit/output/brightnesssample/2.jpg')

#brightness('edit/input/acne1.jpg')

# brightness
    # brightn
    # >= 1 : increased brightness

def contrast(imagepath, contrastn=1.5):
    """contrast function"""
    img1 = Image.open(imagepath)
    enhancer = ImageEnhance.Contrast(img1)
    enhancer.enhance(contrastn).save('edit/output/contrastsample/1.jpg')

# contrast('edit/input/acne1.jpg')