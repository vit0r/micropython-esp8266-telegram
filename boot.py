# This file is executed on every boot (including wake-boot from deepsleep)
import gc

import esp
import machine
import uos
from device_mod import do_connect

esp.osdebug(None)
# uos.dupterm(None, 1) # disable REPL on UART(0)
# import webrepl
# webrepl.start()
do_connect()
gc.collect()
