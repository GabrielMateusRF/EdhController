import re
import requests
import json
import os
from Addcard import remove_data, save_data
from JsonRead import read_Json


#Flow:
# 1 ele vai receber um txt, por agora vai abrir aqui, mas num futuro terá que ser um file separado ou integrar
# ao JsonRead e transformar ele só em ReadData ou algo do tipo.
# 2 Após receber o dado, irá começar o processo de validar e montar uma lista, note que ele não vai poder logo
# tirar, pois caso dê um dado inválido o Return false tem que parar tudo e dar um aviso de erro.
# 3 Por fim modificar temporariamente somente os valores necessário#




#Isso claramente está no local errado, mas deixa ai por agora senão vou ficar me confundindo entre mil arquivos.

def deck_load():
    return open("decklists\missy_irl.txt",'r')

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
    
def veri_list_of_cards(release):
    f = deck_load()
    lines=(f.read().splitlines())
    print(lines)
    file = 'Names.json'
    for line in lines:
        cardname= card_validate2(line)
        print(cardname)
        finder=False
        for item2 in read_Json(file):
            if item2['Name']==cardname and (item2['Quantity'] > 0 or release):
                print("TESTE")
                finder=True 
        if not finder:
            return False, cardname, file
    return True, "nothing", file
        

def use_cards(list):
    file = 'Names.json'
    try:
        for line in list:
            for item in read_Json(file):
                if item['Name']==line and item['Quantity'] > 0:
                    item['Quantity'] =-1
                else:
                    raise ValueError("Aconteceu erro ao retirar as cartas, por favor, use o backup")
    except ValueError as e:
        print(f"ERRO: {e}. Tente novamente.")


def release_cards(list):
    file = 'Names.json'
    try:
        for line in list:
            for item in read_Json(file):
                if item['Name']==line:
                    item['Quantity'] =+1
                else:
                    raise ValueError("Aconteceu erro ao colocar as cartas, por favor, use o backup")
    except ValueError as e:
        print(f"ERRO: {e}. Tente novamente.")





    


def use_decklist():
    veri, card, list = veri_list_of_cards(False)
    if veri:
        print("Cartas foram separadas")
        use_cards(list)
    else:
        print(f'Há cartas não encontradas: {card}')


#NOTA: em release decklist, a carta já tem que ter um registro, essa NÃO pode ser uma maneira de registrar várias cartas
def release_decklist():
    veri, card, list = veri_list_of_cards(True)
    if veri:
        print("Cartas foram separadas")
        release_cards(list)
    else:
        print(f'A seguinte carta não está registrada: {card}')




    