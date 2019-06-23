import urequests as requests
from mywifi import pin_status, device_id

def get_joke():
  r = requests.get('https://official-joke-api.appspot.com/jokes/random')
  pin_status(r)
  return r.json()

def send_joke_telegram():
  joke = get_joke()
  if joke:
    text_message = '{}\nPunchline: {}'.format(joke.get('setup'), joke.get('punchline'))
    chat_id = 0
    if chat_id == 0:
      exit(1)
    response = {'message': {'from': {'username': device_id() }, 'chat': {'id': chat_id}, 'text': text_message}}
    telegram_botreq = requests.post('https://telegram-webhook-sample.herokuapp.com/', json=response)
    pin_status(telegram_botreq)
    telegram_botreq.close()

send_joke_telegram()
