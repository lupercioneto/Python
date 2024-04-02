# Question 1: Faça um Programa que peça dois números e imprima o maior deles.
n1 = float(input("Digite um número:"))
n2 = float(input("Digite um segundo número:"))
if n1 > n2: 
    print("O número maior é", n1)
else:
    print("O número maior é", n2)

# Question 2: Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
n1 = float(input("Digite um número:"))
if n1 > 0:
    print("O número apresentado é positivo")
else:
    print("O número apresentado é negativo")


''' Question 3: Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:

A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''

n1 = int(input("Digite uma nota:"))
n2 = int(input("Digite uma segunda nota:"))
M = (n1 + n2)/2
if M >= 7:
    print("Aprovado")

elif M < 7: 
    print("Reprovado")

elif M == 10:
    print("Aprovado com distinção")
