## esse abaixo que sao meus testes é basicamente o 3.10

## Metodo sort
carros = ['BYD', 'BMW', 'Audi', 'Toyota', 'Subaru', 'Honda', 'Fiat', 'Renault', 'Yamaha']
nums = [5, 4, 3, 2, 6, 4, 3, 9, 12, 421, 321, 523]

## carros.sort(reverse=true) ## <- transforma a lista em sort. reverse true pra ficar ordem inversa



print(sorted(carros)) #aqui é só pra monstrar sorteada já (ordem alfabetica)

## carros.reverse() ## <- reverte definitivamente
print(carros)

print(len(carros)) # <- quantidade de registros na lista

print(sorted(nums, reverse=True)) # <- Lista de numeros em ordem decrescente

print("\n=========================================================\n")

## 3.8
lugares = ['EUA', 'Canadá', 'México', 'Chile', 'Paraguai', 'Uruguai', 'França', 'Noruega', 'Italia']
print('Lista de lugares que eu gostaria de ir: ', lugares)
print('Lista em ordem alfabética:', sorted(lugares))
print('A lista continua normal, se liga:', lugares)
print('Lista reversa:', sorted(lugares, reverse=True))
print('Lista continua normal:', lugares)

lugares.reverse()

print('Ordem alterada:', lugares)

lugares.reverse()

print('Voltou ao normal kk:', lugares)

lugares.sort
print('Lista sortada:', lugares)

lugares.sort(reverse=True)
print('Lista sortada reversaaa:', lugares)

print("\n=========================================================\n")

## Exercicio 3.9 vou ter que só fazer basicamente um len(lista), então não vou fazer tudo que pede aí
pessoasJantar = ['Bolsonaro(jair)', 'Lula', 'marçal', 'tabata', 'renan']

print("Estou convidando", len(pessoasJantar), "pessoas para o jantar, ta ok?")

print("\n=========================================================\n")

## 3.10