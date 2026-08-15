#!/usr/bin/env python3
# the line above using the python3 interpreter

import sys
import os

def show_help():
    print("""
commands:
- decay create [file]
- decay delete [file]

flags:
""")

def check_if_file_exists(file):
    return os.path.exists(file)

def create_file(file):
    exists = check_if_file_exists(file)
    if exists:
        print("file already exists")
    else: open(file, "x").close()

def delete_file(file):
    os.remove(file)

if len(sys.argv) == 1:
    print("\n- 'decay help' to show a list of commands")

elif sys.argv[1] == "create":
    try:
        if len(sys.argv) >= 3:
            create_file(sys.argv[2])
        else:
            show_help()
    except FileNotFoundError: print("directory not found (folder does not exist)")

elif sys.argv[1] == "delete":
    try:
        if len(sys.argv) >= 3:
            delete_file(sys.argv[2])
        else:
            show_help()
    except FileNotFoundError: print("directory not found (folder does not exist)")

elif sys.argv[1] == "help":
    show_help()

else: print("\n- 'decay help' to show a list of commands")
