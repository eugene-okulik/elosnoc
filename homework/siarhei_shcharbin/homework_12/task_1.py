class Flower:
    def __init__(self, name, color, freshness, stem_length, lifetime, price):
        self.name = name
        self.color = color
        self.freshness = freshness
        self.stem_length = stem_length
        self.lifetime = lifetime
        self.price = price


class Rose(Flower):
    def __init__(self, color, freshness, stem_length, lifetime, price, count):
        super().__init__('Roses', color, freshness, stem_length, lifetime, price)
        self.count = count
        self.data = self.name, color, freshness, stem_length, lifetime, price

    def __str__(self):
        return f'{self.data}'

    def __repr__(self):
        return f'{self.data}'


class Peony(Flower):
    def __init__(self, color, freshness, stem_length, lifetime, price, count):
        super().__init__('Peonies', color, freshness, stem_length, lifetime, price)
        self.count = count
        self.data = self.name, color, freshness, stem_length, lifetime, price

    def __str__(self):
        return f'{self.data}'

    def __repr__(self):
        return f'{self.data}'


class Tulip(Flower):
    def __init__(self, color, freshness, stem_length, lifetime, price, count):
        super().__init__('Tulips', color, freshness, stem_length, lifetime, price)
        self.count = count
        self.data = self.name, color, freshness, stem_length, lifetime, price

    def __str__(self):
        return f'{self.data}'

    def __repr__(self):
        return f'{self.data}'


class Sunflower(Flower):
    def __init__(self, color, freshness, stem_length, lifetime, price, count):
        super().__init__('Sunflowers', color, freshness, stem_length, lifetime, price)
        self.count = count
        self.data = self.name, color, freshness, stem_length, lifetime, price

    def __str__(self):
        return f'{self.data}'

    def __repr__(self):
        return f'{self.data}'


class Bouquet:
    def __init__(self, flowers=None):
        if flowers is None:
            self.flowers = []
            print('The bouquet has no flowers yet')
        else:
            self.flowers = flowers
            flowers_name = [flower.name for flower in self.flowers]
            print(f"{','.join(flowers_name)} have been added to the bouquet")

    def add_flowers(self, flower):
        self.flowers.append(flower)
        print('Flower(s) has been added to the bouquet')

    def total_cost(self):
        if not self.flowers:
            tot_cost = 0
        else:
            tot_cost = sum(flower.price * flower.count for flower in self.flowers)
        return f'Bouquet total cost is {tot_cost} euros'

    def average_lifetime(self):
        if not self.flowers:
            avg_lifetime = 0
        else:
            avg_lifetime = sum(flower.lifetime for flower in self.flowers) / len(self.flowers)
        return f'Bouquet average lifetime is {avg_lifetime} days'

    def sort_flowers(self, attribute):
        try:
            sorted_flowers = sorted(self.flowers, key=lambda flower: getattr(flower, attribute))
            return sorted_flowers
        except AttributeError:
            print(f"Flowers in the bouquet have no attribute'{attribute}'")
            return None

    def find_flowers(self, **kwargs):
        result = self.flowers
        try:
            for attr, value in kwargs.items():
                result = [flower for flower in result if getattr(flower, attr) == value]
            return result
        except AttributeError:
            print(f"Couldn't find attribute '{attr}'")
            return None


rose = Rose('red', 'nice', 40, 3, 15, 5)
tulip = Tulip('white', 'medium', 25, 4, 10, 3)
peony = Peony('white', 'nice', 35, 4, 20, 3)
sunflower = Sunflower('yellow', 'bad', 50, 1, 10, 1)
print(rose)
bouquet = Bouquet([rose, tulip])
print(bouquet.total_cost())
bouquet.add_flowers(peony)
bouquet.add_flowers(sunflower)
print(bouquet.total_cost())
new_bouquet = Bouquet()
print(new_bouquet.average_lifetime())
print(new_bouquet.total_cost())
print(bouquet.average_lifetime())
print(bouquet.sort_flowers('freshness'))
print(bouquet.find_flowers(freshness='noce'))
