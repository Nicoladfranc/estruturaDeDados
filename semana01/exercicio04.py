class Lista:
    def __init__(self, info=None):
        self.info = info
        self.prox = None

def cria_lista():
    return Lista()

def insere_lista(lst, valor):
    if lst is None: 
        return Lista(valor)
    atual = lst
    while atual.prox is not None:
        atual = atual.prox
    novo = Lista(valor)
    atual.prox = novo
    return lst  

def inverte(lst):
    atual = None
    referencia = lst
    prox = None
    
    while referencia is not None:
        prox = referencia.prox
        referencia.prox = atual
        atual = referencia
        referencia = prox
    
    return atual

def print_lista(lst):
    current = lst
    while current is not None:
        print(current.info)
        current = current.prox

lst = cria_lista()
lst = insere_lista(lst, 30)
lst = insere_lista(lst, 40)
lst = insere_lista(lst, 50)
lst = insere_lista(lst, 10)
lst_invertida = inverte(lst)
print("lista invertida:")
print_lista(lst_invertida)

