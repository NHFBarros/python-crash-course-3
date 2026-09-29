## Modificando elementos em uma lista
frutas = ["maçã", "banana", "pera", "uva", "abóbora", "melancia", "abacaxi"]

frutas[4] = "manga"

print(frutas)


## Adicionar elementos no final da lista

frutas.append("ameixa")

print(frutas)


## Adicionar em qualquer canto (pode ser no meio)

frutas.insert(3, "tomate")

print (frutas)


## Remover um elemento sabendo a posição do prezado

del frutas[3]

print(frutas)


## remover um elemento da lista, mas ainda assim poder trabalhar com ele

melhorFruta = frutas.pop(5) ## <- se deixar o pop vazio ele pega o ultimo elemento

print(melhorFruta, frutas)


## removendo por valor

piorFruta = "pera"

frutas.remove(piorFruta) ## O remove só tira 1 vez o nome, se tiver varias peras na lista, ele só tira a primeira que aparecer no indice :(

print(frutas)

############################## Testes Acima #############################
print("===============================================================================\n")
## 3.4 (aqui vou dar uma tryhardada)

pessoasJantar = ['Bolsonaro(jair)', 'Lula', 'marçal', 'tabata', 'renan']

for i in range(len(pessoasJantar)):
    print(f'prezado {pessoasJantar[i]}, você é meu convidado de honra para participar do melhor jantar de todos os tempos.')

print(f'acabo de receber a informação que o prezado {pessoasJantar[1]} não vai poder ir :(. Convidamos no lugar Alexandre de Moraes')

pessoasJantar[1] = "Alexandre de moraes"
print(f'prezado {pessoasJantar[1]}, você é meu convidado de honra para participar do melhor jantar de todos os tempos.')

print("PREZADOS!!! ACHEI UMA MESA MAIOR!!!. Se liga no convite novamente ai pra mais gente")

pessoasJantar.insert(0, "Lula")
pessoasJantar.insert(3, "Jones Manoel")
pessoasJantar.append("Kim kataguiri")


for i in range(len(pessoasJantar)):
    print(f'prezado {pessoasJantar[i]}, você é meu convidado de honra para participar do melhor jantar de todos os tempos.')

print("era fake news do pt glr :(. Vai vir só 2 pessoas tbm, fiquei de mal")

for i in range(len(pessoasJantar)-2):
    print(f'Prezado {pessoasJantar[0]}, graças a teu presidente aí vai render mais não to tirando teu convite junto com geral')
    pessoasJantar.pop(0)

for i in range(len(pessoasJantar)):
    print(f"Ei {pessoasJantar[i]}, você ainda está convidado viu")

del pessoasJantar[0]
del pessoasJantar[0]

print (pessoasJantar)