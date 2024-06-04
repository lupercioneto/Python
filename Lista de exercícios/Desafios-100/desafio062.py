'''
Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos. - Desafio 062 
'''
from time import sleep

#Inserção de dados
pt = int(input("Primeiro Termo: "))
r = int(input("Razão: "))

#Variáveis para contagem
termo = pt #Primeiro termo 
cont = 1 #Contagem dos termos
total = 0 #Total de termos 
contin = 10 #Quantiade de termos adicionados a cada inserção nova

#Estrutura aninhada
while contin != 0:
    total += contin
    while cont <= total:
        print(termo, end=' --> ')
        termo += r
        cont += 1 
    print("\033[1;34mPAUSA\033[m")
    contin = int(input("Quantos termos a mais deseja adicionar?\nCaso contrário, digite \033[1;37m0\033[m: "))
print(f"Progressão finalizada com \033[1;32m{total}\033[m termos mostrados")