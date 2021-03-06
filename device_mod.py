from time import sleep

from machine import ADC, Pin, unique_id

pin = Pin(5, Pin.OUT)
pin2 = Pin(2, Pin.OUT)
adc0 = ADC(0)


def __try_connect(sta_if):
    while not sta_if.isconnected():
        pin2.on()
        sleep(0.5)
        pin2.off()
        sleep(0.5)


def do_connect():
    import network

    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("connecting to network...")
        sta_if.active(True)
        wcred = __read_credentials()
        sta_if.connect(wcred.get("essid"), wcred.get("password"))
        __try_connect(sta_if)
    print("network config:", sta_if.ifconfig())


def __read_credentials():
    import json

    with open("mywifi_cred.json", "r") as cred:
        wcred = json.load(cred)
    return wcred


def pin_status(resp):
    pin2.off()
    print("request api {}".format(resp.status_code))
    if resp.status_code == 200:
        pin2.on()
        sleep(0.3)


def device_id():
    machine_id = unique_id()
    from ubinascii import hexlify

    return hexlify(machine_id).decode("utf-8")


def do_on_off_led(resp):
    pin_status(resp)
    led_action = str(resp.json().get("led_status")).lower()
    if led_action == "on" and adc0.read() >= 500:
        pin.on()
    elif led_action == "off" or adc0.read() < 500:
        pin.off()
