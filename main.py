# Conteúdo 

# Métodos e operações #
""" 
1. Inteiros (int)

    • Métodos e operações:

        + (adição)
        - (subtração)
        * (multiplicação)
        // (divisão inteira)
        % (módulo - resto da divisão)

2. Números de Ponto Flutuante (float)

    •Métodos e operações:
        + (adição)
        - (subtração)
        * (multiplicação)
        / (divisão)
        ** (potenciação)

3. Strings (str)

    • Métodos e operações:
        .upper() (converte para maiúsculas)
        .lower() (converte para minúsculas)
        .strip() (remove espaços em branco no início e no final)
        .split(sep) (divide a string em uma lista, utilizando sep como delimitador)
        + (concatenação de strings)

4. Booleanos (bool)
    
    • Operações lógicas:
        and (E lógico)
        or (OU lógico)
        not (NÃO lógico)
        == (igualdade)
        != (diferença) 
"""

# try-except e if #

# This way the script is susceptible to errors
""" number_1 = float(input("Enter number 1: "))
number_2 = float(input("Enter number 2: "))

result = number_1 / number_2

print(result) """

# This way the script has error handling 
""" try: 
    number_1 = float(input("Enter number 1: "))
    number_2 = float(input("Enter number 2: "))

    result = number_1 / number_2

    print(result)
except:
    print("Result of division is a indetermination.") """

# This way the script has error handling with python error
""" try: 
    number_1 = float(input("Enter number 1: "))
    number_2 = float(input("Enter number 2: "))

    result = number_1 / number_2

    print(result)
except ZeroDivisionError:
    print("Error: Result of division is a indetermination.")
except KeyboardInterrupt:
    print("\nError: There was interruption in program.") """

# TypeError #

# len() is not function to count numbers
""" len(3) """

""" try:
    result = len(3)
    print(result)
except TypeError as e:
    print(e) # print a error message """

# usin try-except with else
""" try:
    result = len("Jadeson")
    print(result)
except TypeError as e:
    print(e) # print a error message
else:
    print("Tudo ocorreu bem.") # if it works, do it """

# usin try-except with else and finnaly
""" try:
    result = len("Jadeson")
    print(result)
except TypeError as e:
    print(e) # print a error message
else:
    print("Eveything is fine!") # if it works, do it
finally:
    print("The important is to participe.") # executes line of code, regardless of error """


# Type Check #

# usin isistance
""" number = int(input("Enter a number: "))

if isinstance(number, int):
    print("The variable is a integer.")
else:
    print("The variable is not a integer.") """

# anothe way
""" value = input("Enter a value: ")

try:
    number = float(value)
    if isinstance(number, float):
        print("The variable is a number.")
except ValueError:
    print("The variable is not a number.") """

# using if
age = 20
if age < 18:
    print("Under 18 years old")
elif age == 18:
    print("Exactly 18 years")
else:
    print("Over 18 years old")










