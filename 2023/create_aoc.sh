#!/bin/bash

day=${1?Missing day modifier.}

mkdir "Day $day"
cp template.py "Day $day/main.py"
touch "Day $day/test.txt" "Day $day/input.txt"
echo "Succesfully created the folder for Day $day"
cd "Day $day"
$SHELL
