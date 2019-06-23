from machine import Pin, unique_id
from time import sleep


pin = Pin(5, Pin.OUT)

def __try_connect(sta_if):
  while not sta_if.isconnected():
    pin.on()
    sleep(0.5)
    pin.off()
    sleep(0.5)

def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        wcred = __read_credentials()
        sta_if.connect(wcred.get('essid'),wcred.get('password'))
        __try_connect(sta_if)
    print('network config:', sta_if.ifconfig())

def __read_credentials():
  import json
  with open('mywifi_cred.json', 'r') as cred:  
    wcred = json.load(cred)
  return wcred

def pin_status(req):
  pin.on()
  if req.status_code == 200:
    sleep(0.5)
  else:
    sleep(2)
  pin.off()

def device_id():
  machine_id = unique_id()
  from ubinascii import hexlify 
  return hexlify(machine_id).decode('utf-8')