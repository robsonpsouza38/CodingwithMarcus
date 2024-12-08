# def calcular_valor_total (codigo, quantidade):


# # fazer uma tabela de preços (em R$)
# precos = {
#     1: 4.00
#     2: 4.50
#     3: 5.00
#     4: 2.00
#     5: 1.50 
# }

# if codigo in precos:
#     valor_unitario = precos[codigo]
#     valor_total = valor_unitario * quantidade 
#     return valor_total 


# # dados de entrada 
# codigo = int(input())
# quaatidade = int(input())
# # càlculo e exibição do resultado com 2 casas decimais
# valor_total = calcular_valor_total (codigo, quantidade)

# print(f"Total R$ {valor_total:.2f}")

codigo, quantidade = map(int, input().split())

if codigo ==1:
    preco =4
elif codigo==2:
    preco = 4.5
elif codigo==3:
    preco = 5
elif codigo==4:
    preco = 2
elif codigo==5:
    preco = 1.5

total = preco * quantidade
print(f"Total: R$ {total:.2f}")