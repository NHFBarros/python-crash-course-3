## 2.1

message = "sabor"

print("isso é", message, "mensagem")

## 2.2 (Aproveitand0o o 2.1)

message = "não sabor"

print("Na verdade isso é", message, "mensagem")

## Caso string com ' e "

saborString = "s'a'b'o'r"
saborString2 = 'é nois, ok "beleza" '

print(saborString)
print(saborString2)

##.title
nome = "nickolas henrique"

print(nome.title()) ## = Nickolas Henrique
print(nome.upper()) ## = NICKOLAS HENRIQUE
print(nome.lower()) ## = nickolas henrique

first_name = "nickolas"
last_name = "henrique"

full_name = f"{first_name} {last_name}"

print(full_name) ## nickolas henrique

## \n quebra linhas e \t da um espaçamento:

print("coisas que eu gosto: \n\to meme do sabor\n\tkalel\n\tbatman\n\tpadaria\n\thomem aranha\nfim da lista\tsabor lista*")

## rstrip lstrip strip

espaco = " melk "

print(espaco.rstrip()) ## = " melk"
print(espaco.lstrip()) ## = "melk "
print(espaco.strip()) ## = "melk"

## removendo prefixo

site = "https://sabor.com"

print(site.removeprefix("https://")) ## = sabor.com