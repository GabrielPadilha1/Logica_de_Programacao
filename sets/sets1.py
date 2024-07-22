"""
Exercício 3: Criando e Manipulando Conjuntos

Dicas:
Utilize a função set() para criar um conjunto.
A função len() retorna o tamanho do conjunto.
O método add() adiciona um elemento ao conjunto.
O operador in verifica se um elemento está presente no conjunto.
O método remove() remove um elemento do conjunto.
O operador | (união) retorna um novo conjunto com todos os 
elementos dos conjuntos originais, sem repetições.
O operador & (intersecção) retorna um novo conjunto com os 
elementos que estão presentes em ambos os conjuntos originais.
O operador - (diferença) retorna um novo conjunto com os 
elementos do primeiro conjunto que não estão presentes no 
segundo conjunto. 

- Crie um conjunto chamado letras contendo
as vogais do alfabeto: "a", "e", "i", "o", "u".
- Exiba na tela o tamanho do conjunto letras.
- Adicione a consoante "b" ao conjunto letras.
- Verifique se a vogal "i" está presente no conjunto letras.
- Remova a consoante "b" do conjunto letras.
- Crie um novo conjunto chamado consoantes contendo as 
consoantes: "b", "d", "f".
- Verifique se o conjunto consoantes está contido no conjunto letras.
- Exiba na tela a união dos conjuntos letras e consoantes 
(todos os elementos sem repetições).
"""

letras = {'a', 'e', 'i', 'o', 'u'}

print(f'O tamanho deste conjunto é {len(letras)}. ')

letras.add('b')

if 'i' in letras:
    print('A vogal "i" está presente neste conjunto. ')
else:
    print('A vogal "i" não está presente neste conjunto. ')

letras.remove('b')

consoantes = {'b', 'd', 'f',}

inter_con_vog = letras & consoantes
if inter_con_vog != set():
    print(f'O conjunto de consoantes está contida no conjunto "letras" {inter_con_vog} ')
else:
    inter_con_vog == set()
    print('O conjunto de consoantes não está contida no conjunto "letras"')

uniao_con_vog = letras.union(consoantes)
print(uniao_con_vog)