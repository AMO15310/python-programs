import PIL 
from PIL import Image
image1 = Image.open(r"/put the image path here/")
r,g,b = image1.split()
image1 = Image.merge("RGB",(b,g,r))
image1.show()

