#Dissecando uma variável - Desafio 004
from time import sleep
a = input("Digite algo: ")
print("\033[33mANALISANDO...\033[m")
sleep(3)
print(f"O tipo primitivo do valor digitado é --> \033[31m{type(a)}\033[m")
sleep(2)
print(f"O valor digitado é alfa-numérico? --> \033[32m{a.isalnum()}\033[m")
sleep(2)
print(f"O valor digitado é numérico? --> \033[31m{a.isnumeric()}\033[m")
sleep(2)
print(f"O valor digitado é alfabético? --> \033[32m{a.isalpha()}\033[m")
sleep(2)
print(f"O valor digitado está em maiúsculas? --> \033[31m{a.isupper()}\033[m")
sleep(2)
print(f"O valor digitado está em minúsculas? --> \033[32m{a.islower()}\033[m")
sleep(2)
#Para Python, capitalizado significa uma palavra com sua letra inicial maiúscula
print(f"O valor digitado está capitalizado? --> \033[31m{a.istitle()}\033[m")
sleep(2)
print(f"O valor digitado é somente espaços em branco? --> \033[32m{a.isspace()}\033[m")

#A função input sempre retorna uma string, se não for especficada