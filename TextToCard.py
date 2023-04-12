from PIL import Image, ImageDraw, ImageFont
import textwrap, pandas as pd, os

x=10
WIDTH = 64
HEIGHT = 89
BOUND = 12.5
INDENT = 3

#=========================================================
# empties current directory
path = os.getcwd() + r'\temporaryImages'
for image in os.listdir(path):
  os.remove(path + rf'\{image}')

font = ImageFont.truetype("calibri.ttf", x*4)
df = pd.read_excel('allTexts.xlsx')
columns = list(df)
columns = columns[1:]  #otherwise it also goes through the index column

for i in columns:
    repeats = 0
    for j, text in enumerate(df[i]):
        if not pd.isna(text):
            if text[0] == ' ':
                raise error(f'text of {i}{j} starts with a space')
            repeat_times = 1
            fsection = text.split(' ')[0]
            if fsection[0] == 'x':
                repeat_times = int(fsection[1:])
                while text[0] != ' ':
                    text = text[1:]
                # in case I put in an extra space
                while text[0] == ' ':
                    text = text[1:]

            for n in range(repeat_times):
                if n > 0:
                    repeats+=1

                img = Image.open(fr'CardTemplates\{i}.png')
                img = img.resize((x*WIDTH, x*HEIGHT))
                d = ImageDraw.Draw(img)

                wrapped = textwrap.fill(text, width=31)
                d.text((x*INDENT, x*(BOUND+INDENT)), wrapped, font=font, fill="black")
                img.save(f"temporaryImages\{i}{j+repeats}.png")

import PrepareForPrint
proceed = input('Print? Y/n: ')
if proceed == 'Y':
    import Print
    print('\nsent to printer')
else:
    print('\naborted')
