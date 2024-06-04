'''
Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Porém, agora o jogador vai tentar adivinhar até acertar, 
mostrando no final quantos palpites foram necessários para vencer. - Desafio 058
'''
from random import randint
from time import sleep
from emoji import emojize

#Variáveis de armazenar número "pensado"
nc = randint(0,10)

print("""Vou pensar em um número entre \033[34m0 \033[me\033[m \033[34m10\033[m!
Tente adivinhar qual foi! Duvido você acertá-lo!""")

palp = int(input("Qual seu palpite? "))
while palp > 10 or palp < 0:
    palp = int(input("Por favor, digite apenas um número entre 0 e 10: "))
qtpalp = 1 #Contagem de palpites

#Estrutura de repetição
while palp != nc:
    #Dicas para o palpite
    if palp < nc:
        palp = int(input("Maior... Tente mais uma vez: "))
        qtpalp += 1
    if palp > nc:
        palp = int(input("Menor... Tente mais uma vez: "))
        qtpalp += 1
print(f"Você acertou com \033[33m{qtpalp}\033[m tentativas")

#Mensagens de parabenização de acordo com a qauntidade de acertos
if qtpalp == 1: 
    print(emojize("\nUau! Você é muito sortudo! \033[1;33mParabéns!\033[m:partying_face:"))
elif 2 <= qtpalp < 5:
    print(emojize("\nVocê foi bem! Com certeza eu consegueria esse resultado :smiling_face_with_sunglasses:"))
else:
    print(emojize("\nAcertou, mas demorou bastante hein?!:rolling_on_the_floor_laughing:"))