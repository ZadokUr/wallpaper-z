import os

def renameFiles(directory):
    directoryList = os.listdir(directory)
    for count, filename in enumerate(directoryList):
        src = directory + filename
        dest = directory + str(count)+".jpg"
        #rename all files [number].jpg
        os.rename(src, dest)


try:
    renameFiles('./wallpapers/')
    print("Files renamed successfully")
except:
    print("An error occured when renaming the files")