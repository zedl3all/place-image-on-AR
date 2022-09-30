from PIL import Image, ImageDraw, ImageFilter

imgmain = Image.open("test.jpg")
imgplace = Image.open("LOGO/1.jpg")
backimg =imgmain.copy()
backimg.paste(imgplace,(x_centerPixel,y_centerPixel),quality=95)
backimg.save("img_save/testplace.jpg",quality=95)