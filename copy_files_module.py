import shutil
import os
'''
Функция копирования файлов
'''
def copy_files(src_folder, dst_folder):
    list_files = os.listdir(src_folder)
    for i in list_files:
        shutil.copy2(f"{src_folder}\\{i}", f"{dst_folder}")
