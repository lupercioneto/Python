'''
Faça um programa que leia o nome completo de uma pessoa, 
mostrando em seguida o primeiro e o último nome separadamente - Desafio 027
'''
print("Bem-vindo, Usuário!") 
nm = str(input("Digite seu nome completo: ")).strip().title()
varnm = nm.split()
print(f"""- Seu primeiro nome é {varnm[0]} 
- Seu último nome é {varnm[-1]}\n
- Juntos, eles formam {varnm[0] + ' ' + varnm[-1]}. \n""")