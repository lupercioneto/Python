'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida - Deasfio 043
'''

from time import sleep

p = float(input("Qual seu peso? (Kg): "))
a = float(input("Qual sua altura? (m): "))
imc = p/a ** 2
print("\n\033[33mCALCULANDO...\033[m\n")
sleep(3)
print(f"Seu \033[32mIMC\033[m é de {imc:.1f}")

#Condições
if imc < 18.5:
    print("Você está abaixo do peso, alimente-se mais!")
elif imc <= 25:
    print("Você esté com um peso ideal! Continue assim!")
elif imc <= 30:
    print("Você está com \033[4;31msobrepeso\033[m, regule sua alimentação!")
elif imc <= 40:
    print("Você está em estado de \033[1;mOBESIDADE\033[m, tome cuidado!")
else: 
    print("Você está em estado de \033[1;31mOBESIDADE MÓRBIDA\033[m, procure tratamento imediatamente!")