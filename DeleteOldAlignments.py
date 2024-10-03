import os
from os import listdir
from os.path import isfile, join

directory_to_search = "C:\\ProgramData\\Hexagon\\PC-DMIS\\2020 R2\\Alignments\\"
files = [f for f in listdir(directory_to_search) if isfile(join(directory_to_search, f))]

for file in files:
    if not file.upper().startswith("SAFE_"):
        file_path = join(directory_to_search, file)
        os.remove(file_path)
