class House:
    def __init__(self, name, numbers_of_floors):
        self.name = name
        self.numbers_of_floors = numbers_of_floors

    def go_to(self, new_floor):
        floor_ = 0
        self.new_floor = new_floor

        if self.new_floor > self.numbers_of_floors or self.new_floor < 1:
                print("Такого этажа не существует")
        else:
            for floor_ in range(new_floor):
                print(floor_ + 1)

    def __len__(self):
        return self.numbers_of_floors

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.numbers_of_floors}'

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
