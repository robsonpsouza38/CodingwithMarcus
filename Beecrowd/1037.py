numero = float(input())

if numero>=0:

    if numero <= 25:
        print("Intervalo [0,25]")
    elif numero <=50:
        print("Intervalo (25,50]")
    elif numero <= 75:
        print("Intervalo (50,75]")
    elif numero <= 100:
        print("Intervalo (75,100]")
    else:
        print("Fora de intervalo")
else:
    print("Fora de intervalo")


        


