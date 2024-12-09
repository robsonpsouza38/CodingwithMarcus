A, B = map(float, input(), split())

media = (A + B)/2 

if media >= 7:
    print("Aprovado")
elif media >= 4:
    print("Recuperacao")
else:
    print("Reprovado")
    