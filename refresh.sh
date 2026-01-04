/usr/bin/sudo pkill -F /home/pi/offpid.pid
/usr/bin/sudo pkill -F /home/pi/metarpid.pid
/usr/bin/sudo /usr/bin/python3 /home/pi/METARMap-Texas/metar.py & echo $! > /home/pi/metarpid.pid
exit 0
