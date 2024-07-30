"""
Exercícios com dicionários

Exercício 5: Criando e Acessando Elementos de um Dicionário

Dicas:
Utilize a função dict() para criar um dicionário.
Para acessar um valor específico no dicionário, utilize a chave entre colchetes [].
Para adicionar um novo par chave-valor, utilize a atribuição dentro dos colchetes.
Para iterar sobre as chaves de um dicionário, utilize o loop for.
Para iterar sobre os pares chave-valor de um dicionário, utilize o loop for com a função items().


- Crie um dicionário chamado agenda para armazenar informações de contato de seus amigos:
- Chave: nome do amigo (string)
- Valor: dicionário com informações de contato (telefone, email)
- Adicione 3 amigos à sua agenda, cada um com nome, telefone e email.
- Exiba na tela o telefone do primeiro amigo da agenda.
- Modifique o email do segundo amigo para um novo endereço.
- Adicione uma nova chave "cidade" ao dicionário de informações do terceiro amigo,
com o valor correspondente à sua cidade natal.
- Exiba na tela todas as chaves e valores do dicionário do terceiro amigo.
"""
agenda = {
    'Marcos': {
        'telefone': '1234-5678',
        'email': 'marcos123@gmail.com'
    },
    'Mateus': {
        'telefone': '8765-4321',
        'email': 'mateus321@gmail.com'
    },
    'Mathias': {
        'telefone': '2468-1357',
        'email': 'mathias234@gmail.com'
    }
}
amigo1 = list(agenda.keys())[0]
tel_amigo1 = agenda[amigo1]['telefone'] 
print(f'Telefone do seu primeiro amigo: {tel_amigo1} ({amigo1}) ')

amigo2 = list(agenda.keys())[1]
agenda[amigo2].update({'email': 'novomateus@gmail.com'})

amigo3 = list(agenda.keys())[2]
agenda[amigo3].update({"cidade": "Barcelona"})
x = agenda[amigo3].items() 
print(f'Informações do terceiro amigo {amigo3}: {dict(x)}')
