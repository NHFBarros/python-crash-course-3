## Fatiando listas
nomes = ['Maikesuel', 'Mickaele', 'Nickolas', 'Nickole', "Papai", 'Mamãe']

print(f"Os mio: {nomes[4:]}")
print(f"Os pio: {nomes[:4]}")
print(f"Os fi: {nomes[1:4]}")
print(f"Os ultimos 2: {nomes[-2:]}")
print(f"os primeiros 2: {nomes[:2]}")

print(f"\nEsses são os primeiros 2 membros da lista:")
for membro in nomes[:2]:
    print(membro.upper())

nomes2 = nomes[:] ## se usar "nomes2 = nomes" vai gerar um registro em ambas a listas se adicionar um append em apenas uma
nomes.append("vovô")
nomes2.append("Vovó")
print(nomes)
print(nomes2)

## 4.10
pizzas = ['Calabresa', 'Frango', 'Catubresa', 'Carne de sol', 'Marguerita', 'Lombo']

print("Os três primeiros elementos da lista são:", pizzas[:3])
print("Os três que ficam no meio são:", pizzas[2:5])
print("Os três ultimos:", pizzas[-3:])

amigosPizzas = pizzas[:]
pizzas.append('Broccolis')
amigosPizzas.append('Abacaxi')

print("Minhas pizzas favoritas:")
for pizza in pizzas:
    print(pizza, end=" ")

print("\n\nPizza favorita do meu amigo:")
for pizza in amigosPizzas:
    print(pizza, end=" ")

## 4.12 não entendi esse, mas é só fazer uns for numas lista aí, coisa que faco acho desde do diy3.