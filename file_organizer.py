#!/bin/python3
import os
import sys
import argparse
parser=argparse.ArgumentParser(prog="file_organizer")
parser.add_argument("--dry-run", action="store_true", help="to know where the file will go")
parser.add_argument("--path",default=".",help="if you want a specific directories that's outside home dir", type= str)
args = parser.parse_args()
path = os.path.expanduser(args.path)
# cwd= os.getcwd() <-- this will be used if i do make it inro argparse tool
# place = input("what dir you wanna organize:") #no need for parent dir
standard_path = os.path.join(path)
if __name__ == "__main__":
    try:
        files=(os.listdir(standard_path))
    except FileNotFoundError:
        print(f"{args.path} does not exist")
        sys.exit()
    os.chdir(standard_path)
    data = {".png":"pictures", ".jpg":"pictures", ".jpeg": "pictures", ".docx":"documents", ".pptx":"documents", ".txt" : "documents"}
    for file in files:
        filet = file.lower()
        for k, v in data.items():
            if filet.endswith(k):
                src= os.path.join(standard_path,file)
                dest = os.path.join(standard_path, v, file)
                if args.dry_run:
                    print(f"{file} will go to {dest}" )
                    break
                try:
                    Duplicate = False
                    counter = 1
                    for i in os.listdir(os.path.join(standard_path,v)):
                        if file == i:
                            os.rename(src,os.path.join(standard_path,v, f"{file}-{counter}"))
                            counter +=1
                            Duplicate = True
                            break
                    if not Duplicate:
                        os.rename(src,os.path.join(standard_path,v,file))
                except FileNotFoundError:
                    confirm = input(f"directories for {v} does not exist yet \n would you want to create a new directories?(y/n):")
                    if confirm == "y":
                        os.mkdir(v)
                        os.rename(src,os.path.join(standard_path,v,file))
                        print("directories have been made")
                    else:
                        continue
    print("The Process Is completed")