'''Crie um programa que analise o nome de uma pessoa 
(Escrita em maiúsculas, minúsculas, quantidade de letras e qual é seu primeiro nome)
Desafio 022
'''

print("Bem-vindo ao analisador de nomes! Por favor insira seu nome completo logo abaixo:")
nome = str(input("")).strip()
print("Seu nome com todas as letras maiúsuculas é {}" .format(nome.upper()))
print("Seu nome com todas as letras minúsuclas é {}" .format(nome.lower()))
print("Seu nome possuí {} letras ao todo" .format(len(nome) - nome.count(' ')))
sep = nome.split()
print("Seu primeiro nome é {} e ele possui {} letras" .format(sep[0], len(sep[0])))

'''.split() 
- Parâmetros adicionais: 
* sep (refere-se ao caractere que irá separar a string); 
* maxsplit (quantidade de separações a ser realizada)'''

