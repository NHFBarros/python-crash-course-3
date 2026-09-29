## 2.3
first_name = "nickolas"
last_name = "henrique"
full_name = f"{first_name} {last_name}"

print(f"olá {first_name}, gostaria de aprender a fazer o sabor?")

## 2.4
print(f"Nome minusculo: {first_name.lower()}\nNome maiusculo: {first_name.upper()}\nPrimeiras letras maiusculas: {first_name.title()}")

## 2.5 & 2.6
famous_person = "Albert Einsten"
message = "Uma pessoa que nunca cometeu um erro nunca tentou nada de novo"

print(f'{famous_person.title()} disse uma vez: "{message}".')

## 2.7
first_name = " nickolas "
print(f"Nome com rstrip: {first_name.rstrip()}a\nNome com lstrip: {first_name.lstrip()}a\nNome com strip: {first_name.strip()}a\n\t coloquei um 'a' na frente pra ver o espaçamento")

## 2.8

filename = "python_notes.txt"
print(filename.removesuffix(".txt"))

