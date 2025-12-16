#!/bin/bash

day=${1?Missing day modifier.}

mkdir "day_$day"
cp template.py "day_$day/main.py"
touch "day_$day/test.txt" "day_$day/input.txt"
echo "Succesfully created the folder for day_$day"
cd "day_$day"
