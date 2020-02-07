import math
import matplotlib.pyplot as plt
from matplotlib.image import imread
from cs1media import *

purple = (128, 0, 128)
yellow = (255, 255, 0)

img = create_picture(100, 100, purple)
img.show()
img.set_pixels(yellow)
img.show()





def paste(canvas, img, x1, y1):
    w, h = img.size()
    for y in range(h):
        for x in range(w):
            canvas.set(x1 + x, y1 + y, img.get(x, y))


def dist(c1, c2):
    r1, g1, b1 = c1
    r2, g2, b2 = c2
    return math.sqrt((r1-r2)**2 + (g1-g2)**2 + (b1-b2)**2)


def chroma(img, key, threshold):
    w, h = img.size()
    for y in range(h):
        for x in range(w):
            p = img.get(x, y)
            if dixt(p, key) < threshold:
                img.set(x, y, color.yellow)

def chroma_paste(canvas, img, x1, y1, key):
    w, h = img.size()
    for y in range(h):
        for x in range(w):
            p = img.get(x, y)
            if p != key:
                canvas.set(x1+x, y1+y, p)

def hide_picture(canvas, img, bwimg):
    w, h = img.size()
    for y in range(h):
        for x in range(w):
            if r / 2 != 0:
                r -= 1

black = (0, 0, 0)




white = (255, 255, 255)
black = (0, 0, 0)

def restore_picture(canvas, img):
    w, h = img.size()
    for y in range(h):
        for x in range(w):
            r, g, b = img.get(x, y)
            if r % 2 == 1:
                canvas.set(x, y, black)
            else:
                canvas.set(x, y, white)
