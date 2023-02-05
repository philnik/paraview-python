#!/bin/sh
cd ~/python/paraview/images/
ffmpeg -framerate 30 -pattern_type glob -i 'aview_*.png' -pix_fmt yuv420p aview_.mp4
