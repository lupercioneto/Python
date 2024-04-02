#Crie um programa que leia o salário de um funcionário e exiba seu novo salário após um aumento de 15% - Desafio 013
s = float(input("Digite o salário do funcionário - R$"))
ns = s + (15/100 * s)
print("Com um salário de R${:.2f}, o novo salário desse funcionário, após um aumento de 15%, será de R${:.2f}" .format(s, ns))
#Também é possível realizar a atividade através de mais variáveis, como realizado no desafio anterior (desafio012.py)