import random

opcoes = ['pedra', 'papel', 'tesoura']

print('|-------PEDRA PAPEL TESOURA-------|')
print()
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
else:
    print('QUE PENA. PERDESTE.')