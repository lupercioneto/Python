''' 
Faça um programa que tenha uma função chamada escreva(), 
que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.  - Desafio 096
'''
from time import sleep

#Definindo a função printspc
def printspc(msg):
    tam = len(msg) + 4 #A mensagem será alinhada de acordo o seu tamanho, juntamente com os espaços em branco no começo e fim da frase
    print(f"""{'~' * tam}
{f'  {msg}  '}
{'~' * tam}""")

#Programa principal
frases = []
cores = {'red': '\033[1;31m', 'green': '\033[1;32m', 'yellow': '\033[1;33m', 'blue': '\033[1;34m', 'standard': '\033[m'}

while True: #Lendo as frases digitadas pelo usuário e inserindo-as nas lista frases 
    mensagem = str(input(f"\nDigite uma mensagem: "))
    frases.append(mensagem)

    #Confirmação para continuar ou parar de digitar frases
    conf = str(input(f"Deseja continuar? [{cores['green']}S{cores['standard']}/{cores['red']}N{cores['standard']}]: ")).upper().strip()[0]
    while conf not in 'SN':
        conf = str(input(f'Por favor, digite apenas {cores["green"]}S{cores["standard"]} para "Sim" e {cores['red']}N{cores['standard']} para "Não": ')).upper().strip()[0]

    if conf in 'N':
        break

print(f"\n{cores['yellow']}ORGANIZANDO...{cores['standard']}")
sleep(2)

for i,f in enumerate(frases): #Percorrendo a lista e exibindo cada frase individualmente
    print(f"\n{cores['yellow']}Frase{cores['standard']} {i + 1}: ")
    printspc(f"{f}") #Chamando a função 
    sleep(1)