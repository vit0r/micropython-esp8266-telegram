import urequests as requests
from device_mod import device_id, do_on_off_led
from time import sleep


def on_off_led_pin():
    telegram_botresp = requests.get(
        'https://telegram-webhook-sample.herokuapp.com/')
    do_on_off_led(telegram_botresp)
    telegram_botresp.close()
    sleep(8)


while True:
    on_off_led_pin()
