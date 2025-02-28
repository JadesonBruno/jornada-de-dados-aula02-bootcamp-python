# Desafio - Refatorar o projeto da aula anterior evitando Bugs!
# Para resolver os bugs identificados — tratamento de entradas inválidas que não podem ser convertidas para um número de ponto flutuante e 
# prevenção de valores negativos para salário e bônus, você pode modificar o código diretamente. Isso envolve adicionar verificações adicionais 
# após a tentativa de conversão para garantir que os valores sejam positivos.

# 1) Solicita ao usuário que digite seu nome

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

# 4) Calcule o valor do bônus final

# 5) Imprima cálculo do KPI para o usuário

# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?

name = input("Type your name: ")

if name.isdigit():
    raise ValueError ("Error: You entered your name incorrectly.")
elif not name:
    raise ValueError ("Error: Name cannot be empty.")
elif name.isspace():
    raise ValueError ("Error: You entered only spaces.")
try:
    salary = float(input("Type your salary: "))
except ValueError as e:
    print(f"Error: {e}")
    exit()
try:
    bonus = float(input("Type your bonus: "))
except ValueError as e:
    print(f"Error: {e}")
    exit()

CONSTANTE_BONUS = 1000

final_bonus = CONSTANTE_BONUS + salary * bonus

print(f'''###============###\nMr./Mrs. {name},\nYour salary is: {salary}\nAnd your final bonus is: {final_bonus}\n###============###''')