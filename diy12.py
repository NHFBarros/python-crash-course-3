## 5.3 - 5.5
alien_color = 'green'

if alien_color == 'green':
    print("Você ganhou 5 pontos por abrir fogo contra um alienigena")
elif alien_color == 'yellow':
    print("Ganhou 10 pontos")
elif alien_color == 'red':
    print("Ganhou 15 pontos")
else:
    print("Você ganhou 10 pontos")

print('\n===============================================\n')

## 5.6

idade = 19

if idade < 2:
    print("Você é um neném rapaz")
elif idade >= 2 and idade < 4:
    print("Você é uma criança")
elif idade >=4 and idade < 13:
    print("Você é um(a) garoto(a)")
elif idade >= 13 and idade < 20:
    print("Você é um(a) adolescente")
elif idade >= 20 and idade < 65:
    print("Você é um(a) adulto(a)")
else:
    print("Você é um(a) idoso(a)")

print('\n===============================================\n')

frutasFavoritas = ['Banana', 'Maça', 'Manga']

if 'Banana' in frutasFavoritas:
    print("Você gosta mesmo de banana")
if 'Uva' in frutasFavoritas:
    print("Você gosta memso de Uva")
if 'Maça' in frutasFavoritas:
    print("Você gosta mesmo de maça")
if 'Amora' in frutasFavoritas:
    print("Você gosta mesmo de Amora")
if 'Manga' in frutasFavoritas:
    print("Você gosta mesmo de manga")