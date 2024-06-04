'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto. - Desafio 057
'''
gen = str(input("Digite seu sexo [\033[34mM\033[m/\033[31mF\033[m]: ")).upper().strip()[0]
while gen not in 'MF': 
    gen = str(input("Sexo inválido. Informe \033[31mF\033[m (Feminino) ou \033[34mM\033[m (Masculino): ")).upper().strip()[0]
print(f"Sexo {gen} registrado")