## DIcionarios

alien_0 = {'nome': 'Alien01', 'cor': 'verde'}
alien_0['posicaoX'] = 0
alien_0['posicaoY'] = 5

print(alien_0['nome'])
print(alien_0)

print("\n=========================================\n")
## 6.1
pessoa = {}

pessoa['nome'] = 'Maria'
pessoa['idade'] = 26
pessoa['Origem'] = 'Curitiba - PR'
pessoa['hobbie1'] = 'Cantar'
pessoa['hobbie2'] = 'Dançar'
#pessoa['pontos'] = 200

print(pessoa)
pessoa['nome'] = 'José'
print(f'O nome da pessoa agora é {pessoa['nome']}')

del pessoa['hobbie2']

print(pessoa)

pessoaPontos = pessoa.get('pontos', 0)

print(pessoaPontos)

## 6.2

numerosFavoritos = {
    'jean':1,
    'kalel':10,
    'mikesuel':8,
    'Wolverine':5
}

print("Número favorito de Jean:", numerosFavoritos['jean'])
print("Número favorito de Kalel:", numerosFavoritos['kalel'])
print("Número favorito do mikesuel bb", numerosFavoritos['mikesuel'])
print("Número favorito do Logan, Wolverine:", numerosFavoritos['Wolverine'])

## 6.3

dicionario = {
    'Array':'É uma lista em que os dados devem ser encaixados um ao lado do outro na memória',
    'lista':"É uma lista em que os dados podem ser encaixados em qualquer canto na memória",
    'dicionário':'Define valores para termos',
    'for':"repetição, para x em y vezes",
    'if':'caso se'
}

## aqui vai ser dicionarios. bacana :> Obs.: dicionarios não são que nem objetos. (Merge do git)

## alien_0 = {'color': 'green', 'points': 5}

## print(alien_0['color'])
## print(alien_0['points'])