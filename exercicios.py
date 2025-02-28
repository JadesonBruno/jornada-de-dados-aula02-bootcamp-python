# Exercícios

# importado bibiliotecas necessárias
import math 

# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
""" valor_1 = int(input("Digite o valor 1: "))
valor_2 = int(input("Digite o valor 2: "))

soma = valor_1 + valor_2

print(f"A soma dos números é: {soma}") """

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
""" value = int(input("Digite o valor: "))
DIVISION_CONSTANT = 5

remainder_division = value % DIVISION_CONSTANT

print(f"The division remainder is: {remainder_division}") """
# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
""" value_1 = int(input("Type value 1: "))
value_2 = int(input("Type value 2: "))

multiplication = value_1 * value_2

print(f"The sum of numbers is: {multiplication}") """
# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
""" value_1 = int(input("Type value 1: "))1
value_2 = int(input("Type value 2: "))

division = value_1 // value_2

print(f"The division of numbers is: {division}") """

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
""" value = int(input("Type the value: "))

exponentiation = value ** 2

print(f"The exponentiation is: {exponentiation}") """

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
""" value_1 = float(input("Type value 1: "))
value_2 = float(input("Type value 2: "))

sum = value_1 + value_2

print(f"The sum of numbers is: {sum}") """

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
""" quantity_numbers = int(input("Quantity of numbers for average calculate: "))
list = []

for i in range(quantity_numbers):
    value = float(input("Type the value: "))
    list.append(value)

sum = sum(list)
print(sum)

average = sum / quantity_numbers

print(f'The average of values is: {average}') """

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
""" base = float(input("Type value of base: "))
exponent = float(input("Type value of exponent: "))

exponentation = base ** exponent

print(f"The exponentation is: {exponentation}") """

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
""" celsius_temperature = float(input("Type the temperature: "))

fahrenheit_temperature = (celsius_temperature * 9/5) + 32

print(f"The temperature in Fahrenheit is: {fahrenheit_temperature}") """

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
""" radius = float(input("Enter the radius value: "))
PI = math.pi

circle_area = PI * (radius ** 2)

print(f"The area of circle is: {circle_area:.2f}") """

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
""" word = input("Enter the word: ")

upper_word = word.upper()

print(f"The upper word is: {upper_word}") """

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
""" complete_name = input("Enter the complete name: ")

lower_complete_name = complete_name.lower()

print(f"The upper word is: {lower_complete_name}") """
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
""" phrase = input("Enter the phrase: ")

without_spaces = phrase.strip()

print(f"The phrase without spaces is: {without_spaces}") """

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
""" date = input("Enter the date in format (dd/mm/yyyy): ")

day = date.split("/")[0]
month = date.split("/")[1]
year = date.split("/")[2]

print(f"Day: {day}\nMonth: {month}\nYear: {year}") """

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
""" string_1 = input("Enter the string 1: ")
string_2 = input("Enter the string 2: ")

concatenete = string_1 + " " + string_2

print(f"The concatenete string is: {concatenete}") """

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
""" boolean_1 = input("Enter boolean value 1 (True/False): ").strip().title()
boolean_2 = input("Enter boolean value 2 (True/False): ").strip().title()

and_result = boolean_1 and boolean_2

print(f'The boolean value is: {and_result}') """

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
""" boolean_1 = input("Enter boolean value 1 (True/False): ").strip().title()
boolean_2 = input("Enter boolean value 2 (True/False): ").strip().title()

or_result = boolean_1 or boolean_2

print(f'The boolean value is: {or_result}') """
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
""" boolean_input = input("Enter boolean value 1 (True/False): ").strip().title()

if boolean_input != 'True' and boolean_input != 'False':
    raise ValueError("Invalid input. Please enter 'True' or 'False' ")

boolean_value = boolean_input == 'True'

not_boolean = not boolean_value

print(f'The boolean value is: {not_boolean}') """

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
""" number_1_input = input("Enter number 1: ")
number_2_input = input("Enter number 2: ")

try:
    number_1 = float(number_1_input)
    number_2 = float(number_2_input)
except ValueError:
    raise ValueError("Invalid input. Enter a valid number.")

number_comparative = number_1_input == number_2_input 

print(f'Inputs are equal numbers: {number_comparative}') """

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
""" number_1_input = input("Enter number 1: ")
number_2_input = input("Enter number 2: ")

try:
    number_1 = float(number_1_input)
    number_2 = float(number_2_input)
except ValueError:
    raise ValueError("Invalid input. Enter a valid number.")

number_comparative = number_1_input != number_2_input 

print(f'Inputs are different numbers: {number_comparative}') """

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação