#!/bin/python3
import os
import sys
import argparse
parser=argparse.ArgumentParser(prog="file_organizer")
parser.add_argument("plce",help="what directories you want to organize", type = str)
parser.add_argument("--dry-run", action="store_true", help="to know where the file will go")
parser.add_argument("--path",help="if you want a specific directories that's outside home dir", type= str)
args = parser.parse_args()
path = os.path.expanduser("~")
# cwd= os.getcwd() <-- this will be used if i do make it inro argparse tool
# place = input("what dir you wanna organize:") #no need for parent dir
standard_path = os.path.join(path,args.plce)
if __name__ == "__main__":
    try:
        files=(os.listdir(standard_path))
    except FileNotFoundError:
        print(f"{args.plce} does not exist")
        sys.exit()
    os.chdir(standard_path)
    data = {".png":"pictures", ".jpg":"pictures", ".jpeg": "pictures", ".docx":"documents", ".pptx":"documents", ".txt" : "documents"}
    if args.dry_run:
        for k, v in data.items():
            for i in os.listdir(os.path.join(standard_path,v)):
                print(f"{i} will go to {v}")
    elif args.path: #um pretty sure this is  kinda dog shit? how can i able to give option to custom your own path or just ahve the standard?? pls help
        standard_path = args.path
        for file in files:
            filet = file.lower()
            for k, v in data.items():
                if filet.endswith(k):
                    src= os.path.join(standard_path,file)
                    try:
                        Duplicate = False
                        counter = 1
                        for i in os.listdir(os.path.join(standard_path,v,)):
                            if file == i:
                                os.rename(src,os.path.join(standard_path,v, f"{file}-{counter}"))
                                counter +=1
                                Duplicate = True
                                break
                            else:
                                pass
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
    elif not args.dry_run and not args.path:
        for file in files:
            filet = file.lower()
            for k, v in data.items():
                if filet.endswith(k):
                    src= os.path.join(standard_path,file)
                    try:
                        Duplicate = False
                        counter = 1
                        for i in os.listdir(os.path.join(standard_path,v,)):
                            if file == i:
                                os.rename(src,os.path.join(standard_path,v, f"{file}-{counter}"))
                                counter +=1
                                Duplicate = True
                                break
                            else:
                                pass
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