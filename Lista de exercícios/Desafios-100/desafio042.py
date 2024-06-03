'''
Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes - Desafio 042
'''
from time import sleep
print('-=-' * 9)
print("\033[36mAnalisador de Triângulos △\033[m")
print('-=-' * 9)
print("Irei analisar se é possível construir um triângulo\ncom base nas medidas que me der e irei classificá-lo!\n")
sleep(3)

l1 = float(input("Digite a primeira medida: "))
l2 = float(input("Digite a segunda medida: "))
l3 = float(input("Digite a terceira medida: "))
print("\n\033[1;33mANALISANDO...\033[m\n")
sleep(3)

if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
    print("Os segmentos analisados podem formar um triângulo \033[32m△\033[m")
    if l1 == l2 == l3:
        print("O triângulo formado será \033[1;34mEQUILÁTERO\033[m")
    elif l1 != l2 != l3 != l1:    
        print("O triângulo formado será \033[1;31mESCALENO\033[m")
    else:
        print("O triângulo formado será \033[1;33mISÓCELES\033[m")
else: 
    print("Não é possível construir um triângulo com estas medidas \033[31m△\033[m")

#Não há necessidade de utilizar módulo matemático (|x|), como foi feito no Desafio 035 