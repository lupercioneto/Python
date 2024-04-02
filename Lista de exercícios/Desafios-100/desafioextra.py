'''
Extra - Crie um programa que leia o preço de um produto e mostre seu novo preço 
ao ser comprado à vista com 7% de desconto
e parcelado com 4% de aumento
- Desafio Extra
'''

p = float(input("Qual o preço do produto? R$"))
pavst = p - (7/100 * p)
pprcld = p + (4/100 * p)
print("O preço do produto à vista, com 7% de desconto, será de R${}" .format(pavst))
print("O preço do produto parcelado, com até 4% de aumento, será de {}" .format(pprcld))
print("Opçoes de parcelament disponíveis: 12x | 6x" )