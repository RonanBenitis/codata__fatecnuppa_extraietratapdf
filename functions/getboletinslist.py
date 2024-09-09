import re
from model.boletim import Boletim

def get_boletins_list(dir_origem) -> list[Boletim]:

    list_boletins = []

    for file in dir_origem.glob('*.pdf'):
        boletim_re_group = re.search(r"_(\d{2,3}).(\d{4})_(\d{2}).(\d{2}).(\d{4})", file.name)
        numero_boletim = boletim_re_group.group(1)
        ano_boletim = boletim_re_group.group(2)
        dia_pesquisa = boletim_re_group.group(3)
        mes_pesquisa = boletim_re_group.group(4)
        ano_pesquisa = boletim_re_group.group(5)
        url_boletim = str(file) # Transformar WindowsPath em string

        boletim = Boletim(numero_boletim, ano_boletim, dia_pesquisa, mes_pesquisa, ano_pesquisa, url_boletim)

        list_boletins.append(boletim)
    
    return list_boletins