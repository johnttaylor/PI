#!/bin/bash

# Return a valid CGI response (which is ignored by Ajax call)
echo -e "Content-type: text/html\n\n"
echo "starting vlc"


# Start VLC in the background
sudo su pi -c "/home/pi/bin/start-vlc >/dev/null 2>&1 &"
