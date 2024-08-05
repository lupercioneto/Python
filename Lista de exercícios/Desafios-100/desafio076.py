'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
No final, mostre uma listagem de preços, organizando os dados em forma tabular. - Desafio 076
'''
prodpreç = ('Iphone Pro Max', 15000, 'Bolsa', 67.49,
            'Lápis', 3,'Notebook Positivo', 1700.99,
            'Mouse Gamer Razer', 180,'Caderno', 24.99,
            'Gabinete RGB', 1249,'Teclado RGB', 349.79)
cores = ('\033[31m','\033[32m','\033[33m','\03[34m','\033[m')

print(f"""{'=' * 40}
{'LISTAGEM DE PREÇOS' :^40}
{'=' * 40}""")

#Para cada posição, inciando do índice zero e indo até o fim da tupla
for position in range(0, len(prodpreç)):
    if position % 2 == 0:
        print(f"{prodpreç[position]:.<30}", end='')
    else: 
        print(f"{cores[1]}R${prodpreç[position]:.2f}{cores[4]}")
print('=' * 40)