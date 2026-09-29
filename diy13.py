## Numero do capeta o desse diy aqui :>
disponiveisIngredientes = ['queijo', 'molho de tomate', 'calabresa', 'bacon', 'ervilha', 'milho', 'azeitona']
solicitacaoIngrediente = ['queijo', 'azeitona', 'abacaxi']

if solicitacaoIngrediente:
    print("\nComeçando a preparação da pizza!!!!!")
    for solicitacao in solicitacaoIngrediente:
        if solicitacao in disponiveisIngredientes:
            print(f"   * {solicitacao} adicionado")
        else:
            print("   ! Ficar devendo", solicitacao,"pai")
    print("Finalizado pai\n")
else:
    print("Como? se eu to no play 4")

print('\n===============================================\n')

## 5.8 e 5.9
nomes = ['Sabor adm', 'admin', 'kalelzin de cria', 'GF', 'Caio cesar...']

if nomes:
    for nome in nomes:
        if nome == 'admin':
            print("Eita adm, tu pode ver relatório, viu?")
        else:
            print("Eae chefe, como que ce ta adm?", nome)
else:
    print("Nem tem usuário man")

print('\n===============================================\n')

## 5.10
usuariosAtuais = ['Nickolas', 'Kalel', 'Caio', 'GF', 'Luan']

usuariosAtuaisLower = [value.lower() for value in usuariosAtuais]

usuariosNovos = ['Luan', 'kAlel', 'Kaito', 'Ray', 'Anorak']

for usuario in usuariosNovos:
    if usuario.lower() in usuariosAtuaisLower:
        print(f'{usuario} vai ter que usar outro nome ô, esse ai já tão usano...')
    else:
        print(f'{usuario}, Liberado pai')

## 5.11
nums = list(range(1, 10, 1))

for num in nums:
    if num == 1:
        print(f'{num}st', end=' ')
    elif num == 2:
        print(f'{num}nd', end=" ")
    elif num == 3:
        print(f'{num}rd', end=' ')
    else:
        print(f'{num}th', end=' ')
print('\n')

## esse foi legal pq eu usei listas formadas por for para definir os itens e a função list. bacana