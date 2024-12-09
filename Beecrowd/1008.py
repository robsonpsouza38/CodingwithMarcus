# Nº funcionário + Nº Horas trabalhadas + valor recebido por hora
numero_funcionario = int(input("Digite o número do funcionário: ")) 
numero_hora_trabalhada = int(input()) 
valor_rebido_hora = float(input())

salary = numero_hora_trabalhada * valor_rebido_hora
# Exibição de resultados com 2 saídas (nº e salário do funcionário)
print(f"NUMBER = {numero_funcionario}")
print(f"SALARY = U$ {salary:.2f}")


