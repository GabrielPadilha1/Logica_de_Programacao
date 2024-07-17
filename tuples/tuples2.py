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

frutas = ("banana", "maçã", "laranja")
legumes = ("tomate", "cenoura", "batata")
mercado = frutas + legumes

if "laranja" in mercado:
    print("Laranja está disponível")
else:
    print("Laranja não está disponível")

if "alface" in mercado:
    print("Alface está disponível")
else:
    print("Alface não está disponível")
print(mercado[-1])