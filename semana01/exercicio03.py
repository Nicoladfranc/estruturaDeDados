#Após aquele exercicio 2 dificil este daqui não foi tao problematico, consegui me guiar pelo outro sem necessitar de ajuda.
class Lista:
    def __init__(self, info=None):
        self.info = info
        self.prox = None
def merge(l1, l2):
    lista3 = []
    valores1 = l1
    valores2 = l2
    while valores1 is not None or valores2 is not None:
        if valores1 is not None:
            lista3.append(valores1.info)
            valores1 = valores1.prox
        if valores2 is not None:
            lista3.append(valores2.info)
            valores2 = valores2.prox
    return lista3
  
l1 = Lista(5)
l1.prox = Lista(10)
l2 = Lista(6)
l2.prox = Lista(2)
lista3 = merge(l1, l2)
print("mesclagem:")
for valor in lista3:
    print(valor)
