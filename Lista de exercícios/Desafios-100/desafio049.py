#Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for. - Desafio 049
n = int(input("Digite um número para ver sua tabuada: "))
print(f"Segue a tabuada do número \033[33m{n}\033[m")
print('=-=' * 5)
for tab in range(1, 11):
    mult = n * tab
    print(f"{n} x {tab :^2} = {mult :^2}")
print('=-=' * 5)