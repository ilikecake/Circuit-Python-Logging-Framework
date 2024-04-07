import time
import storage
import microcontroller

if microcontroller.nvm[0] != 0xAA:
    print("Setting storage to read/write. This will disable USB writes")
    storage.remount("/", readonly=False)    #This means that circuit python can read/write to the FS.
    if microcontroller.nvm[0] != 0x55:
        #If the nvm is not set to either 0xAA or 0x55, set it here. TODO: Do I need to do this?
        microcontroller.nvm[0:1] = b"\x55"
else:
    print("Setting storage to read-only. This will allow USB writes")
