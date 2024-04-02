#Crie um conversor de moedas - - Desafio 010
r = float(input("Quanto dinheiro você tem atualmente? R$"))
#Cotação do dia 02/04/2024 (04/02/2024, US format)
D = r / 5.06
L = r / 6.35
E = r / 5.44
Y = r / 0.033
print("-" * 38)
print("Com R${:.2f} você pode comprar $US{:.2f}" .format(r, D))
print("Com R${:.2f} você pode comprar {:.2f}€" .format(r, E))
print("Com R${:.2f} você pode comprar {:.2f}£" .format(r, L))
print("Com R${:.2f} você pode comprar {:.2f}¥" .format(r, Y))
print("-" * 38)
