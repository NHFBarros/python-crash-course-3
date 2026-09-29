## criando lista
foiOQue = ["Uisque", "Vodka", "Cerveja", "Lolo", "Cigarro", "Pó", "Viado Enxerido"]
print(foiOQue) ## Lista inteira
print(foiOQue[0]) ## Primeiro elemento
print(foiOQue[-1]) ## Ultimo elemento
print(f"Teve {foiOQue[0].title()}, {foiOQue[1]}, {foiOQue[2]}, {foiOQue[3]}, uma carteira de {foiOQue[4]}, duas carreiras de {foiOQue[5]} ")

## 3.1
amigos = ['Kalel', 'GF', 'Caio', 'Luan']
print(amigos[0])
print(amigos[1])
print(amigos[2])
print(amigos[3])

## 3.2 (vou tryhardar um pouco aqui)
for i in range(4): 
    print(f"fala mano {amigos[i]}, como vai?")

## 3.3 (esse eu não entendi muito bem...)
transporte = ["factor 150", "Gol bolinha", "Gol quadrado"]
print(f"Atualmente tenho uma {transporte[0]}")
print(f"queria comprar um {transporte[2]}")
print(f"mas o {transporte[1]} também é legal")