import requests

def buscar_cartas(nome_carta, max_results=5):
    """Busca cartas no Scryfall e retorna uma lista de resultados.

    Args:
        nome_carta (str): O nome da carta a ser buscada.
        max_results (int, optional): O número máximo de resultados a serem retornados. Defaults to 5.

    Returns:
        list: Uma lista de dicionários, onde cada dicionário representa uma carta encontrada.
    """

    url = f"https://api.scryfall.com/cards/search?q={nome_carta}&include_multilingual=cards"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        resultados = data['data'][:max_results]
        return resultados
    else:
        return []

if __name__ == "__main__":
    nome_carta = input("Digite o nome da carta (parcialmente ou completo): ")
    resultados = buscar_cartas(nome_carta)

    if resultados:
        print(f"Foram encontradas {len(resultados)} cartas:")
        for carta in resultados:
            print(f"- {carta['name']} ({carta['set']}) - {carta['mana_cost']} - {carta['type_line']}")
    else:
        print("Nenhuma carta encontrada.")