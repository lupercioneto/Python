#Crie um programa que sorteie o nome de quatro alunos - Desafio 019
#Biblioteca "random" permite "randomizar" elementos
from random import choice 
n = str(input("Digite um nome a ser sorteado:"))
n2 = str(input("Digite o nome do segundo aluno:"))
n3 = str(input("Digite o nome do terceiro aluno:"))
n4 = str(input("Digite o nome do quarto aluno:"))
l = [n, n2, n3, n4]

#A funcionalidade "choice" permite a escolha de um elemento qualquer da lista criada
s = choice(l)
print("O aluno sorteado foi {}" .format(s))