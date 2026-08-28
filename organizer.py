import os
import shutil
import sys
import json

if len(sys.argv) != 2:
    print("Wrong numbers of arguments")
    sys.exit(1)

path = sys.argv[1]

dir_list = os.listdir(path=path)

raport = {
    "folder": path,
    "moved_files": {},
    "total": 0
}

for i in dir_list:
    name, ext = os.path.splitext(i)
    file = os.path.join(path, i)
    if os.path.isfile(file):
        if not ext:
            dest_no = os.path.join(path, "no_extension")
            os.makedirs(dest_no, exist_ok=True)
            shutil.move(file, dest_no)
            category = "no_extension"
        else:
            dest = os.path.join(path, ext)
            os.makedirs(dest, exist_ok=True)
            shutil.move(file, dest)
            category = ext

        raport["moved_files"][category] = raport["moved_files"].get(category, 0) + 1
        raport["total"] += 1

with open("raport.json", "w") as raport_file:
    json.dump(raport, raport_file, indent=2)
