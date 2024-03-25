#Admito Esse exercicio foi complicado, passei dificuldades, utilizei o chat mas mesmo assim estava dando problemas na logica, ai resolvi fazer
#Com a logica do .prox.prox e mesmo assim foi complicado desenvolver sozinho, tive que pedir ajudas para alguns problemas com a posição que imprimia N.
class Lista:
    def __init__(self, info=None):
        self.info = info
        self.prox = None

def separar(lst, n):
    lista1 = Lista()  
    lista2 = Lista() 
    atual1 = lista1
    atual2 = lista2
    atual = lst

    while atual is not None:
        if atual.info != n:
            atual1.prox = Lista(atual.info)
            atual1 = atual1.prox
            atual = atual.prox
        else:
            atual1.prox = Lista(atual.info)  
            atual1 = atual1.prox
            atual = atual.prox  
            break

    while atual is not None:
        atual2.prox = Lista(atual.info)
        atual2 = atual2.prox
        atual = atual.prox

    return lista1.prox, lista2.prox  

lst = Lista(5)
lst.prox = Lista(10)
lst.prox.prox = Lista(3)
lst.prox.prox.prox = Lista(8)
lst.prox.prox.prox.prox = Lista(9)
lst.prox.prox.prox.prox.prox = Lista(2)
lista1, lista2 = separar(lst, 3)

print("lista 1")
atual = lista1
while atual is not None:
    print(atual.info)
    atual = atual.prox
print("lista 2")
atual = lista2
while atual is not None:
    print(atual.info)
    atual = atual.prox
