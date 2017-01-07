Install
=======

Install Lirc:

	sudo apt-get install lirc

Symlink the config for the Velux remote into place (or alternatively copy the contents of it into
your existing `lircd.conf` file:

	ln -s /path/to/energenie-ir/devices/velux.conf /etc/lirc/lircd.conf


Run
===

	cd /path/to/energenie-ir
	python ./server.py


Use
===

Do a GET request on any of the following URLs:

* [Status page](http://raspberrypi.local:5000)
* [Put blinds up](http://raspberrypi.local:5000/up)
* [Put blinds down](http://raspberrypi.local:5000/down)
