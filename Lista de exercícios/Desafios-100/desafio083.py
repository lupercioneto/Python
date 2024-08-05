'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu programa deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta. - Desafio 083
'''

#Lista para armazenar os parênteses da expressão digitada pelo usuário
parent = list()
cores = ('\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[m')
expruser = str(input("Digite uma expressão: "))

#Percorrendo cada elemento da expressão
for p in expruser:

    #Se o elemento encontrado for um parênteses se abrindo, será adicionado à lista
    if p == '(':
        parent.append('(')

    #Se for um parênteses fechando, podem ser duas possibilidades:
    elif p == ')':
        
        #Se houver pelo menos um parêntese na lista, este será excluído, assim entende-se que o parêntese em questão já foi fechado
        if len(parent) > 0:
            parent.pop()
        else:
            parent.append(')')
            break

#Ao final, se todos os parênteses forem excluídos e a lista ficar vazia, significará que todos os parênteses tiveram seus pares abertos e fechados
if len(parent) == 0:
    print(f"Sua expressão está {cores[1]}VÁLIDA{cores[4]}!")
else:
    print(f"Sua expressão está {cores[0]}INVÁLIDA{cores[4]}")
