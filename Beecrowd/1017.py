
# Leitura dos dados de entrada
tempo = int(input())
velocidade_media = int(input())

# Cálculo da distância percorrida
distancia = tempo * velocidade_media

# Cálculo da quantidade de litros necessária
litros = distancia / 12

# Exibição do resultado com 3 casas decimais
print(f"{litros:.3f}")

