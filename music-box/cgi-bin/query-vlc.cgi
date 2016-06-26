#!/bin/bash

# Return a valid CGI response (which is ignored by Ajax call)
echo -e "Content-type: text/html\n\n"

# is VLC running?
if pidof vlc 2>&1 >/dev/null; then
    echo "true"
else
    echo "false"
fi
