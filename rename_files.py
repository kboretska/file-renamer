import os
import glob
import sys

directory = sys.argv[1]
file_type = sys.argv[2]
slice_index = int(sys.argv[3])

os.chdir(directory)

for file in glob.glob(f"*.{file_type}"):
    file_name, extension = os.path.splitext(file)
    new_file_name = file_name[:-slice_index] + extension
    try:
        os.rename(file, new_file_name)
    except OSError as e:
        print(e)
    else:
        print(f"Renamed {file} to {new_file_name}")
