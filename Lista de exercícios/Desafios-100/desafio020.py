#Crie um programa que leia o nome de 4 alunos e defina a ordem de apresentação de suas atividades
#Biblioteca "random", função shuffle (embaralhar)
from random import shuffle
n = str(input("Digite o nome do primeiro aluno:"))
n2 = str(input("Digite o nome do segundo aluno:"))
n3 = str(input("Digite o nome do terceiro aluno:"))
n4 = str(input("Digite o nome do quarto aluno:"))
l = [n, n2, n3, n4]
shuffle(l)
print("A ordem de apresentação será: \n {}" .format(l))

#Forma alternativa utilizada (Não entendi o funcionamento do método sample)
"""from random import sample
n = str(input("Digite o nome do primeiro aluno:"))
n2 = str(input("Digite o nome do segundo aluno:"))
n3 = str(input("Digite o nome do terceiro aluno:"))
n4 = str(input("Digite o nome do quarto aluno:"))
l = [n, n2, n3, n4]
o = sample(1, 4)
print("A ordem de apresentação será: \n {}" .format(l))"""