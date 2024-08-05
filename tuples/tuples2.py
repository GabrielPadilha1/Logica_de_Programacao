"""
Exercício 2: Combinando Tuplas e Verificando Elementos

Dicas:
O operador + pode ser utilizado para concatenar tuplas.
Para verificar se um elemento existe em uma tupla, utilize 
o operador in.
O índice de um elemento em uma tupla pode ser obtido 
utilizando o método index().


- Crie duas tuplas: frutas contendo ("banana", "maçã", "laranja")
e legumes contendo ("tomate", "cenoura", "batata").
- Crie uma nova tupla chamada mercado que combine as tuplas
frutas e legumes.
- Verifique se a fruta "laranja" está presente na tupla 
mercado.
- Verifique se o legume "alface" está presente na tupla 
mercado.
- Exiba na tela o último item da tupla mercado.
"""

frutas = ("Banana", "Maçã", "Laranja")
legumes = ("Tomate", "Cenoura", "Batata")
mercado = frutas + legumes

if "Laranja" in mercado:
    print("Laranja está disponível.")
else:
    print("Laranja não está disponível.")

if "Alface" in mercado:
    print("Alface está disponível.")
else:
    print("Alface não está disponível.")
print(f"O último item da lista de compras é: {mercado[-1]}")