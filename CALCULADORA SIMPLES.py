          # Calculadora simples
print()
print('        CALCULADORA SIMPLES')
print()

try:
    num1 = float(input('   Digite o primeiro numero:'))
    operacao = input('   Qual a operação que pretende fazer? (+, -, *, /):')
    num2 = float(input('   Digite o segundo numero:'))

    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        if num2 == 0:
            print('   Impossivel de fazer divisão por 0!')
            resultado = None
        else:
            resultado = num1 / num2

    else:
        print('   resultado inválido')
        resultado = None
    if resultado is not None:
        print(f'   o resultado da tua conta é {resultado}')

except ValueError:
    print('   Algo de errado não está certo. Começa de novo!')