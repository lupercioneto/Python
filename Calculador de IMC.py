P = float(input("Digite seu peso (em KG):"))
A = float(input("Digite sua altura (em metros):"))
IMC = P/A**2
if IMC < 18.5: 
    print("Seu IMC é", round(IMC, 2))
    print("Você está em estado de magreza. Procure alimentar-se mais e melhor!")

elif 18.5 <= IMC <= 24.9:
    print("Seu IMC é", round(IMC, 2))
    print("Sua saúde está em boas condições! Continue assim!")           

elif 25 <= IMC <= 29.9:
        print("Seu IMC é", round(IMC, 2))
        print("Você está acima do peso recomendado. Tome cuidado e previna-se!")
    

elif 30 <= IMC <= 39.9:
        print("Seu IMC é", round(IMC, 2))
        print("Cuidado! Você está com peso muito elevado! Procure ajuda médica!")

elif IMC >= 40:
    print("Seu IMC é:", round(IMC, 2))
    print("Você apresenta obesidade grave! Por favor, consulte um especialista médico com urgência para tentar reverter a situação!")

        
