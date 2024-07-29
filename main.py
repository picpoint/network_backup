import shutil
import os

FOLDER_SRC = "src"
FOLDER_DST = "dst"

def copy_files(src_folder, dst_folder):
    shutil.copy2(f"{FOLDER_SRC}\\16.jpg", f"{FOLDER_DST}")
    list_files = os.listdir(src_folder)

    for i in list_files:
        print(i)



copy_files(FOLDER_SRC, FOLDER_DST)