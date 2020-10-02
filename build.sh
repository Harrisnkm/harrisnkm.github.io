#!/bin/bash

for FILE in content/*; do
    filebase=$(basename $FILE)
    if [ $filebase = "index.html" ]
    then
        cat templates/top.html content/$filebase templates/bottom_script.html > docs/$filebase
    else
        cat templates/top.html content/$filebase templates/bottom.html > docs/$filebase
    fi
done