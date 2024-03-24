class Lista:
    def __init__(self, info=None):
        self.info = info
        self.prox = None
        

def cria_lista():
    return Lista()

def insere_lista(lst, valor):
    novo= Lista(valor)
    novo.prox = lst
    return novo

def lista_imprime(lst):
    atual= lst
    while atual is not None:
        print(atual.info)
        atual = atual.prox
        
def lista_vazia(lst):
    return lst is None


def retira_n(lst, valor):
    while lst is not None and lst.info == valor:
        lst = lst.prox

    atual= lst
    while atual is not None and atual.prox is not None:
        if atual.prox.info == valor:
            atual.prox = atual.prox.prox
        atual = atual.prox

    return lst
    
lst = cria_lista()
lst=insere_lista(lst, 50)
lst= insere_lista(lst, 60)
lst= insere_lista(lst, 50)
lst= insere_lista(lst, 30)
lst= retira_n(lst, 50)




lista_imprime(lst)
