from PIL import Image
import math

img = Image.open('world.png')
width, height = img.size
img2 = Image.new('RGB', (width , height))

col=[(40,78,178),(124,235,68),(194,237,117),(229,185,95),(172,126,44),(81,61,34)]

def nearColor(c):
    r,g,b,a=c
    best=1000000
    bi=-1
    for i in range(len(col)):
        r1,g1,b1=col[i]
        sc=math.sqrt((r1-r)**2+(g1-g)**2+(b1-b)**2)
        if best>sc:
            best=sc
            bi=i
    return col[bi]	

for y in range(height):
  for x in range(width):
    r,g,b = nearColor(img.getpixel((x,y)))
    img2.putpixel((x,y), (int(r), int(g), int(b)))

img2.show()
img2.save('worldout.png')
