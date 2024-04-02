#Escreva um programa que leia um valor em metros e o exiba em centímetros e milímetros converta - Desafio 008
v = float(input("Digite um valor, em metros:"))
km = (v/1000)
hc = (v/100)
dam = (v/10)
dm = (v * 10)
cm = (v * 100)
mm = (v * 1000)
print(f"A medida de {v}m corresponde a: \n {km}km \n {hc}hc \n {dam}dam \n {dm}dm \n {cm:.2f}cm \n {mm :.2f}mm ")
#Uso de f string 