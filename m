#!/bin/bash
# Credits : https://stackoverflow.com/questions/3466166/how-to-check-if-running-in-cygwin-mac-or-linux/17072017#17072017

if [ "$(uname)" == "Darwin" ]; then
# Mac OS X platform
cd web && python manage.py "$@" && cd ../

elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
# Linux platform
cd web && python manage.py "$@" && cd ../

elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW32_NT" ]; then
# Windows NT platform
command="$@" 
cmd "/C cd web & manage.py $command & cd ..\
"
fi
