Install
=======

Install Lirc:

	sudo apt-get install lirc

Symlink the config for the Velux remote into place (or alternatively copy the contents of it into your existing `lircd.conf` file):

	sudo mv /etc/lirc/lircd.conf /etc/lirc/lircd_original.conf
	sudo ln -s /home/pi/ir-remote/lirc/velux.conf /etc/lirc/lircd.conf

	sudo mv /etc/lirc/hardware.conf /etc/lirc/hardware_original.conf
	sudo ln -s /home/pi/ir-remote/lirc/hardware.conf /etc/lirc/hardware.conf

Ensure the Lirc module loads when the Raspberry Pi starts:

	sudo vim /boot/config.txt

	# Uncomment this to enable the lirc-rpi module
	#dtoverlay=lirc-rpi

	sudo reboot

When the Pi has rebooted, try a test command, and if all goes well there'll be no output and the
blind should go down:

	irsend SEND_ONCE velux KEY_DOWN --count=10

Install Flask for the web app:

	sudo pip install flask
	sudo pip install flask-cors


Run
===

	cd /home/pi/ir-remote
	python ./server.py

To make the server run persistently (e.g. after a reboot), Supervisor can be used:

	sudo apt-get install supervisor
	cd /etc/supervisor/conf.d
	sudo vim ir-remote.conf

Enter the following and save the file:

	[program:ir-remote]
	command=/usr/bin/python /home/pi/ir-remote/server.py
	directory=/home/pi/ir-remote
	redirect_stderr=true
	startsecs=5
	autorestart=true
	stdout_logfile=/var/log/ir-remote.stdout.log
	
Then update Supervisor:

	sudo service supervisor start
	sudo supervisorctl update
	sudo supervisorctl status


Use
===

Do a GET request on any of the following URLs:

* [Status page](http://raspberrypi.local:5000)
* [Put blinds up](http://raspberrypi.local:5000/up)
* [Put blinds down](http://raspberrypi.local:5000/down)
