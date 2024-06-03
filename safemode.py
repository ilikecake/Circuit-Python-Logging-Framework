'''safemode.py

Catches errors that put Circuit Python into safe mode. These errors are probably bugs in Circuit
Python and are probably not affected by user code. In my experience, these just happen sometimes.
Documentation seems to imply that using wifi can sometimes cause an error to be thrown. In here, we
try to log these events to the error log file and potentially reboot the device to try to recover.
This might not always work if the flash memory is read only to Circuit Python or if there is some
hardware error with the flash memory.

'''
import microcontroller
import storage
import time
import adafruit_logging as logging
import supervisor
import os
import traceback

try:
    storage.remount("/", readonly=False)
    logger = logging.getLogger(os.getenv("LOG_NAME"))
    logger.addHandler(logging.RotatingFileHandler(os.getenv("LOG_FILENAME"), 'a', os.getenv("LOG_FILE_MAX_SIZE"), os.getenv("LOG_FILES_TO_KEEP")))
    logger.setLevel(logging.ERROR)
    logger.critical(f"Controller entered safemode: {supervisor.runtime.safe_mode_reason}")

    if os.getenv("LOG_AUTO_RESTART") is "True":
        time.sleep(20)
        microcontroller.reset()
        
except Exception as e:
    #If there is some issue writing the safemode reason to the log file, try to write *that* error to the log file.
    #This was useful for debugging, but probably won't do anything in real code.
    logger.error(traceback.format_exception(e))
