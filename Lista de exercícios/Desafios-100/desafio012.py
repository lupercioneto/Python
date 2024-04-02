#Faça um programa que leia o preço de um produto e retorne seu preço com 5% de desconto - Desafio 012
p = float(input("Digite o preço do produto: R$"))
d5 = (5/100 * p)
pd = (p - d5)
print("O preço descontado foi R${:.2f} (desconto de 5%) e seu novo preço é de R${:.2f}" .format(d5, pd))

''''
Também é possível realizar a atividade 
sem o uso das variáveis "d5" e "pd",
caso não haja necessidade de guardar valores das variáveis.
Veja o exercício seguinte para entender melhor (desafio013.py)
'''
