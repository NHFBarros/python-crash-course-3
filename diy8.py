for value in range(1,5):
    print(value) # <- 1, 2, 3, 4

numerosPares = list(range(2, 11, 2)) ## <- Wrapper
numerosImpares = list(range(1, 20, 2))

print(numerosPares)
print(numerosImpares)

print("\n=========================================\n")

square = []

for i in range(1, 11):
    square.append(i ** 2)

print(square)

print("\n=========================================\n")

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(f'Lista: {nums}')
print(f'O menor valor: {min(nums)}\nO maior valor: {max(nums)}\nSoma: {sum(nums)}')

print("\n=========================================\n")

valoresQuadrados = [value**2 for value in range(1,11)]
valoresPares = [value for value in range(2, 11, 2)]

print(valoresQuadrados)
print(valoresPares)

## 4.3
for i in range(1, 21):
    print(i, end=" ")

## 4.4
umMilhao = []
for i in range(1, 1_000_001):
    umMilhao.append(i)

#for valor in umMilhao:
#    print(f'   * {valor}')


## 4.5
print(f'\n\nMinimo: {min(umMilhao)}\nMaximo: {max(umMilhao)}\nSoma: {sum(umMilhao)}')

## 4.6

numerosImpares = list(range(1, 20, 2))
print (numerosImpares)

for i in range(len(numerosImpares)):
    print(numerosImpares[i], end=" ")


## 4.7
multiploTres = list(range(3, 31, 3))

for i in range(len(multiploTres)):
    print(multiploTres[i], end=" ")
print("") #quebrar a linha né pai


## 4.8 e 4.9
primeirosCubos = [value**3 for value in range(1, 11, 1)]

for i in range(len(primeirosCubos)):
    print(primeirosCubos[i], end=" ")