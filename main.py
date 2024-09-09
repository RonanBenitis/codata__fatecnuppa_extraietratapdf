import functions
from pathlib import Path

# inicializa debugger ipdb em caso de exceção
functions.debugger

dir_origem = Path.cwd() / 'data' / 'raw' / 'pdf'
dir_destino = Path.cwd() / 'data'/ 'processed'

list_boletins_inicio = functions.get_boletins_list(dir_origem)

# Webscrapper para baixar os PDFs do site
functions.fatec_webscrapper(dir_origem, list_boletins_inicio)

# Atualizando lista de boletins
list_boletins = functions.get_boletins_list(dir_origem)

# Se nenhuma lista foi baixada, encerra aplicação
if len(list_boletins_inicio) == len(list_boletins):
    print('Nenhum arquivo baixado. Os boletins estão atualizados.')
    print('Encerrando aplicação!')
    exit()

for boletim in list_boletins:
    print(f'>>> BOLETIM LIDO: {boletim._numero}/{boletim._ano}')
    df_nuppa = functions.estrutura_tabela_pdf(boletim)
    # Salva produção
    df_nuppa.to_excel(f'{dir_destino / boletim._numero}-2022.xlsx', index=False)
    print(f'=== Boletim {boletim._numero} salvo como {boletim._numero}-2022! ===\n')
