command="$@" 
cmd "/C cd web & manage.py $command & cd ..\
"