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
""" Escreva um programa que converta a temperatura de Celsius para Fahrenheit. O programa deve solicitar ao usuário a temperatura em Celsius e, 
utilizando try-except, garantir que a entrada seja numérica, tratando qualquer ValueError. 
Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida. """

""" try:
    celsius_temperature = float(input("Type the temperature: "))

    fahrenheit_temperature = (celsius_temperature * 9/5) + 32

    print(f"The temperature in Fahrenheit is: {fahrenheit_temperature}")

except ValueError:
    print("Error: The input is not a number.") """

# 22: Verificador de Palíndromo
# Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). 
# Utilize try-except para garantir que a entrada seja uma string. 
# Dica: Utilize a função isinstance() para verificar o tipo da entrada.

""" try:
    word = input("Enter word: ")

    if not word:
        raise ValueError ("Input cannot be empty.")

    if isinstance(word, str):
        cleaned_word = word.strip().replace(" ", "")
        word_reversed = cleaned_word[::-1]
        is_palindrome = cleaned_word == word_reversed
        
        if is_palindrome == True:
            print("The word is palindrome.")
        else:
            print("The word is not palindrome.")

except ValueError as e:
    print(f"Error: {e}")

else: 
    print("Everything went well!") """

# 23: Calculadora Simples
# Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. 
# Use try-except para lidar com divisões por zero e entradas não numéricas. 
# Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. Imprima o resultado ou uma mensagem de erro apropriada.
""" try:
    operation = input("Enter a operation (+, -, *, /): ")
    if operation not in ("+", "-", "*", "/"):
        raise ("Error: input operation invalid")
        
    number_1 = float(input("Enter a number 1: "))
    number_2 = float(input("Enter a number 2: "))


    if operation == "+":
        result = number_1 + number_2
    elif operation == "-":
        result = number_1 - number_2
    elif operation == "*":
        result = number_1 * number_2
    elif operation == "/":
        result = number_1 / number_2

    print(f'The result of operation is: {result}')

except ValueError:
    print("Error: Input is not a number.")

except ZeroDivisionError:
    print("Error: It's not permitted division by zero.") """

# 24: Classificador de Números
# Escreva um programa que solicite ao usuário para digitar um número. Utilize try-except para assegurar 
# que a entrada seja numérica e utilize if-elif-else para classificar o número como "positivo", "negativo" ou "zero". 
# Adicionalmente, identifique se o número é "par" ou "ímpar".
""" try:
    number = float(input("Enter a number: "))

    if number > 0:
        classifier = "Positive"
    elif number < 0:
        classifier = "Negative"
    else:
        classifier = "Zero"

    print(f'This is number is {classifier}.')

    if (number % 2) == 0:
        print("It´s also even.")  
    else:
        print("It´s alse odd.")  

except ValueError:
    print("Error: Input is invalid, it´s not a number.") """

# 25: Conversão de Tipo com Validação
# Crie um script que solicite ao usuário uma lista de números separados por vírgula. O programa deve converter 
# a string de entrada em uma lista de números inteiros. Utilize try-except para tratar a conversão de cada número 
# e validar que cada elemento da lista convertida é um inteiro. Se a conversão falhar ou um elemento não for um inteiro, 
# imprima uma mensagem de erro. Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.
""" try:
    list_input = input("Enter numbers separated by ',': ")
    integer_list = list_input.split(",")

    for i in range(len(integer_list)):
        integer_list[i] = int(integer_list[i])

    print(integer_list)

except ValueError:
    print(f"Error: The element {integer_list[i]}, is not a integer")

else:
    print("Everything went well.") """

# Solução alternativa:
""" entrada_lista = input("Digite uma lista de números separados por vírgula: ")
numeros_str = entrada_lista.split(",")
numeros_int = []
try:
    for num in numeros_str:
        numeros_int.append(int(num.strip()))
    print("Lista de inteiros:", numeros_int)
except ValueError:
    print("Erro: certifique-se de que todos os elementos são números inteiros válidos.") """