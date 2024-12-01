num = int(input())

if num >10:
    print("num eh maior que 10 ")
elif num >5:
    print("maior que 5")
elif num>3:
    print("maior que 3")
else:
    print("menor igual a 3")


# if num>5:
#     print(1)
# if num>10:
#     print(2)
# else: 
#     print(3)

p,r   = map(int,input().split())

if p:
    if r:
        print("A")
    else:
        print("B")
else:
    print("C")

