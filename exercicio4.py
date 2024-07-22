"""
Exercício 4 - DESAFIO: Calculadora Básica.

Dica:
operadores aritméticos +, -, * e / 
operador lógico ==
instrução if…elif…else 

- Escreva um programa que funcione como uma calculadora básica.
Ele deve pedir ao usuário dois números e uma operação ( + ,  - ,  * ,  / ).
Com base na operação escolhida, o programa deve executar a operação e exibir o resultado.
"""

var_numeral1 = int(input("Digite um número: "))
var_operador = (input("Digite um operador (+, -, *, /) "))
var_numeral2 = int(input("Digite um segundo número: "))
if var_operador == "+":
    print(f"A soma desses dois números é: {var_numeral1} + {var_numeral2} = {var_numeral1 + var_numeral2}")
elif var_operador == "-":
    print(f"A subtração desses dois números é: {var_numeral1} - {var_numeral2} = {var_numeral1 - var_numeral2}")
elif var_operador == "*":
    print(f"A Multiplição desses dois números é: {var_numeral1} * {var_numeral2} = {var_numeral1 * var_numeral2}")
elif var_operador == "/":
    if var_numeral2 != 0:
        print(f"A subtração desses dois números é: {var_numeral1} / {var_numeral2} = {var_numeral1 / var_numeral2:.2f} ")
    else:
        print("Inválido, você está tentando realizar uma divisão por ZERO")

else:
    print("Este cálculo é inválido")