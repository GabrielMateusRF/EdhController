import requests
import json
import os
from Addcard import add_card

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



def main():
    while True:
        print("\nMenu:")
        print("1. Adicionar carta")
        print("2. Imprimir lista")
        print("3. Testes")
        print("0. Sair")
        number = input("Digite o número de uma opção: ")
        try:
            number=int(number)
        except:
            number='_'
        match number:
            case 1:
                add_card()
            case 2:
                print(lista)
            case 3:
                print("sou feito para testes")
                
            case 0:
                break
            case _:
                print("valor inválido")



if __name__ == "__main__":
    main()