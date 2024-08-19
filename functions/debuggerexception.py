import sys
import ipdb
import traceback

def debugger(type, value, tb):
    '''
    Função para debug com ipdb caso ocorra uma exceção não tratada

    type = tipo da exceção
    value = mensagem de erro associada à exceção
    tb = objeto traceback, com informações da pilha de chamada
    '''
    traceback.print_exception(type, value, tb)
    ipdb.pm()  # Entra no post-mortem debugging

'''
sys.excepthook: Função padrão que lida com exceções não tratadas
- Trocamos por nossa função
- Quando o Python chama sys.excepthook (que agora é info), ele passa automaticamente os
três parâmetros que info pede
'''
sys.excepthook = debugger