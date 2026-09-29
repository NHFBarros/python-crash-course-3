## Tupla

umMaisUmEhQuanto = (1, 1, 2) ## Isso é uma tupla

print(umMaisUmEhQuanto[2])

# umMaisUmEhQuanto[2] = 3 # <- da erro

## 4.13

refeicoes = ('Macarronada', 'Arroz com ovo', 'Pão com ovo', 'Pizza', 'Lasanha')

print("| ", end="")
for refeicao in refeicoes:
    print(refeicao, end=" | ")

# refeicoes[2] = 'Abacatada' # <- isso aí dá erro :(

refeicoes = ('Macarronada', 'Caviar', 'McMelt', 'Pizza', 'Lasanha')

print("\n\n| ", end='')
for refeicao in refeicoes:
    print(refeicao, end=" | ")