import os
from PIL import Image

path = os.getcwd() + r'\listsToPrint'
printer_name = "EPSON5940C9 (XP-4200 Series)"

for _list in os.listdir(path):
    os.startfile(path+fr'\{_list}', "print")
