'''
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
'''
from time import sleep
disc = dict()
cores = {'vermelho': '\033[1;31m', 'verde': '\033[1;32m', 'amarelo': '\033[1;33m', 'azul': '\033[1;34m','neutro': '\033[m'}

#Inserindo os dados no dicionário
disc['nome'] = str(input("Nome do aluno: ")).strip().title()
while disc['nome'].isalpha() == False:
    nome = str(input(f"Por favor, digite um nome apenas com caractres {cores['amarelo']}ALFABÉTICOS{cores['neutro']}: ")).strip().title()

disc['media'] = float(input(f"Média de {disc['nome']}: "))
while disc['media'] < 0 or disc['media'] > 10:
    media = float(input(f"Por favor, digite uma média {cores['azul']}VÁLIDA{cores['neutro']} (entre 0 e 10): "))

#Analisando a situação do aluno
if disc['media'] >= 7:
    disc['situação'] = 'Aprovado'
elif 5 <= disc['media'] < 6.9:
    disc['situação'] = 'Avaliação Final'
else: 
    disc['situação'] = 'Reprovado'

print(f"\n{cores['amarelo']}PROCESSANDO...{cores['neutro']}")
sleep(2.5)

print(f"""\n{'ALUNO' :<8} {'MÉDIA' :<8} {'SITUAÇÃO' :>10}
{disc['nome'] :<8} {disc['media'] :<8} {disc['situação'] :>10}""")


