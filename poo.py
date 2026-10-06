# ## Mini estudo de POO em python

# class Dog:
#     #Simples tentativa de modelar um cachorro

#     def __init__(self, name, age):
#         #Inicializa os atributos de nome e idade
#         self.name = name
#         self.age = age

#     def sit(self):
#         #Simula um chachorro sentado em resposta a um comando
#         print(f"{self.name} agora está sentado")

#     def roll_over(self):
#         #Simula um cachorro rolantdo em resposta a um comando
#         print(f"{self.name} rolou!")

# meu_cachorro = Dog('Maikesuel', 6)

# print(f'O nome do meu cachorro é {meu_cachorro.name}')
# print(f'{meu_cachorro.sit()}')
''''''

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"Esse carro tem {self.odometer_reading} quilometros rodados")

    def update_odometer(self, km):
        if km >= self.odometer_reading:
            self.odometer_reading = km
        else:
            print("Você não pode voltar a quilometragem")

    def increase_odometer(self, km):
        self.odometer_reading += km

class eletricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

meu_byd = eletricCar('BYD', 'Dolphin', 2024)
print(meu_byd.get_descriptive_name)