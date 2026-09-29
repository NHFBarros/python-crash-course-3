# # Um conjunto (set) é uma coleção de elementos únicos, sem itens repetidos.
# frutas = {"maçã", "banana", "laranja", "uva", "maçã"}

# itensUnicos = {
#     "martelo": 2,
#     "chave de fenda": 1,
#     "alicate": 1,
#     "fita métrica": 1,
#     "furadeira": 1,
#     "martelo": 2
# }  # Dicionário para armazenar os itens únicos e suas quantidades

# print("ferramentas")
# for ferramenta in itensUnicos:  # Usando set() para garantir que os itens sejam únicos
#     print(ferramenta)

# for fruta in frutas:
#     print(fruta)

# alien_0 = {'nome': 'Alien01', 'cor': 'verde'}
# alien_1 = {'nome': 'Alien02', 'cor': 'vermelho'}
# alien_2 = {'nome': 'Alien03', 'cor': 'azul'}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)

# pessoas = []

# for i in range(30):
#     nova_pessoa = {'id': i, 'nome': f'Pessoa{i}', 'idade': 20 + i}
#     pessoas.append(nova_pessoa)

# for pessoa in pessoas[:5]:
#     print(pessoa)

# print(len(pessoas))

## 6.7
people1 = {'name': 'Kalel', 'age': 25, 'city': 'Curitiba'}
people2 = {'name': 'Caio', 'age': 30, 'city': 'São Paulo'}
people3 = {'name': 'Nickolas', 'age': 28, 'city': 'Rio de Janeiro'}

people = [people1, people2, people3]

for person in people:
    print(f"Nome: {person['name']}, Idade: {person['age']}, Cidade: {person['city']}")

cachorro = {
    'nome': 'Rex',
    'raca': 'Labrador',
    'idade': 3,
    'cor': 'preto',
    'dono': 'João'
}

gato = {
    'nome': 'Mia',
    'raca': 'Siamês',
    'idade': 2,
    'cor': 'cinza',
    'dono': 'Maria'
}

hamster = {
    'nome': 'Bola',
    'raca': 'Sírio',
    'idade': 1,
    'cor': 'branco',
    'dono': 'Pedro'
}

pets = [cachorro, gato, hamster]

for pet in pets:
    print(f"Nome: {pet['nome']}, Raça: {pet['raca']}, Idade: {pet['idade']}, Cor: {pet['cor']}, Dono: {pet['dono']}")


lugaresFavoritos = {
    'joao':'fortaleza',
    'kalel':'curitiba',
    'caio':'porto alegre'
}

for k, v in lugaresFavoritos.items():
    print(f"O {k} gosta de {v}")

numFavorito = {
    'joao':[1, 2, 3],
    'kalel':[4, 3, 2],
    'davi':[4, 13, 14],
    'viniccius':[13]   
}

for pessoa, nums in numFavorito.items():
    numeros = "";
    for num in nums:
        numeros = numeros + f'{num}, '
    print(f"Os numeros favoritos do {pessoa} é {numeros.removesuffix(", ")}")

    