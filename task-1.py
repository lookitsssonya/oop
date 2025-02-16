class BeeElephant:
    def __init__(self, bee_part, elephant_part):
        self.bee_part = bee_part
        self.elephant_part = elephant_part

    def fly(self):
        return self.bee_part >= self.elephant_part

    def trumpet(self):
        if self.elephant_part >= self.bee_part:
            return "tu-tu-doo-doo!"
        else:
            return "wzzzzz"

    def eat(self, meal, value):
        if meal == "nectar":
            self.elephant_part -= value
            self.bee_part += value
        elif meal == "grass":
            self.bee_part -= value
            self.elephant_part += value

        self.bee_part = max(0, min(self.bee_part, 100))
        self.elephant_part = max(0, min(self.elephant_part, 100))

    def get_parts(self):
        return [self.bee_part, self.elephant_part]


bee_elephant = BeeElephant(50, 30)

print(bee_elephant.fly())

print(bee_elephant.trumpet())

bee_elephant.eat("nectar", 10)
print(bee_elephant.get_parts())  # [60, 20]

bee_elephant.eat("grass", 15)
print(bee_elephant.get_parts())  # [45, 35]