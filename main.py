import os
from PIL import Image, ImageFont, ImageDraw, ImageOps

font_size = 64

start = 0x4e00
end = 0x62ff
total = end - start

if(not os.path.isdir("output")):
    os.mkdir("output")

fonts = ["simkai.ttf", "simhei.ttf", "simfang.ttf"]

for f in fonts:
    font = ImageFont.truetype(f, font_size)
    for i in range(start, end + 1):
        c = chr(i)
        print("Generating " + f.split(".")[0] + "_" + c)
        im = Image.Image()._new(font.getmask(c))
        #im = im.resize((font_size, font_size), Image.ANTIALIAS)
        im = ImageOps.invert(im)
        im.save("output/" + f.split(".")[0] + "_" + c + ".png")
   
