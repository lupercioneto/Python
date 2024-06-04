'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
No final do programa, mostre: 
- A média de idade do grupo
- Qual é o nome do homem mais velho 
- Quantas mulheres têm menos de 20 anos.
'''
from time import sleep

cores = ('\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[m')

#Variáveis contadoras 
somaidade = 0
hmaisvelho = 0
idadehmaisvelho = 0
m20menos = 0
qtth = 0
qttm = 0

print(f"""{'=' * 25}
{cores[2]}{'CADASTRO DE PESSOAS' :^25}{cores[4]}
{'=' * 25}\n""")

for p in range(1,5):
    print(f"\n{"=" * 8} {p}° PESSOA {'=' * 8}")

    nome = str(input(f"Nome: ")).strip().title()
    idade = int(input(f"Idade: "))

    while idade < 0 or idade > 124:
        idade = int(input("Por favor, digite uma idade entre 1 e 124 anos: "))
    somaidade += idade #Somando as idades para fazer a média no final

    gen = str(input(f"Sexo da {p}° [{cores[3]}M{cores[4]}/{cores[0]}F{cores[4]}]: ")).strip().upper()[0]
    while gen not in 'MF':
        gen = str(input(f'Por favor, insira apenas {cores[3]}M{cores[4]} para "Masculino" e {cores[0]}F{cores[4]} para "Feminino": ')).strip().upper()[0]

    print("=" * 25)

    #Condição para saber o mais velho
    if p == 1 and gen == 'M' :
        hmaisvelho = nome
        idadehmaisvelho = idade
    else:
        if gen == 'M' and idade > idadehmaisvelho:
            hmaisvelho = nome
            idadehmaisvelho = idade 

    
    #Quantidade mulheres com menos de 20 anos 
    if gen == 'F' and idade < 20:
        m20menos += 1


    #Quantidade de homens
    if gen == 'M':
        qtth += 1

    #Quantidade de mulheres
    if gen == 'F':
        qttm += 1

media = somaidade/4 #Média de idade

print("=" * 45)
print(f"A média de idade do grupo é de {media :.1f} anos")
print(f"- Há {qttm} mulher(es) cadastradas" if qttm > 0 else "- Nenhuma mulher foi cadastrada.")
print(f"- Há {m20menos} mulher(es) com menos de 20 anos" if m20menos > 0 else "- Nenhuma mulher possuí menos de 20 anos.")
print(f"- O homem mais velho é {cores[3]}{hmaisvelho}{cores[4]} e ele possui {idadehmaisvelho} anos" if qtth > 0 else "- Nenhum homem foi informado")
print("=" * 45)