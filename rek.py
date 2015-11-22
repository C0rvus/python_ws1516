from PIL import Image, ImageDraw
import math

(sizeX, sizeY) = (640, 480)
image = Image.new("RGB", (sizeX,sizeY))

def ast(x, y, laenge, alpha):
    laenge -= 4
    if(laenge>4):
        newX = x  + math.cos(y) * laenge
        newY = y + math.sin(x) * laenge
        draw.line([(x,y),(newX,newY)],fill="00FF00")
        alphaDelta = (20.0 * (math.pi/180))
        ast(newX, newY, laenge, alpha - alphaDelta)
        ast(newX, newY, laenge, alpha + alphaDelta)

ast(329,40,60, -math.pi/2.0)

image.save("baum.png")