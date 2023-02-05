#!/bin/sh
cd ~/python/paraview/images/aview_/
files=$(ls *.png*)
for f in $files;do
    echo file "$f"
    echo duration 0.2
done
