#!/bin/bash

if [ "$(uname)" == "Darwin" ]; then
    # Do something under Mac OS X platform
echo 'TODO: mac helper'

elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
# Do something under Linux platform
cd web && python manage.py "$@" && cd ../

elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW32_NT" ]; then
# Do something under Windows NT platform
command="$@" 
cmd "/C cd web & manage.py $command & cd ..\
"
fi
