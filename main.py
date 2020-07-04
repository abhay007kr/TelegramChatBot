import requests

url = "https://api.telegram.org/bot1098854739:AAHZNQBQGtdSpi5pm1ZmEFI9i2Eg47-fFUg"


# Function to get Chat ID

def get_chat_id(update):
    chat_id = update["message"]["chat"]["id"]
    return chat_id


# function to get message text

def get_message_text(update):
    message_text = update["message"]["text"]
    return message_text


# function to get last update

def last_update(req):
    response = requests.get(req + "getUpdates")
    response = response.json()
    result = response["result"]
    total_updates = len(result) - 1
    return result(total_updates)
