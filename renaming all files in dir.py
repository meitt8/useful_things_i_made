# Python 3 code to rename multiple
# files in a directory or folder

# importing os module
import os


# Function to rename multiple files

folder = "dbr data/Bragg 0 degrees take 3"
for count, filename in enumerate(os.listdir(folder)):
    dst = os.path.splitext(filename)[0] + "_0.txt" # takes filename stem, adds a string and new extension
    src = f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
    dst = f"{folder}/{dst}"

    # rename() function will
    # rename all the files
    os.rename(src, dst)
