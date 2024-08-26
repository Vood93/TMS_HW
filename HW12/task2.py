class Beelephant:
    def __init__(self, bee_value, elephant_value):
        self.bee_value = bee_value
        self.elephant_value = elephant_value

    def fly(self):
        return self.bee_value >= self.elephant_value

    def trumpet(self):
        if self.elephant_value >= self.bee_value:
            return "tu-tu-doo-doo"
        else:
            return "wzzzz"

    def eat(self, meal, value):
        if meal == "nectar":
            self.elephant_value = max(0, self.elephant_value - value)
            self.bee_value = min(100, self.bee_value + value)
        elif meal == "grass":
            self.elephant_value = min(100, self.elephant_value - value)
            self.bee_value = max(0, self.bee_value + value)
        else:
            raise ValueError("Incorrect value")


beelephant = Beelephant(40, 60)

print(beelephant.fly())
print(beelephant.trumpet())
beelephant.eat("nectar", 20)
print(beelephant.bee_value, beelephant.elephant_value)
