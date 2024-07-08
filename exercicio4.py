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