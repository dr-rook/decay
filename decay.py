#!/usr/bin/env python3
# the line above using the python3 interpreter

import sys
import os
import time # using this to make it easier to understand

def show_help():
    print("""
commands:
    decay create [file] {flag}
    decay delete [file]

flags (optional):
    --for [seconds]
""")

def check_if_file_exists(file):
    return os.path.exists(file)

def create_file(file):
    exists = check_if_file_exists(file)
    if exists:
        print("\nfile already exists\n")
    else:
        open(file, "x").close()
        print(f"\n{file} has been created\n")

def create_file_with_timer(duration, file):
    create_file(file)
    while duration > 0:
        print(f"\rdeleting file in: {duration:03} second(s)", end="") # this just updates the text instead of going down. \r is to keep the text in 1 line (overwriting), and end="" is to keep it in the same place (not go down)
        duration -= 1
        time.sleep(1) # sleep for 1 second
    print("\n")
    delete_file(file)

def delete_file(file):
    os.remove(file)
    print(f"\n{file} has been deleted\n")

if len(sys.argv) == 1: # if only 'decay' is typed
    print("\n- 'decay help' to show a list of commands")

# commands
elif sys.argv[1] == "create":
    try:
        if len(sys.argv) < 3: # for example: 'decay create' is invalid
            show_help()
            sys.exit() # it just quits the program

        elif len(sys.argv) == 3: # for example: 'decay create foo.txt'
            create_file(sys.argv[2]) # sys.argv[2] is the file 'foo.txt'

        elif len(sys.argv) >= 4: # for example: 'decay create foo.txt something'
            if sys.argv[3] == "--for":
                if len(sys.argv) == 5: # for example: 'decay create foo.txt --for 5'
                    try:
                        duration = int(sys.argv[4]) # convert string to integer (number)
                        create_file_with_timer(duration, sys.argv[2])

                    except ValueError: # if its '5s' and not '5'
                        print("\nfor the time (in seconds), type the number only")
                else: show_help()

            else: print(f"\n'{sys.argv[3]}' is not a flag\n'decay help' for more info")

        else: show_help()
    except FileNotFoundError: print("\n\ndirectory not found (folder does not exist)")

elif sys.argv[1] == "delete":
    try:
        if len(sys.argv) >= 3:
            delete_file(sys.argv[2])
        else:
            show_help()
            sys.exit()
    except FileNotFoundError: print("\n\nfile not found error. check if the file and folder exists")

elif sys.argv[1] == "help":
    show_help()


else: print("\n- 'decay help' to show a list of commands")
