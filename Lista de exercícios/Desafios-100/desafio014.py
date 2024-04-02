'''
Crie um programa que leia uma temperatura digitada (em graus celsius [°C]) e converta a mesma para farenheit e Kelvin
- Desafio 014
'''
c = float(input("Qual a temperatura de onde você está (°C)?"))
f = (c * 1.8) + 32 
k = c + 273
print("A temperatura de {}°C, convertida para Fahrenheit, é de {}°F" .format(c,f))
print("A temperatura convertida para Kelvin será de {}K " .format(k))