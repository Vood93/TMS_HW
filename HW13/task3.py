class Pizza:
    def __init__(self, size, cheese, pepperoni, mushrooms, onions, bacon):
        self.size = size
        self.cheese = cheese
        self.pepperoni = pepperoni
        self.mushrooms = mushrooms
        self.onions = onions
        self.bacon = bacon

    def __str__(self):
        return f"Pizza(size={self.size}, cheese={self.cheese}, pepperoni={self.pepperoni}, mushrooms={self.mushrooms}, onions={self.onions}, bacon={self.bacon})"


class PizzaBuilder:
    def __init__(self):
        self.reset()

    def reset(self):
        self._pizza = Pizza("", False, False, False, False, False)
        return self

    def set_size(self, size):
        self._pizza.size = size
        return self

    def add_cheese(self):
        self._pizza.cheese = True
        return self

    def add_pepperoni(self):
        self._pizza.pepperoni = True
        return self

    def add_mushrooms(self):
        self._pizza.mushrooms = True
        return self

    def add_onions(self):
        self._pizza.onions = True
        return self

    def add_bacon(self):
        self._pizza.bacon = True
        return self

    def pizza(self):
        pizza = self._pizza
        self.reset()
        return pizza


class PizzaDirector:
    def __init__(self, builder):
        self._builder = builder

    def make_vegetarian_pizza(self):
        self._builder.reset().set_size(
            "large"
        ).add_cheese().add_mushrooms().add_onions()
        return self._builder.pizza()

    def make_meat_lovers_pizza(self):
        self._builder.reset().set_size(
            "medium"
        ).add_cheese().add_pepperoni().add_bacon()
        return self._builder.pizza()


builder = PizzaBuilder()
director = PizzaDirector(builder)

pizza = director.make_vegetarian_pizza()
print(pizza)
