aplicativos = ['Youtube', 'Google', 'Facebook', 'Twitter', 'Instagram', 'HQ Mania', 'CNH Brasil', 'Setting', 'Camera']

print('\n===================================================\n')

for aplicativo in aplicativos:
    print(f"Errou meu {aplicativo.upper()}")
    print(f'pela primeira vez na sua vida cê errou meu {aplicativo.lower()}')

print('\n===================================================\n')

for i in range (len(aplicativos)):
    print(f'{aplicativos[i].upper()} é uma bosta, com todo respeito')

    if i < (len(aplicativos)-1):
        print(f'Nesse caso, vamos analisar o {aplicativos[i+1].lower()}, será que ele é melhor?\n')
    else:
        print('\nNenhum presta mesmo...')

print('\n===================================================\n')

## 4.1 Pizzas

pizzas = ['Calabresa', 'Frango', 'Marguerita', 'Carne de sol']

print("Pizzas que eu gosto:")
for pizza in pizzas:
    print('   *', pizza)

print('\nPizza é muito bom, realmente')


print('\n===================================================\n')

## 4.2 Animais

animais = ['Cachorro', 'Gato', 'Passáro', 'Tartaruga', 'Hamster', 'Furão', 'Peixe']

print('Animais Domesticos:')
for animal in animais:
    print('   *', animal)
print('\nApoio sim você ter um desses animais em casa')

print('\n===================================================\n')