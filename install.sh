#!/bin/sh
# so this shebang in line 1 basically tells the computer to run as shell whenever this file is ran, the shell interpreter

mkdir -p "$HOME/.local/bin/" # create /bin if it doesnt exist. -p flag basically means to create directory if neccesary, and dont complain if it already exists
cp "$(dirname "$0")/decay.py" "$HOME/.local/bin/decay" # copy the file to the command
chmod +x "$HOME/.local/bin/decay" # changes file permissioms to be able to execute (+x)

echo done

# $(dirname "$0") is the current directory of the file (install.sh)
# $HOME is the home directory of the system
