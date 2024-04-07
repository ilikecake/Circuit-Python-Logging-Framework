# Circuit Python Logging Framework

This is a set of files that are meant to help log occational errors in user code. It is intended to be used after the code is mostly running to catch occasional errors that occur that can't be caught in initial development. It will catch errors that crash the user code and save them to the Circuit Python USB drive. This should let you go back and review the errors later to determine why your device stopped working. For this to work, you cannot have the device connected to a computer. 

Note that errors in the user code will still crash the device and require a reboot to fix. This only logs the error so that we can see what it was later.

This has been tested on the ESP32-S3 Feather Running Circuit Python 9.0.3

## This code does two things:

1. It will check if the file system is read only, and if USB is connected. We assume that if USB is connected, that we want the file system set to read only (read only to Circut Python, meaning writeable over USB). We also assume that USB is not connected, say because the device is connected to a 5V wall wart or something, that we want to enable read/write file system so that we can use the wifi workflow and write to the flash memory of the device. It is not possible to change the read-only-ness of the file system from user code, so we do a check at the start of user code in the code.py file. If we need to update the file system, we set a flag in non-volatile memory and hard reset the device. boot.py reads this flag and sets the file system accordingly.
   
2. Enables logging to catch errors that crash the user code. I have had a few projects that seem to work fine, but will occasionally die and require a power cycle to fix. This is intended to catch occasional errors and write them to a file for later inspection. We can only write to the log file if the file system is not read-only, hence the implementation of #1 above.

## To use this code:
1. If you already have code in the code.py file, rename it to main.py. From now on, all user code should go into main.py.
2. Copy the boot.py and code.py files to the root of your Circuit Python drive. 
3. Make sure you have set up your [settings.toml](https://learn.adafruit.com/scrolling-countdown-timer/create-your-settings-toml-file) file if you want wifi access to the device. 

## Notes:
 * supervisor.runtime.usb_connected is true when we are connected over USB
 * storage.getmount("/").readonly is true when the file system is read only to circuit python
 * Set microcontroller.nvm[0:1] flag:
    * 0xAA to tell the device to make the file system read only (Allow writes over USB)
    * 0x55 to tell the device to make the file system read/write. (This disables writing over USB)
