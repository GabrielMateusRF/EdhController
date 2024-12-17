import requests
import json
import os
from Addcard import add_card, remove_card
from DataManager import use_decklist
from JsonRead import read_Json


def print_data():
    file = 'Names.json'
    for item in  read_Json(file):
        if item['Quantity'] > 0:
            print(f'{item['Quantity']} {item['Name']}')


def decklist_create():
    with open('Deck1.txt', 'r') as file:
        text = file.readlines()
    for i,item in  enumerate(text):
        print(f'{item}')

# Na API do scrifall deve ter como tutorar por SET + Collector numbers, mas o problema é que, assim a versão da carta seria salva
# Da para criar um sistema que, pega e confirmar a carta a partir do set number, mas quando pesquisa só pega o nome 
# Talvez fosse interessante fazer o deck creation inteiro aqui dentro do sistema.

def main():
    while True:
        print("\nMenu:")
        print("1. Adicionar carta")
        print("2. Imprimir lista")
        print("3. Remover carta")
        print("4. Teste")
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
                print_data()
            case 3:
                remove_card()
            case 4:
                use_decklist()
            case 0:
                break
            case _:
                print("valor inválido")



if __name__ == "__main__":
    main()