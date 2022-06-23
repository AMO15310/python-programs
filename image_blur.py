import PIL 
from PIL import Image,ImageFilter
#Original_Image = Image.open(r"put the path of the image here then uncomment line")
blur_image = Original_Image.filter(ImageFilter.BLUR)
blur_image.show()
#Original_Image.show()
