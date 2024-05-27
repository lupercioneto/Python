#Crie um programa que leia um ângulo qualquer (em graus) e mostre o seu seno, cosseno e tangente     

from math import sin, cos, tan, radians
ang = float(input("Digite um valor para o ângulo: "))
sin = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print("Os valores do seno, cosseno e tangente de {}° são, respectivamente:\n {:.2f} {:.2f} {:.2f}" .format(ang, sin, cos, tan))

