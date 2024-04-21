class Pilha:
    def __init__(self, max_tamanho=10):
        self.max = max_tamanho  
        self.n = 0  
        self.itens = [] 

    def pilha_vazia(self):
        return self.n == 0

    def pilha_cheia(self):
        return self.n == self.max

    def pilha_push(self, valor):
        if self.pilha_cheia():
            print("Erro: pilha cheia")
            return False
        self.itens.insert(0, valor) 
        self.n += 1
        return True

    def pilha_pop(self):
        if self.pilha_vazia():
            print("Erro: pilha  vazia")
            return None
        self.n -= 1
        return self.itens.pop(0)  

    def topo_pilha(self):
        if not self.pilha_vazia():
            return self.itens[0]
#pedro
class Historico:
    def __init__(self, max_tamanho):
        self.max = max_tamanho
        self.itens = []

    def adicionar(self, item):
        if len(self.itens) == self.max:
            self.itens.pop(0) 
        self.itens.append(item)

    def mostrar(self):
        print("Histórico:")
        for i, item in enumerate(self.itens, 1):
            print(f"{i}. {item}")

    def limpar(self):
        self.itens = []
#nicolas
def eh_sinal(caracter):
    return caracter in ['+', '-', '*', '/', '**']

def precedencia(sinal):
    if sinal in ['+', '-']:
        return 1
    elif sinal in ['*', '/']:
        return 2
    else:
        return 0

def calcular_operacao(sinal, numero1, numero2):
    if sinal == '+':
        return numero1 + numero2
    elif sinal == '-':
        return numero1 - numero2
    elif sinal == '*':
        return numero1 * numero2
    elif sinal == '/':
        if numero2 == 0:
            raise ValueError("Divisão por zero!")
        return numero1 / numero2
    elif sinal == '**':
        return numero1 ** numero2
#pedro
def is_negative(caracter, next_caracter):
    return caracter == '-' and not eh_sinal(next_caracter)

def avaliar_expressao(expressao):
    pilha_sinais = Pilha()  
    pilha_numeros = Pilha()  
    operando = ''

    def e_numero(caracter):
        try:
            float(caracter)
            return True
        except ValueError:
            return False

    for caracter in expressao:
        if e_numero(caracter):
            if is_negative(operando, caracter):
                if not pilha_numeros.pilha_cheia():
                    pilha_numeros.pilha_push(-float(operando))  # Números negativos são tratados aqui
                    operando = ''
                else:
                    print("Erro: A pilha de números está cheia")
                    return None
            else:
                operando += caracter
        else:
            if operando:
                if not pilha_numeros.pilha_cheia():
                    pilha_numeros.pilha_push(float(operando))
                    operando = ''
                else:
                    print("Erro: A pilha de números está cheia")
                    return None
            if eh_sinal(caracter):
                while not pilha_sinais.pilha_vazia() and precedencia(pilha_sinais.topo_pilha()) >= precedencia(caracter):
                    sinal = pilha_sinais.pilha_pop()
                    numero2 = pilha_numeros.pilha_pop()
                    numero1 = pilha_numeros.pilha_pop()
                    resultado = calcular_operacao(sinal, numero1, numero2)
                    pilha_numeros.pilha_push(resultado)
                if not pilha_sinais.pilha_cheia():
                    pilha_sinais.pilha_push(caracter)
                else:
                    print("Erro: A pilha de sinais está cheia")
                    return None
                #nicolas
            elif caracter == '(':
                if not pilha_sinais.pilha_cheia():
                    pilha_sinais.pilha_push(caracter)
                else:
                    print("Erro: A pilha de sinais está cheia")
                    return None
            elif caracter == ')':
                while pilha_sinais.topo_pilha() != '(':
                    sinal = pilha_sinais.pilha_pop()
                    numero2 = pilha_numeros.pilha_pop()
                    numero1 = pilha_numeros.pilha_pop()
                    resultado = calcular_operacao(sinal, numero1, numero2)
                    pilha_numeros.pilha_push(resultado)
                pilha_sinais.pilha_pop()

    if operando:
        if not pilha_numeros.pilha_cheia():
            pilha_numeros.pilha_push(float(operando))
        else:
            print("Erro: A pilha de números está cheia")
            return None

    while not pilha_sinais.pilha_vazia():
        sinal = pilha_sinais.pilha_pop()
        if sinal == '-':
            numero2 = pilha_numeros.pilha_pop()
            numero1 = pilha_numeros.pilha_pop()
            resultado = calcular_operacao(sinal, numero1, numero2)
            pilha_numeros.pilha_push(resultado)
        else:
            numero2 = pilha_numeros.pilha_pop()
            numero1 = pilha_numeros.pilha_pop()
            resultado = calcular_operacao(sinal, numero1, numero2)
            pilha_numeros.pilha_push(resultado)

    return pilha_numeros.pilha_pop()
