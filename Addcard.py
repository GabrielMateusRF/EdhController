import requests
import json
import os


def read_Json(file):
    if os.path.exists(file):
        with open(file, 'r') as f:
            data = json.load(f)
            for item in data:
                yield item

def save_data(name):
    file = 'Names.json'
    data_modificadas = []
    exists = False
    for item in read_Json(file):
        if item['Name'] == name:
            item['Quantity'] += 1 
            exists = True
        data_modificadas.append(item)
    
    if not exists:
        novo_dado = {
            "Name": name,
            "InDeck": False,
            "Quantity": 1
        }
        data_modificadas.append(novo_dado)
    
    with open(file, 'w') as f:
        json.dump(data_modificadas, f, indent=4) 
    if exists:
        print(f'O Name "{name}" já existia e a quantidade foi aumentada em 1.')
    else:
        print(f'O Name "{name}" foi salvo com sucesso.')

def card_search(data):
    if data['total_cards'] > 1:
        print(f"Foram encontradas {data['total_cards']} cartas que correspondem ao Name:")
        founddata=[]
        for i,carta in enumerate(data['data']):
            founddata.append(carta['name'])
            print(f" {i+1} - {founddata[i]}")
        while True:
            try:
                number=input("\nSelecione Qual carta quer: ")
                try:
                    number=int(number)
                except:
                    raise ValueError ("Tem que ser um número") 
                if number == 0:
                    raise ValueError("Deve ser maior que zero")
                if number > len(founddata):
                    raise ValueError ("Número não está nas opções")
                return founddata[number-1]
            except ValueError as e:
                    print(f"ERRO: {e} Tente Novamente")
    return data['data'][0]['name']

def card_validate(cardname):
    url =  f"https://api.scryfall.com/cards/search?q={cardname}&include_multilingual=cards"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()


        print(f"o total de cartas encontradas: {data['total_cards']}")
        if data['total_cards'] > 0:
           return card_search(data)
        else:
            return False
    else:
        return False

def valid_input():
        while True:
            try:
                cardname=input("Digite o Name da carta: ")
                if not cardname:
                    raise ValueError("Entrada inválida")
                if len(cardname)>100:
                    raise ValueError("Tamanho do Name inválido")
                cardfound=card_validate(cardname)
                if not cardfound:
                    return False
                return cardfound
            except ValueError as e:
                print(f"ERRO: {e}. Tente novamente.")

    

def add_card():
    card= valid_input()
    if not card:
        print("Carta não encontrada")
    else:
        print(card)
        save_data(card)


def valid_card():
    print("validate")