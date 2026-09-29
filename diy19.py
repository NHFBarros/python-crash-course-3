# usuariosNaoConfirmados = ['alice', 'brian', 'candace']
# usuariosConfirmados = []

# while usuariosNaoConfirmados:
#     usuarioAtual = usuariosNaoConfirmados.pop()
#     print(f"verificando usuário {usuarioAtual}")
#     usuariosConfirmados.append(usuarioAtual.title())

# for usuario in usuariosConfirmados:
#     print(usuario)

# pets = ['gato', 'hamster', 'cachorro', 'hamster', 'peixe', 'hamster', 'coelho']

# print(pets)

# while 'hamster' in pets:
#     pets.remove('hamster')

# print(pets)


# respostas = {}

# while True:
#     nome = input('Qual seu nome? ')
#     resposta = input('Linguagem favorita? ')

#     respostas[nome] = resposta

#     env = input('Deseja continuar?')
#     if env == 'não':
#         break

# print(respostas)

## 7.8 e 7.9

# ordemSanduiche = ['pastrami', 'x1', 'x2', 'pastrami', 'x3', 'pastrami']
# sanduichePronto = []

# print("O pastrami acabou, então vamos remover ele da lista de pedidos")
# while 'pastrami' in ordemSanduiche:
#     ordemSanduiche.remove('pastrami')

# while ordemSanduiche:
#     sanduiche = ordemSanduiche.pop()
#     print(f'{sanduiche} novo na ordem')
#     sanduichePronto.insert(0, sanduiche)

# print(sanduichePronto)

respostas = {}

prompt = "Se você tivesse as férias dos sonhos, onde seria? "

while True:
    nome = input("Qual o seu nome? ")
    resposta = input(prompt)

    respostas[nome] = resposta

    x = input("Deseja adicionar outra resposta?")
    if x == 'não':
        break

print("Resultado da pesquisa:")
for k, v in respostas.items():
    print(f"{k} disse que seria em {v}")

## Acima terminamos o capitulo 7. O proximo é cap 8, funções