import os
import shutil
import sys

if len(sys.argv) != 2:
    print("Wrong numbers of arguments")
    sys.exit(1)

path = sys.argv[1]

dir_list = os.listdir(path=path)

for i in dir_list:
    name, ext = os.path.splitext(i)
    file = os.path.join(path, i)
    if os.path.isfile(file):
        if not ext:
            dest_no = os.path.join(path, "no_extension")
            os.makedirs(dest_no, exist_ok=True)
            shutil.move(file, dest_no)
        else:
            dest = os.path.join(path, ext)
            os.makedirs(dest, exist_ok=True)
            shutil.move(file, dest)
    else:
        pass