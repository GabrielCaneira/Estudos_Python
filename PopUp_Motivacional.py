
import tkinter as tk
import random
import time

frases = [
"A persistência é o caminho do êxito.",
"Pequenos passos levam a grandes conquistas.",
"Aprender a programar é como aprender um novo idioma: exige prática e dedicação.",
"Cada linha de código é uma oportunidade para criar algo incrível.",
"Erros são apenas oportunidades para aprender e melhorar.",
"A criatividade e a programação andam de mãos dadas.",
"A paciência é uma virtude fundamental na programação.",
"Não tenha medo de tentar algo novo na programação.",
"A programação é a arte de transformar ideias em realidade.",
"Com persistência e dedicação, você pode conquistar qualquer desafio na programação.",
"Não desista quando enfrentar um bug. Resolva-o e siga em frente.",
"A programação é como um quebra-cabeça fascinante. Encaixe as peças e veja a imagem completa.",
"Aprender a programar é como ter uma superpoderosa caneta para criar o futuro.",
"Cada linha de código que você escreve é um passo em direção ao seu objetivo.",
"A programação é uma forma de arte digital.",
"Aprender a programar é como abrir as portas para um mundo de possibilidades.",
"A curiosidade é a chave para a evolução na programação.",
"Seja paciente com você mesmo. A programação requer tempo e prática.",
"Aprender a programar é como aprender a resolver problemas com criatividade.",
"A persistência é a chave para superar qualquer obstáculo na programação.",
"A programação é um campo em constante evolução. Esteja sempre disposto a aprender.",
"A melhor maneira de aprender a programar é colocar as mãos na massa.",
"A programação é um caminho para criar soluções inovadoras.",
"Aprender a programar é como aprender a falar a língua das máquinas.",
"Cada erro que você comete na programação é uma oportunidade para aprender algo novo.",
"A criatividade é a chave para transformar problemas em soluções na programação.",
"A programação é como uma aventura em que você cria o seu próprio destino.",
"Com determinação e dedicação, você pode alcançar qualquer objetivo na programação.",
"Aprender a programar é como aprender a ler e escrever em um novo mundo digital.",
"A programação é uma dança entre lógica e criatividade.",
"Não tenha medo de cometer erros na programação. Eles são oportunidades de aprendizado.",
"A persistência na programação leva a resultados surpreendentes.",
"A programação é uma ferramenta poderosa para transformar o mundo ao seu redor.",
"Aprender a programar é como construir um castelo de ideias e lógica.",
"A programação é uma maneira de expressar sua imaginação e resolver problemas.",
"Com dedicação e prática, você pode dominar qualquer linguagem de programação.",
"A programação é um campo em constante crescimento. Aproveite as oportunidades.",
"Aprender a programar é como adquirir uma nova forma de pensar e raciocinar.",
"A criatividade é o ingrediente secreto para escrever um código único.",
"A programação é uma arte que combina lógica e imaginação.",
"Não tenha medo de perguntar e buscar ajuda na comunidade de programadores.",
"Aprender a programar é como ter a capacidade de dar vida às suas ideias.",
"A programação é uma jornada de aprendizado contínuo.",
"Com dedicação e esforço, você pode se tornar um mestre da programação.",
"A programação abre portas para carreiras emocionantes e cheias de oportunidades.",
"Aprender a programar é como adquirir superpoderes digitais.",
"A resolução de problemas é o coração da programação.",
"A programação é uma forma de criar soluções inteligentes para desafios do mundo real.",
"Aprender a programar é como aprender a tocar um instrumento: requer prática e dedicação.",
"A programação é uma forma de deixar uma marca no mundo digital."
]

def mostrar_popup():

     frase = random.choice(frases)
     popup = tk.Tk()
     popup.wm_title('Ganha confiança')
     label = tk.Label(popup, text=frase)
     label.pack(padx=100, pady=100)
     popup.mainloop()

intervalo = 20 * 60

while True:
    mostrar_popup()
    time.sleep(intervalo)