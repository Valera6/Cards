from PIL import Image
import os

path = os.getcwd() + r'\CardTemplates'
for name in os.listdir(path):
    img_path = path + fr'\{name}'
    im = Image.open(img_path)
    im = im.convert('RGBA')
    width, height = im.size
    im = im.crop((22, 51, 856, 1210))
    im.save(img_path)
