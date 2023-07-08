import random

print()
print('ATENÇAO:')
print('A escolha do computador é completamente aleatoria')
print('A tua jogada não afecta a sua escolha')
def ppt():
    opcoes = ['pedra', 'papel', 'tesoura']

    print()
    print('|-------PEDRA PAPEL TESOURA-------|')
    ver_pontos()
    print()

    escolha = input('Pedra, papel ou tesoura? ')
    pc = random.choice(opcoes)
    print(f'O computador escolheu: {pc.upper()}')
    print()

    if escolha.lower() == pc:
        print('EMPATE')
    elif escolha.lower() == 'pedra' and pc == 'tesoura' or escolha.lower() == 'papel' and pc == 'pedra' or escolha.lower() == 'tesoura' and pc == 'papel':
        print('GANHASTE! PARABÉNS!')
        mais_pontos('jogador')
    elif escolha.lower() not in opcoes:
        print(f'Opcção {escolha.upper()} inválida. Escolhe entre Pedra, Papel ou Tesoura')
    else:
        print('QUE PENA. PERDESTE.')
        mais_pontos('computador')
    novo_jogo()

def novo_jogo():
    jogar = input('JOGAR DE NOVO? (S/N): ').lower()
    if jogar == 's':
        ppt()
    elif jogar == 'n':
        print()
        print('|-----------FIM DO JOGO----------|')
        ver_pontos()
    else:
        print('Opcção inválida.')
        novo_jogo()

def ver_pontos():
    print(f'   |JOGADOR: {pontos_jogador}  | COMPUTADOR: {pontos_pc}|')

def mais_pontos(pontuacao):
    if pontuacao == 'jogador':
        global pontos_jogador
        pontos_jogador += 1
    else:
        pontuacao == 'computador'
        global pontos_pc
        pontos_pc +=1


pontos_jogador = 0
pontos_pc = 0

ppt()
