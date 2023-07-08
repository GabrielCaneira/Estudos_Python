import random

def ppt():
    opcoes = ['pedra', 'papel', 'tesoura']

    print()
    print('|-------PEDRA PAPEL TESOURA-------|')
    print()

    escolha = input('Pedra, papel ou tesoura? ')
    pc = random.choice(opcoes)
    print(f'O computador escolheu {pc}')
    print()

    if escolha.lower() == pc:
        print('EMPATE')
    elif escolha.lower() == 'pedra' and pc == 'tesoura':
        print('GANHASTE! PARABÉNS!')
    elif escolha.lower() == 'papel' and pc == 'pedra':
        print('GANHASTE! PARABÉNS!')
    elif escolha.lower() == 'tesoura' and pc == 'papel':
        print('GANHASTE! PARABÉNS!')
    elif escolha.lower() not in opcoes:
        print(f'Opcção {escolha.upper()} inválida. Escolhe entre Pedra, Papel ou Tesoura')
    else:
        print('QUE PENA. PERDESTE.')
    novo_jogo()

def novo_jogo():
    jogar = input('JOGAR DE NOVO? (S/N): ').lower()
    if jogar == 's':
        ppt()
    elif jogar == 'n':
        print()
        print('|-----------FIM DO JOGO----------|')
    else:
        print('Opcção inválida.')
        novo_jogo()

ppt()
