import re
import ipdb
import pandas as pd

# Criando objeto regex para tornar mais eficiente
correct_pattern = re.compile(r'([0-9.,]+\s\w+)\s*([0-9,.-]+)\s*([0-9,.-]+)\s*([0-9,.-]+)\s*([0-9,.-]+)')

def cell_split(series_value):
    '''
    Função core, realiza o distrinchamento dos valores celula, separa-os em grupos
    e os retorna uma tupla com esses valores segmentados.

    Input:
    - Valor da celula que possui unidade e os valores
    - Celula tem de ter as 5 propriedades: Unidade, os 4 valores monetários

    Output:
    - Tupla dos 5 valores segmentados
    '''
    # Caso inicie com traço, importação inverteu coluna
    # sequencia abaixo arruma o caso
    if series_value[0] == '-':
        # Metacaracter ^ refere-se a inico de string
        start_pattern = r"^-+\s*"
        # Substitui pelo padrão: retira hifen
        series_value = re.sub(start_pattern, "", series_value)
        # Substitui pelo padrão: Move hífen
        move_pattern = r"(\d+\s\w+)"
        series_value = re.sub(move_pattern, r"\1 - ", series_value)

    # Toda vez que tiver traço, adiciona espaço para aplicarmos o set_group_pattern
    series_value = series_value.replace('-', ' -')
    # Nos casos onde aparece string antes do número
    # retira a string
    series_value = series_value.split()

    try:
        float(series_value[0])
    except:
        series_value.remove(series_value[0])
        pass

    series_value = ' '.join(series_value)

    # Coletando valores que atendam completamente o regex
    pattern_match = correct_pattern.fullmatch(series_value)
    
    return pattern_match.group(1), pattern_match.group(2), pattern_match.group(3), pattern_match.group(4), pattern_match.group(5)

def cell_to_col(series_produto, series_val_unid):
    '''
    Esta função retorna um series de tuplas, sendo
    cada tupla o distrinchamento dos valores, anteriormente
    concatenados da series.

    Para atribuir cada distrinchamento como se fossem separados
    em colunas:
    - Colete o valore de retorno
    - Descompacte-o com Starred Expression dentro da função zip

    A atribuição da operação acima construirá tuplas com os valores
    organizados como se estivessem em colunas. Capture os valores
    organizados através de atribuição segmentada (devem ser 5 valores):
    - t1, t2, t3, t4, t5 = zip(*valor_retornado)
    - Cada t (tupla) é a sequencia organizada para ser atribuida a uma
    coluna de dataframe
    '''
    padrao_sem_unidade = re.compile(r'\s?[0-9,.-]+\s*[0-9,.-]+\s*[0-9,.-]+\s*[0-9,.-]+')

    def organize_when_unit_below(row):
        '''
        Função destinada a concatenar as unidades, quando estão na linha debaixo
        a linha de valores, que está na linha acima
        '''
        index = row.name

        if row.iloc[0] != None and bool(padrao_sem_unidade.fullmatch(row.iloc[0])):
            unity = df_val_unid.iloc[index + 1, 0]
            df_val_unid.iloc[index + 1, 0] = None
            row.iloc[0] = f'{unity} {row.iloc[0]}'

        return row

    if series_produto.count() == series_val_unid.count():
        return series_val_unid.apply(cell_split)
    
    # Transformado em df para poder utilizar axis
    # Sem isso, estava interpretando os valores isoladamente como str
    series_val_unid.name = 'valores'
    df_val_unid = pd.DataFrame(series_val_unid)
    df_val_unid = df_val_unid.apply(organize_when_unit_below, axis=1)
    series_val_unid = df_val_unid['valores'].dropna() # Retorna pra Series

    if series_produto.count() == series_val_unid.count():
        return series_val_unid.apply(cell_split)
    else:
        print('\nComportamento inexperado em cell_to_col! Quantidade de produto diferente de quantidade de valores')
        print('>>> Iniciando debugger')
        ipdb.set_trace()