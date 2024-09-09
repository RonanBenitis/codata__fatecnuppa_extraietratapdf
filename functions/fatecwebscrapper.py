import re
import requests
from bs4 import BeautifulSoup
from model.boletim import Boletim

def fatec_webscrapper(dir_origem, list_boletins):
    boletins_existente_max_number = max(int(boletim._numero) for boletim in list_boletins)

    url = 'https://www.fatecmogidascruzes.com.br/admin/workGroups/view/NUPPA'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    all_links = soup.find_all('a')

    for link in all_links[::-1]:
        if link.string is not None and 'boletim semanal' in link.string.lower():
            # buscando numero e ano boletim
            group_numero_ano = re.search(r"\b(\d{2,3})\/(\d{4})\b", link.text)
            numero_boletim = group_numero_ano.group(1)
            ano_boletim = group_numero_ano.group(2)
            print(f'Lendo boletim {numero_boletim}/{ano_boletim} no site da NUPPA')

            if int(numero_boletim) <= boletins_existente_max_number:
                print(f'Boletim {numero_boletim} já se encontra no sistema')
                print('Não há mais boletins a serem baixados\n')
                break

            # buscando data pesquisa
            group_data = re.search(r"\b(\d{2})\/(\d{2})\/(\d{2,4})\b", link.text)
            dia_pesquisa = group_data.group(1)
            mes_pesquisa = group_data.group(2)
            ano_pesquisa = group_data.group(3)

            url_boletim = link['href']

            boletim = Boletim(numero_boletim, ano_boletim, dia_pesquisa, mes_pesquisa, ano_pesquisa, url_boletim)

            _baixar_boletim(boletim, dir_origem)

def _baixar_boletim(boletim: Boletim, path: str) -> None:
    response = requests.get(boletim._path)

    if response.status_code == 200:
        with open(f'{path}/boletim_{boletim._numero}.{boletim._ano}_{boletim._dia_pesquisa}.{boletim._mes_pesquisa}.{boletim._ano_pesquisa}.pdf', 'wb') as file:
            file.write(response.content)
        
        print(f'Boletim {boletim._numero} baixado com sucesso!\n')
    else:
        print(f'Erro ao baixar boletim {boletim._numero}')