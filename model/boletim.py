class Boletim:
    def __init__(self, numero, ano, dia_pesquisa, mes_pesquisa, ano_pesquisa, path):
        self._numero = numero
        self._ano = ano
        self._dia_pesquisa = dia_pesquisa
        self._mes_pesquisa = mes_pesquisa
        self._ano_pesquisa = ano_pesquisa
        self._path = path if path[:6] != '/admin' else f'https://www.fatecmogidascruzes.com.br/{path}'

    def __str__(self):
        return (f'Boletim {self._numero}/{self._ano}\n'+
                f'Pesquisa: {self._dia_pesquisa}/{self._mes_pesquisa}/{self._ano_pesquisa}\n'+
                f'URL: {self._path}')
