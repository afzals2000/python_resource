import os
import shutil


def write_to_file(file_2_write, content):
    text_file = open(file_2_write, "w")
    text_file.write(content)
    text_file.close()

def delete_file(path):
    os.remove(path)


def drop_folder(folder):
    shutil.rmtree(folder)

