from PIL import Image
import os
from glob import glob
from pathlib import Path
input("hello")
print("""
     Welcome to the image to pdf converter
     This tool converts each image in a folder into a separate pdf 
     """)
folder_path = str(input("Please provide the folder path: "))
file_ext = str(input("Please provide the file extension (eg. jpg, not .jpg: "))
full_path = folder_path + "\\*." + file_ext

for filename in glob(full_path):
     print(filename)
     file_stem = Path(filename).stem
     image = Image.open(filename)
     im = image.convert('RGB')
     im.save(file_stem + '.pdf')
