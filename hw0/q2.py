import numpy as np 
import sys
from PIL import Image

im = Image.open(sys.argv[1])
width, height = im.size
angle = 180
data = im.rotate(angle)
out = Image.new("RGB", (width, height), "white")
out.paste(data)	
out.save("ans2.png")

