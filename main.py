from PIL import Image, ImageFont, ImageDraw, ImageOps
import os

font_size = 64
font = ImageFont.truetype("simkai.ttf", font_size)

start = 0x4e00
end = 0x62ff
total = end - start

if(not os.path.isdir("output")):
    os.mkdir("output")

for i in range(start, end + 1):
    c = chr(i)
    print("Generating " + c)
    im = Image.Image()._new(font.getmask(c))
    #im = im.resize((font_size, font_size), Image.ANTIALIAS)
    im = ImageOps.invert(im)
    im.save("output/" + c + ".png")
    
