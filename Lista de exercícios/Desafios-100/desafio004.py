#Dissecando uma variável - Desafio 004
a = input("Digite algo:")
print("O tipo primitivo do valor digitado é ",type(a))
print("O valor digitado é alfa-numérico?", a.isalnum())
print("O valor digitado é numérico?", a.isnumeric())
print("O valor digitado é alfabético?", a.isalpha())
print("O valor digitado está em maiúsculas?", a.isupper())
print("O valor digitado está em minúsculas?", a.islower())

#Para Python, capitalizado significa uma palavra com sua letra inicial maiúscula
print("O valor digitado está capitalizado?", a.istitle())
print("O valor digitado é somente espaços em branco?", a.isspace())

#A função input sempre retorna uma string, se não for especficada