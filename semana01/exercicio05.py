class Lista:
    def __init__(self, info=None):
        self.info = info
        self.prox = None

def igual(l1, l2):
    while l1 is not None and l2 is not None:
        if l1.info != l2.info:  
            return False
        l1 = l1.prox
        l2 = l2.prox
    return l1 is None and l2 is None
  
def cria_lista(elementos):
    lst = None
    for elemento in reversed(elementos):
        lst = insere_lista(lst, elemento)
    return lst
def insere_lista(lst, valor):
    novo = Lista(valor)
    novo.prox = lst
    return novo

l1 = Lista(5)
l1.prox = Lista(10)
l2 = Lista(5)
l2.prox = Lista(10)

print(" Igualdade da listas:", igual(l1, l2))  
