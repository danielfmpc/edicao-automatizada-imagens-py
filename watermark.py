from PIL import Image
import os

image_path = "watgermark_images"
watermark = Image.open("watermark.png")
with_w, height_w = watermark.size

if image_path not in os.listdir():
  os.mkdir(image_path)


files_path = 'fotos'
files = [i for i in os.listdir(files_path) if i.endswith('.jpg')]


for file in files:
  file_path = os.path.join(files_path, file)
  new_path = os.path.join(image_path, file)

  image = Image.open(file_path)
  w, h = image.size

  base_w = int(0.2 * w)
  w_percent = base_w / float(with_w)
  h_size = int((height_w * w_percent))

  watermark = watermark.resize((base_w, h_size))
  image.paste(watermark, (w - base_w, h - h_size), watermark)
  image.save(new_path, 'JPEG')