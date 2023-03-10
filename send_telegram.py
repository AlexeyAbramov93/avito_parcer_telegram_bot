import requests

def send_telegram(api_token, chat_id, text):
    try:
        requests.get('https://api.telegram.org/bot{}/sendMessage'.format(api_token), params=dict(
            chat_id=chat_id,
            text=text
        ))
    except Exception as ex:
        print(ex)