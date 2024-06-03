'''
Faça um programa que calcule a soma entre todos os números 
que são múltiplos de três e ímpares que se encontram no intervalo de 1 até 500. - Desafio 048
'''
soma = 0 #Soma dos termos incialmente: 0
qtt = 0 #Quantidade de termos inicial: Nenhum termo presente
for mult3 in range(1,501,2):
    if mult3 % 3 == 0:
        print(mult3, end=' ')
        soma += mult3 #Soma de todos os termos múltiplos de três (3) - É equivalente a: soma = soma + mult3 (Conceito de contador; Soma 1 (+1))
        qtt += 1 #Quantidade de termos que serão somados - É equivalente a: qtt = qtt + 1 (Conceito de acumalador; Soma um valor (+n1,+n2,...,+n))
'''
Cada vez que um número que é múltiplo de três é encontrado e somado à variável "soma", 
incrementamos também a variável "qtt" em 1.
'''
print("\nA soma dos {} valores listados é igual a {}" .format(qtt,soma))