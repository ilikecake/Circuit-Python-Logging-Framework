'''safemode.py

Catches errors that put Circuit Python into safe mode. These errors are probably bugs in Circuit
Python and are probably not affected by user code. In my experience, these just happen sometimes.
Documentation seems to imply that using wifi can sometimes cause an error to be thrown. In here, we
try to log these events to the error log file and potentially reboot the device to try to recover.
This might not always work if the flash memory is read only to Circuit Python or if there is some
hardware error with the flash memory.

'''
import microcontroller
import supervisor
import storage
import time
import adafruit_logging as logging

fs_obj = storage.getmount("/")
if fs_obj.readonly is False:
    #the file system is writable by CircuitPython.
    logger = logging.getLogger('error_log')
    logger.addHandler(logging.RotatingFileHandler('log.txt', 'a', 1000, 3))     #TODO: Control these in settings.toml. also make auto-reboot an option in there
    logger.setLevel(logging.ERROR)

    logger.critical(supervisor.runtime.safe_mode_reason)
    
    time.sleep(20)
    microcontroller.reset()