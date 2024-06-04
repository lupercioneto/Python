'''
Crie um programa que leia a idade e o sexo de várias pessoas. 
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. - Desafio 069
'''

from time import sleep

print(f"""{'-' * 30} 
{"CADASTRE UMA PESSOA"} 
{'-' * 30}""")
qth = qtm20menos = qt18mais = 0

while True:
    #Condições e repetições para idade
    idade = int(input("Idade: "))
    while idade <= 0 or idade > 124:
        idade = int(input("Por favor, insira uma idade entre 1 e 124 anos: "))

    if idade > 18: 
        qt18mais += 1

    #Condições e repetições para sexo
    sex = str(input("Sexo [\033[34mM\033[m/\033[31mF\033[m]: ")).upper().strip()[0]
    while sex not in 'MmFf':
        sex = str(input("Por favor, selecione apenas \033[34mM\033[m para masculino e \033[31mF\033[m para feminino: ")).upper().strip()[0]

    if sex in 'Mm':
        qth += 1
    
    #Condição para mulheres com menos de 20 anos
    if idade < 20 and sex in 'Ff':
        qtm20menos += 1
    print("-" * 30)

    #Condições para confirmar (ou não) a continuação do cadastro
    cont = str(input("Quer continuar? [S/N]: ")).upper().strip()[0]

    if cont in 'Nn':
        break
    elif cont not in 'SsNn': 
        cont = str(input('Por favor, insira apenas \033[32mS\033[m para "Sim" ou \033[31mN\033[m para "Não": ')).upper().strip()[0]

print("\033[1;33mPROCESSANDO...\033[m")
sleep(2)
print(f"""- Total de pessoas com mais de 18 anos: {qt18mais}
- Total de homens cadastrados: {qth}
- Total de mulheres com menos de 20 anos: {qtm20menos}""")
    