from PIL import Image

image = Image.open('image.jpg')
image.show()

image.format
image.mode
image.size
image.info

image.resize((200,800))
img2 = image.crop((0,0,300,300))
img2.save("crop.jpg")

image.transpose(Image.FLIP_LEFT_RIGHT)
image.transpose(Image.FLIP_TOP_BOTTOM)
image.transpose(Image.ROTATE_90)

image.thumbnail((90,90))


image = Image.open('maca.jpg')
r, g, b = image.split()

Image.merge("RGB", (b, g, r))

image = Image.open('maca.jpg')
image2 = Image.open('image.jpg')

image.paste(image2)
image.paste(image2, (400,300))