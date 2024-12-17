import re
import requests
import json
import os


def remove_digit(name):
    return re.sub(r'^\d+\s', '', name)

def card_validate2(cardname):
    cardname = remove_digit(cardname)
    url =  f"https://api.scryfall.com/cards/named?exact={cardname}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data['name']
    else:
        return False