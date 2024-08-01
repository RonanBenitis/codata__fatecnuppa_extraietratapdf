import numpy as np
import pandas as pd
import tabula
from pathlib import Path
from functions import celltocol
from functions import getboletimandcoleta

col_order = ['PRODUTO', 'UNIDADE MEDIDA', 'COMUM', 'MINIMO', 'MAXIMO',
             'MEDIA', 'MEDIANA', 'COLETA']

def filtra_produto(cell_value):
    lista_de_nomes = ['GRUPO', 'Comum Mínimo Máximo', 'Produto', 'Mediana',
                      'NaN', 'NAN', 'nan']
    cell_value = str(cell_value)

    # NOTE
    # Any: Percorre uma lista booleana. Se encontrar algum verdadeiro
    # retorna verdadeiro, se tudo for falso, retorna falso.
    # Ou seja, criamos uma lista de verdadeiro/falso com lista_de_nomes
    # e se a celula der verdadeira em algum nome, retorna verdadeiro.
    # Isso evita repetir 'string' in cell_value toda hora.
    return not (cell_value is np.nan or cell_value is None or
        any(nome in cell_value for nome in lista_de_nomes))

def estrutura_tabela_pdf(pdf_path):
    print(f'Iniciando estruturação de {pdf_path.name}')
    boletim_num, data_coleta = getboletimandcoleta.get_boletim_and_coleta(pdf_path)
    df_model = pd.DataFrame(columns=col_order)
    dfs_pdf = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)

    # Iterando pelas paginas (DataFrames)
    for df_pdf in dfs_pdf:
        # Cria um arquivo raw
        dir_raw_xlsx = Path.cwd() / 'data'/ 'raw' / 'xlsx'
        df_pdf.to_excel(f'{dir_raw_xlsx}/raw_{boletim_num}-2022.xlsx', index=False)
        
        # NOTE
        # Retira 'R$' pois houve um arquivo com bug onde
        # ao invés de coluna vazia, havia apenas 'R$'
        df_pdf = df_pdf.map(lambda x: str(x).replace('R$', '').replace(',', '.'))
        # Auxiliar, para não interferir na estrutura do dado
        aux_df_pdf = df_pdf.replace('nan', pd.NA).replace('', pd.NA)

        # >>> Retira primeira linha e retira colunas vazias
        for col in df_pdf.columns:
            # df_pdf[col].isnull().values: Deixa True se for null
            # ~df_pdf[col].isnull().values: Inverte, deixa False
            # any(): Se encontrar algum True, retorna True.
            # Validação: Se tiver True, tem valor. Se for False, tá vazio
            if any(~aux_df_pdf[col].isnull().values) is False:
                df_pdf = df_pdf.drop(col, axis='columns')

        # >>> COLUNA "PRODUTO"
        filtro_col_produto = df_pdf.iloc[:,0].apply(filtra_produto)
        df_model['PRODUTO'] = df_pdf.iloc[:,0][filtro_col_produto].reset_index(drop=True)

        # >>> COLUNA "UNIDADE MEDIDA" "COMUM" "MINIMO" "MAXIMO" "MEDIA"
        filtro_col_medida = df_pdf.iloc[:,1].apply(filtra_produto)
        col_medida_filtrado = df_pdf.iloc[:,1][filtro_col_medida]
        result = col_medida_filtrado.apply(celltocol.cell_to_col)
        df_um, df_comum, df_minimo, df_maximo, df_media = zip(*result)

        df_model['UNIDADE MEDIDA'] = df_um
        df_model['COMUM'] = df_comum
        df_model['MINIMO'] = df_minimo
        df_model['MAXIMO'] = df_maximo
        df_model['MEDIA'] = df_media
        
        # >>> COLUNA "MEDIANA"
        filtro_col_mediana = df_pdf.iloc[:,2].apply(filtra_produto)
        df_model['MEDIANA'] = df_pdf.iloc[:,2][filtro_col_mediana].reset_index(drop=True)

        # >>> COLUNA "COLETA"
        df_model['COLETA'] = data_coleta

        print(f'Tratamento de {pdf_path.name} realizado!')

        return boletim_num, df_model
