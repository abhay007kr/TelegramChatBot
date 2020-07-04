

url="https://api.telegram.org/bot1098854739:AAHZNQBQGtdSpi5pm1ZmEFI9i2Eg47-fFUg"

#Function to get Chat ID

def get_chat_id(update):
    chat_id = update["message"]["chat"]["id"]
    return chat_id

