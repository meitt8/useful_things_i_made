from glob import glob
from pathlib import Path
import re

folder_path = "foler path name" # define a path
full_path = folder_path + "\\*.extension" # where extension is eg. txt, pdf, csv

for filename in glob(full_path):
     file_stem = Path(filename).stem # get stem of file (name)
     print(file_stem)
     split_name = re.split("[_()]",file_stem) # split file names by chosen delimiters
     print(split_name)
     print("-"*13)
