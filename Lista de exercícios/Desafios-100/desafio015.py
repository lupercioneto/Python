'''
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado. 
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
- Desafio 015
'''
kmr = float(input("Digite a quilometragem rodada do carro: "))
dalg = int(input("Por quantos dias ele foi alugado? "))
pc = (60 * dalg) + (0.15 * kmr) 
print("O preço a se pagar pelo aluguel do carro será de R${:.2f}" .format(pc))