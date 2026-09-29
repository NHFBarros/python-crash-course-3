carros = ['fiat', 'Wolksvagen', 'honda', 'toyata', 'hyundai', 'bmw', 'ferrari', 'porche', 'byd', 'tesla', 'nissan', 'volvo', 'chevrolet', 'ford']
carroEspecifico = "fiat"


for carro in carros:
    if carro == "chevrolet":
        print("    *", carro.upper())
    else:
        print("    *", carro.lower())

print("\n==================================================================================\n")

resposta = 13

if resposta != 14:
    print("Votou errado pai")
else:
    print("Dei valor")

if "aa" not in carros and "fiat" in carros:
    print("tem lá viu")
else:
    print("Tem não :(")

print("\n==================================================================================\n")

## 5.1
print('Tu tem carroEspecifico == "fiat"? eu chuto que sim')
print(carroEspecifico == 'fiat', '\n')

print('E carroEspecifico == "ferrari"? Aposto tudo que vai dar false')
print(carroEspecifico == 'ferrari', '\n')

## 5.2 eu já faço faz uns 20 anos, faz o L