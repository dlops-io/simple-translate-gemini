#!/bin/bash

echo "Container is running!!!"

args="$@"
echo $args

if [[ -z ${args} ]]; 
then
    pipenv shell python cli.py
    #pipenv run python cli.py --text "Ready to go home?"
else
  pipenv run python $args
fi