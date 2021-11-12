class Animal:
    """A class used to represent an animal"""

    """name of the zoo that apply to all animals:"""
    zoo_name = "HayThon"

    def __init__(self, _name, _hunger=0):
        """
        every animal in the zoo has a name and hunger level.
        :param name: animal's name
        :param hunger: hunger level. default hunger level is 0.
        :type name: str
        :type hunger: int
        """
        self._name = _name
        self._hunger = _hunger

    def get_name(self):
        """
        gets the animal's name
        :return: animal's name
        :rtype: str
        """
        return self._name

    def is_hungry(self):
        """
        checks if the animal is hungry
        :return: True/False
        :rtype: bool
        """
        return bool(self._hunger)

    def feed(self):
        """
        feeds the animal - reduces 1 from the hunger level
        :return: none
        """
        self._hunger -= 1

    def talk(self):
        """makes animal talk"""
        pass


class Dog(Animal):
    """A class used to represent a dog which is a kind of an animal in the zoo"""
    def talk(self):
        """
        overrides the "talk" method of superclass Animal, so Dog has it's unique talk
        :return: none
        """
        print("woof woof")

    def fetch_stick(self):
        """
        a unique method for dogs only
        :return: none
        """
        print("There you go, sir!")


class Cat(Animal):
    """A class used to represent a cat which is a kind of an animal in the zoo"""

    def talk(self):
        """
        overrides the "talk" method of superclass Animal, so Cat has it's unique talk
        :return: none
        """
        print("meow")

    def chase_laser(self):
        """
        a unique method for cats only
        :return: none
        """
        print("Meeeeow")


class Skunk(Animal):
    """A class used to represent a skunk which is a kind of an animal in the zoo"""
    def __init__(self, _name, _hunger=0, _stink_count=6):
        """
        additional skunk attribute for the superclass animal attributes
        :return: none
        """
        super().__init__(self)
        self._name = _name
        self._hunger = _hunger
        self._stink_count = _stink_count

    def talk(self):
        """
        overrides the "talk" method of superclass Animal, so Skunk has it's unique talk
        :return: none
        """
        super().talk()
        print("tsssss")

    def stink(self):
        """
        a unique method for skanks only
        :return: none
        """
        print("Dear lord!")


class Unicorn(Animal):
    """A class used to represent a unicorn which is a kind of an animal in the zoo"""
    def talk(self):
        """
        overrides the "talk" method of superclass Animal, so unicorn has it's unique talk
        :return: none
        """
        super().talk()
        print("Good day, darling")

    def sing(self):
        """
        a unique method for unicorns only
        :return: none
        """
        print("I’m not your toy...")


class Dragon(Animal):
    """A class used to represent a dragon which is a kind of an animal in the zoo"""
    def __init__(self, _name, _hunger=0, _color="Green"):
        """
        additional skunk attribute for the superclass animal attributes
        :return: none
        """
        super().__init__(self)
        self._name = _name
        self._hunger = _hunger
        self._color = _color

    def talk(self):
        """
        overrides the "talk" method of superclass Animal, so dragon has it's unique talk
        :return: none
        """
        super().talk()
        print("raaaawr")

    def breathe_fire(self):
        """
        a unique method for dragons only
        :return: none
        """
        print("$@#$#@$")


def main():
    print(f"Welcome to {Animal.zoo_name}!\n---")
    """creating 2 of each animal in the zoo"""
    brownie = Dog("Brownie", 10)
    zelda = Cat("Zelda", 3)
    stinky = Skunk("Stinky", 0)
    keith = Unicorn("Keith", 7)
    lizzy = Dragon("Lizzy", 1450)
    doggo = Dog("Doggo", 80)
    kitty = Cat("Kitty", 80)
    stinkyjr = Skunk("Stinky Jr.", 80)
    clair = Unicorn("Clair", 80)
    mcfly = Dragon("McFly", 80)

    # making a list of all the animals, and feeding every hungry animal until it's full.
    zoo_list = [brownie, zelda, stinky, keith, lizzy, doggo, kitty, stinkyjr, clair, mcfly]

    for animal in zoo_list:
        # print(animal._hunger)
        if animal.is_hungry():
            print(f"feeding time for {animal.get_name()} the {type(animal).__name__}")  # __name__ for getting only the class name
        else:
            print(f"{animal.get_name()} the {type(animal).__name__} is not hungry")
        while animal.is_hungry():
            animal.feed()
        animal.talk()
        # print(f"{animal.get_name()} is full, {animal._hunger}")

        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breathe_fire()
        print("---")

    # print(lizzy._color)
    # print(stinky._stink_count)


if __name__ == '__main__':
    main()
