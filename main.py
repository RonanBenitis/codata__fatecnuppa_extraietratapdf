import functions
from pathlib import Path

dir_origem = Path.cwd() / 'data' / 'raw' / 'pdf'
dir_destino = Path.cwd() / 'data'/ 'processed'

pdf_files = [f for f in dir_origem.glob('*.pdf')]

for file in pdf_files:
    print(f'>>> ARQUIVO PDF LIDO: {file.name}')
    boletim_num, df_nuppa = functions.estrutura_tabela_pdf(file)
    # Salva produção
    df_nuppa.to_excel(f'{dir_destino / boletim_num}-2022.xlsx', index=False)
    print(f'=== {file.name} salvo como {boletim_num}-2022! ===\n')
