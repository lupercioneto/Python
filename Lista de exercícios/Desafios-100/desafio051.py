'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
No final, mostre os 10 primeiros termos dessa progressão. - Desafio 051
'''


print(f"""{'-=-' * 10}
{"     10 TERMOS DE UMA PA"}
{'-=-' * 10}""")

#Inserção dsos dados; - n --> primeiro termo da PA - r --> razão da PA
n = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite a razão: "))

#Fórmula da PA (Auxiliar)
u10 = n + (11 - 1) * r

#Laço de repetição
for pa in range(n, u10, r):
    print(pa, end=' -> ')
print("\033[33mFim da PA\033[m")
