'''
Lista de exercícios de python

1. Faça um Programa que peça um número e então mostre a mensagem __O número informado foi [número]__.

2. Faça um Programa que peça dois números e imprima a soma.

3. Faça um Programa que peça as 4 notas bimestrais e mostre a média.

4. Faça um Programa que converta metros para centímetros.

5. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

6. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

7. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
'''
#Question 1
n = int(input("digite um número qualquer:"))
print("O número informado foi", n )

#Question 2
n1 = int(input("Digite um número para somar:"))
n2 = int(input("Digite um segundo número para somar:"))
n3 = n1 + n2
print("A soma dos números", n1, "e", n2, "resulta em", n3)

#Question 3
N1 = float(input("Insira sua primeira nota:"))
N2 = float(input("Insira sua segunda nota:"))
N3 = float(input("Insira sua terceira nota:"))
N4 = float(input("Insira sua quarta nota:"))
M = (N1 + N2 + N3 + N4)/4
print("Sua média final é:", M) 

#Question 4
M = int(input("Digite uma medida (em metros):"))
C = M * 100
print("A medida de", M, "metro(s) em centímetros é", C , "centímetro(s)")

#Question 5
R = int(input("Digite um valor para o raio do círculo:"))
Ac = (3,14 * R ** 2)
print("A área do círculo de raio", R, "é de", Ac)

#Question 6
Lq = int(input("Digite um valor para a aresta de um quadrado:"))
Aq = (Lq ** 2)
Aq2 = Aq * 2
print("A área do quadrado de lado", Lq, "é", Aq, "e seu dobro é", Aq2)

#Question 7 
Gh = int(input("Digite o valor que você ganha por hora (apenas números):"))
Ht = int(input("Digite a quantidade horas trabalhadas em um mês:"))
Gt = (Gh * Ht) 
print("Seu ganho mensal foi de", Gt, "reais.")