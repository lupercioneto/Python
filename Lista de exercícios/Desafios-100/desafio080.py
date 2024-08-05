'''
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o método sort()). 
No final, mostre a lista ordenada na tela. - Desafio 080
'''
numbers = list()
cores = ('\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[m')

#Inserção dos outros 4 valores numéricos
for i in range(0,5):
    num = int(input("Digite um valor: "))

    #Caso o número adicionado seja o primeiro da lista ou seja maior que o último número da lista
    if i == 0 or num > numbers[-1]:   
        numbers.append(num)
        print(f"Valor {num} adicionado ao {cores[0]}FINAL{cores[4]} da lista...\n")
    
    else:
        index = 0 
        while index < len(numbers):
            if num <= numbers[index]:
                numbers.insert(index, num)
                print(f"Valor {num} adicionado ao índice {index} da lista...\n")
                break
            index += 1

print(f"""{'=-' * 30}
Os valores digitados em ordem foram {numbers}""")
