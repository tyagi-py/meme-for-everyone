import numpy as np
from PIL import ImageFont, ImageDraw, Image
import cv2

def draw_text(img, stx,sty, text):
    ## Make canvas and set the color
    
    b,g,r,a = 0,255,0,0


    ## Use simsum.ttc to write Chinese.
    fontpath = "mangal.ttf" # <== 这里是宋体路径 
    font = ImageFont.truetype(fontpath, 32)
    img_pil = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pil)
    draw.text((stx, sty),  text, font = font, fill = (b, g, r, a))
    img = np.array(img_pil)

    return img