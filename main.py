from random import random

import requests as requests
url = "https://api.telegram.org/bot1098854739:AAHZNQBQGtdSpi5pm1ZmEFI9i2Eg47-fFUg"


# function that get chat id
def get_chat_id(update):
    chat_id = update['message']["chat"]["id"]
    return chat_id


# function that get message text
def get_message_text(update):
    message_text = update["message"]["text"]
    return message_text


# function that get last_update
def last_update(req):
    response = requests.get(req + "getUpdates")
    response = response.json()
    result = response["result"]
    total_updates = len(result) - 1
    return result[total_updates]  # get last record message update


# create function that let bot send message to user
def send_message(chat_id, message_text):
    params = {"chat_id": chat_id, "text": message_text}
    response = requests.post(url + "sendMessage", data=params)
    return response


# main function reply message back
def main():
    update_id = last_update(url)["update_id"]
    while True:
        update = last_update(url)
        if update_id == update["update_id"]:
            if get_message_text(update).lower() == "hi" or get_message_text(update).lower() == "hello":
                send_message(get_chat_id(update), 'Hello Welcome to our bot. Type "Play" to roll the dice!')
            else:
                send_message(get_chat_id(update), "Sorry Not Understand what you inputted:( I love you")
            update_id += 1


# calling the function to make it reply
main()
