class Lista:
    def __init__(self, info=None):
        self.info = info
        self.prox = None
        
def cria_lista():
    return Lista()

def insere_lista(lst, valor):
    novo = Lista(valor)
    novo.prox = lst
    return novo

def lista_imprime(lst):
    atual = lst
    while atual is not None:
        print(atual.info)
        atual = atual.prox
        
def lista_vazia(lst):
    return lst is None

def copia(lst):
    nova_lista = None
    atual = lst
    while atual is not None:
        nova_lista = insere_lista(nova_lista, atual.info)#recebe os valores da ista original
        atual = atual.prox
    return nova_lista
lista_original = cria_lista()
lista_original = insere_lista(lista_original, 3)
lista_original = insere_lista(lista_original, 7)
lista_original = insere_lista(lista_original, 10)

print("lista original:")
lista_imprime(lista_original)

copia_da_lista = copia(lista_original)
print("lista copia:")
lista_imprime(copia_da_lista)
