#!/bin/sh

mjpg_streamer -i "input_uvc.so -d /dev/video0 -r 640x480 -f 10" -o "output_http.so -p 9090 -w ./www"
