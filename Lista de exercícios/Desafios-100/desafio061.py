'''
Refaça o DESAFIO 51,
lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão 
usando a estrutura while. - Desafio 061
'''

from time import sleep

#Inserção de dados
print(f"{"=-=" * 3} Gerador de PA {'=-=' * 3}")
pn = int(input("Primeiro Termo: "))
r = int(input("Razão: "))
qtt = int(input("Quantiade de termos: "))

c = 1 #Contador de quantidade de termos
term = pn #Primeiro termo 

print("\n\033[1;34mPROCESSANDO...\033[m")
sleep(2)

#Estrutura de repetição para uma PA
while c <= qtt:
    print(term, end=' --> ')
    term += r
    c += 1 
print("\033[1;36mFIM DA PA\033[m")

