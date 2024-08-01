import re

def cell_to_col(cell_to_correct):
    # Caso inicie com traço, importação inverteu coluna
    # sequencia abaixo arruma o caso
    if cell_to_correct[0] == '-':
        # Metacaracter ^ refere-se a inico de string
        start_pattern = r"^-+\s*"
        # Substitui pelo padrão: retira hifen
        cell_to_correct = re.sub(start_pattern, "", cell_to_correct)
        # Substitui pelo padrão: Move hífen
        move_pattern = r"(\d+\s\w+)"
        cell_to_correct = re.sub(move_pattern, r"\1 - ", cell_to_correct)

    # Retira R$ e toda vez que tiver traço, adiciona espaço para aplicarmos o set_group_pattern
    cell_to_correct = cell_to_correct.replace('-', ' -')
    # Nos casos onde aparece string antes do número
    # retira a string
    cell_to_correct = cell_to_correct.split()

    try:
        float(cell_to_correct[0])
    except:
        cell_to_correct.remove(cell_to_correct[0])
        pass

    cell_to_correct = ' '.join(cell_to_correct)

    # Coletando os valores
    set_group_pattern = r'([0-9.,]+\s\w+)\s*([0-9,.-]+)\s*([0-9,.-]+)\s*([0-9,.-]+)\s*([0-9,.-]+)'
    pattern_match = re.search(set_group_pattern, cell_to_correct)
    
    return pattern_match.group(1), pattern_match.group(2), pattern_match.group(3), pattern_match.group(4), pattern_match.group(5)