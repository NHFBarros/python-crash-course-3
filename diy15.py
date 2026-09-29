user_0 = {
    'username':'NHFBarros',
    'first':'Nickolas',
    'last':'Henrique'
}

for k, v in user_0.items():
    print(f"\nKey: {k}")
    print(f"Value: {v}")

linguagensFavoritas = {
    'kalel':'java',
    'caio':'c++',
    'nickolas':'python',
    'riann':'javascript'
}

for k, v in linguagensFavoritas.items():
    print(f'linguagem favorita do {k.title()} é {v.title()}, mo otário kk')

for key in linguagensFavoritas.keys():
    print(key)

for value in linguagensFavoritas.values():
    print(value)

amigos = ['riann', 'kalel', 'maria', 'paulo']

for name in linguagensFavoritas.keys():
    print(f"Eae {name}")
    if name in amigos:
        linguagem = linguagensFavoritas[name]
        print(f"Tu é muito meu mano ja que gosta de {linguagem}")

## 6.4
dicionario = {
    'Array':'É uma lista em que os dados devem ser encaixados um ao lado do outro na memória',
    'lista':"É uma lista em que os dados podem ser encaixados em qualquer canto na memória",
    'dicionário':'Define valores para termos',
    'for':"repetição, para x em y vezes",
    'if':'caso se'
}

for k in dicionario.keys():
    print(f"\n{k.title()}: {dicionario[k]}")

## 6.5

rios = {
    'nilo':'egito',
    'amazonas':'brasil',
    'mississipi':'eua'
}

for k, v in rios.items():
    print(f"O {k.title()} corre através de {v.title()}")

## 6.6

linguagensFavoritas = {
    'kalel':'java',
    'caio':'c++',
    'nickolas':'python',
    'riann':'javascript'   
}

pessoas = ['kalel', 'caio', 'riann', 'maria', 'paulo']

for pessoa in pessoas:
    if pessoa in linguagensFavoritas.keys():
        print(f"Obrigado por participar da pesquisa {pessoa.title()}")
    else:
        print(f"Tu é muito meu mano {pessoa.title()} se inscreve na pesquisa ai")