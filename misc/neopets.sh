#!/bin/sh
# > tfw neopets will die during your lifetime
USERNAME=""
PASSWORD=""
# nice plaintext you got there
curl -c nc.txt -d "username=$USERNAME&password=$PASSWORD" http://www.neopets.com/login.phtml
curl -b nc.txt -d "type=get_omelette" http://www.neopets.com/prehistoric/omelette.phtml
curl -b nc.txt -d "type=get_jelly" http://www.neopets.com/jelly/jelly.phtml
curl -b nc.txt -d "go_fish=1" http://www.neopets.com/water/fishing.phtml
