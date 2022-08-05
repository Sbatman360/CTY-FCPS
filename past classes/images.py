import Image
import ImageFilter
im = Image.open('zenitsu.png')

im = im.filter(ImageFilter.BLUR)
im.save("zenitsu2.png")