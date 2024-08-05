'''
Faça um programa que tenha uma função chamada contador(). 
Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
'''


from time import sleep
cores = {'red': '\033[1;31m','green': '\033[1;32m','yellow': '\033[1;33m',
         'blue': '\033[1;34m','standard': '\033[m'}

#Definindo a função endofline
def endofline():
    print(end=f'{cores['yellow']}FIM{cores['standard']}')

#Definindo a função linedetail
def linedetail():
    print('=-' * 40)

#Definindo a função count
def count():

    #Contagens pré-definidas
    linedetail()
    print("Contagem de 1 até 10, de 1 em 1: ") #Contagem de 1 até 10, de 1 em 1
    for n in range(1, 11, 1):
        print(f"{n}", end=' --> ', flush=True) 
        sleep(0.5)
    endofline()
    print()
    sleep(1)

    linedetail()
    print("Contagem de 10 até 0, de 2 em 2: ") #Contagem de 10 até 0, de 2 em 2
    for n in range(10, -2, -2):
        print(f"{n}", end=' --> ', flush=True)
        sleep(0.5)   
    endofline()
    print()
    sleep(1)

    #CONTAGEM PERSONALIZADA
    print("\nAgora é a sua vez de personalizar a contagem!")
    sleep(1)

    while True:
        #Inserindo as contagens personalizada
        start = int(input(f"\n{cores['green']}Início{cores['standard']}: "))
        end = int(input(f"{cores['red']}Fim{cores['standard']}: "))
        step = int(input(f"{cores['yellow']}Passo{cores['standard']} (Ou razão): "))

        while step == 0:
            step = int(input("Por favor, digite outro número para o passo (): "))

        #Para contagens em ordem crescente
        if start < end:
            if step < 0:
                step = - (step) * 2

            linedetail()
            print(f"Contagem de {start} até {end}, de {step} em {step}: ")
            for n in range(start, end + 1, step):
                print(f"{n}", end=' --> ', flush=True) 
                sleep(0.5)
            endofline()
                
        #Para contagens em ordem decrescente
        elif start > end:
            if step > 0: 
                step =  (- (step) * 2)//2
            linedetail()
            print(f"Contagem de {start} até {end}, de {step if step > 0 else -(step)} em {step if step > 0 else -(step)}: ") 
            for n in range(start, end - 1, step):
                print(f"{n}", end=' --> ', flush=True)
                sleep(0.5)
            endofline()
        
        sleep(0.5)
        conf = str(input(f"\nDeseja continuar? [{cores['green']}S{cores['standard']}/{cores['red']}N{cores['standard']}]: ")).strip().upper()[0]
        while conf not in 'SN':
            conf = str(input(f'Por favor, digite apenas {cores["green"]}S{cores["standard"]} para "Sim" e {cores["red"]}N{cores["standard"]} para "Não": ')).upper().strip()[0]
        
        if conf in 'N':
            print(f"{cores['yellow']}ENCERRANDO PROGRAMA...{cores['standard']}")
            sleep(2)
            break
count()