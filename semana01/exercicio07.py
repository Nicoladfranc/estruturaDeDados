class List:
    def __init__(self, info=None):
        self.info = info
        self.prox = None

def ultimo_circular(l):
    if not l or l.prox == l:
        return l
    ant = None
    atual = l.prox
    while atual and atual != l:
        ant = atual
        atual = atual.prox
    return ant

def insere_circular(l, val):
    novo = List(val)
    ult = ultimo_circular(l)
    if not ult: # lista vazia
        novo.prox = novo # elemento aponta para si mesmo
    else:
        novo.prox = l
        ult.prox = novo
    return novo

def imprime_circular(l):
    if not l:
        return
    
    atual = l
    contador = 0
    while contador < 10:
        print(atual.info, end=" -> ")
        atual = atual.prox
        contador += 1
        if atual == l:
            if contador < 10:
                atual = l
            else:
                break
    print("\n")

lst = None
lst = insere_circular(lst, 10)
lst = insere_circular(lst, 20)
lst = insere_circular(lst, 30)
insere_circular(lst, 40)
print("lista encadedea Circular:")
imprime_circular(lst)

