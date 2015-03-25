# webradio
Yet another web radio based on TP-Link TL-MR3020 

This webradio is based on the TP-Link TL-MR3020 running OpenWrt (with extroot). Of course it can be also implemented on other routers running Openwrt, provided that they have at least one USB port.

Highlights:
- remote control with web interface
- once configured, all actions are performed from the web interface (you don't have to ssh into the router for any action)
- hardware button can be used for changing radio channels, mute audio or reset the box (short press, long press, very long press)

Hardware requirements:
- TP-Link TL-MR3020
- USB hub
- USB memory stick
- USB sound card

Software requirements:
- Openwrt (with extroot)
- gstreamer, gstreamer-utils and plugins
- packages needed for the USB sound card (see http://wiki.openwrt.org/doc/howto/usb.audio)

Enjoy :)