#Pedro
import logicatb

print("Calculadora TekPix 2000")

print("Comandos:")
print(" opção 1- Você irá realizar cálculos")
print(" opção 2- Verificar histórico")
print(" opção 3- Limpar histórico")
print(" opção 4- Desistir dessa calculadora")


while True:
    opc = input("Digite a Opção: ")

    if opc == '1':
        expressao = input("Digite a expressão matemática")
        resultado = logicatb.avaliar_expressao(expressao)
        print("Resultado:", resultado)

    elif opc == '2':
        print("Histórico de cálculos:")

    elif opc == '3':
        print("Adeus Histórico!")
        print("Histórico limpo com sucesso!")
        print("Histórico atual:  ")


    elif opc == '4':
        print("Chega de falar sobre Calculadora\nVamos falar sobre coisa boa...\nVocê já ouviu falar sobre a câmera Tekpix?\nEla é a mais vendida do Brasil")
        break

