from PIL import Image
import sys
import os
ROOTFOLDER = './'
count = 1

for root, dirs, files in os.walk(ROOTFOLDER):
      print(len(files))
      for file in files:
            string = str(count)
            filename = ROOTFOLDER + string + '.png'
            print(filename)
            basewidth = 300
            img = Image.open(filename)
            wpercent = (basewidth/float(img.size[0]))
            hsize = int((float(img.size[1])*float(wpercent)))
            img = img.resize((basewidth,hsize), Image.ANTIALIAS)
            img.save(filename)
            count += 1