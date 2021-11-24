from PIL import Image
import os

def formatindustry(img1, lastnamefile):
    """factory"""
    for item in os.listdir('edit/input'):
        if item.endswith('.jpg'):
            img1 = Image.open('edit/input/%s' %item)
            # filename, extension = os.path.splitext(item)
            img1.save('%s.%s' %(item, lastnamefile))

formatindustry('edit/input/')