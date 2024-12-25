class House:
    def __init__(self, house_name, floors_count):
        self.house_name = house_name
        self.floors_count = floors_count

    def __str__(self):
        return f"Название: {self.house_name}, кол-во этажей: {self.floors_count}"

    def __len__(self):
        return self.floors_count

    def __eq__(self, other):
        if isinstance(other, House):
            return self.floors_count == other.floors_count
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, House):
            return self.floors_count < other.floors_count
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, House):
            return self.floors_count <= other.floors_count
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, House):
            return self.floors_count > other.floors_count
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, House):
            return self.floors_count >= other.floors_count
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, House):
            return self.floors_count != other.floors_count
        return NotImplemented

    def __add__(self, value):
        if isinstance(value, int):
            self.floors_count += value
            return self
        elif isinstance(value, House):
            self.floors_count += value.floors_count
            return self
        return NotImplemented

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

    def go_to_floor(self, new_floor):
        if new_floor < 1 or new_floor > self.floors_count:
            print("Такого этажа не существует")
        else:
            for floor in range(1, new_floor + 1):
                print(floor)

house_1 = House('ЖК Эльбрус', 10)
house_2 = House('ЖК Акация', 20)

print(house_1)
print(house_2)

print(house_1 == house_2)

house_1 = house_1 + 10
print(house_1)
print(house_1 == house_2)

house_1 += 10
print(house_1)

house_2 = 10 + house_2
print(house_2)

print(house_1 > house_2)
print(house_1 >= house_2)
print(house_1 < house_2)
print(house_1 <= house_2)
print(house_1 != house_2)
