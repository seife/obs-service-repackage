# MAKEFILE for easy "make install" :-)
#
#

install:
	install -p -m 0755 -D repackage         $(DESTDIR)/usr/lib/obs/service/repackage
	install -p -m 0644 -D repackage.service $(DESTDIR)/usr/lib/obs/service/repackage.service

