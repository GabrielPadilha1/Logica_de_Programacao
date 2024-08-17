def hello(nome, idade):
    print(f"Olá {nome}! ")
    if int(idade) > 15:
        print("Você pode votar.")
    else:
        print("Você ainda não pode votar.")

hello("Fulano", 18)
hello("Sicrano", "14")
hello(idade="12", nome="Bertano")