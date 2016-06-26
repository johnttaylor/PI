#!/bin/bash

# Return a valid CGI response (which is ignored by Ajax call)
echo -e "Content-type: text/html\n\n"
echo "stopping vlc"

# stop/clean-up vlc
/home/pi/bin/stop-vlc
