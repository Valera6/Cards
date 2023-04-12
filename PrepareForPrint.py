import sys, os
from PIL import Image

# empties current directory
path = os.getcwd() + r'\listsToPrint'
for image in os.listdir(path):
  os.remove(path + rf'\{image}')

path = os.getcwd() + r'\temporaryImages'
images = [Image.open(path+fr'\{x}') for x in os.listdir(path)]
width, height = images[0].size

total_width = 3*width
total_height = round(3.1*height)

output = Image.new('RGB', (total_width, total_height), 'white')

x_offset = 0
y_offset = round(0.06*height)
_id = 1
for i, im in enumerate(images):
  output.paste(im, (x_offset,y_offset))
  x_offset += im.size[0]
  
  if _id==3 or _id==6:
    y_offset += im.size[1]
    x_offset = 0
  if _id == 9:
    x_offset = 0
    y_offset = round(0.06*height)
    _id = 0
    output.save(fr'listsToPrint\from{i-7}to{i+1}.png')
    output = Image.new('RGB', (total_width, total_height), 'white')
  if i == len(images)-1:
    output.save(fr'listsToPrint\from{i-(_id-2)}to{i+1}.png')
    
  _id+=1
