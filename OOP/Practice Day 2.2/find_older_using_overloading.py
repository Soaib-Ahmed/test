class Cricketer(Person):
    def __init__(self, name, age, height, weight):
        super().__init__(name, age, height, weight)

    def __lt__(self, other):
        return self.age < other.age

shakib = Cricketer('Sakib', 38, 68, 91)
musfiq = Cricketer('Rahim', 36, 68, 88)
kamal = Cricketer('Kamal', 39, 68, 94)
jack = Cricketer('Jack', 38, 68, 91)
kalam = Cricketer('Kalam', 37, 68, 95)

oldest_player = max([shakib, musfiq, kamal, jack, kalam])
print(oldest_player.name)  # Output: 'Kamal'