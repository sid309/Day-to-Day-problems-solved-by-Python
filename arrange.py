import os
import shutil

target="datasets"
os.chdir(target)
print(os.getcwd())
file_names=os.listdir('.')
for file_ in file_names:
    dir_names=file_.split(".")[-1]
    os.makedirs(dir_names,exist_ok=True)
    src=file_
    dest=os.path.join(dir_names,file_)
    shutil.move(src,dest)