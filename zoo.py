from animals import Penguin, PaintedDog
from habitats import Habitat
from habitats import Aquarium

bob = Penguin("Bob")
ralph = PaintedDog("Ralph")

print(bob.walk())
print(bob.swim())

seaworld = Habitat("Sea World")
seaworld.add_animal(bob)
seaworld.add_animal(ralph)

for animal in seaworld.animals:
    print(animal)

#***** refactored after adding type checking *********#

bob = Penguin("Bob")
ralph = PaintedDog("Ralph")

seaworld = Aquarium("Sea World")
seaworld.add_swimmer_pythonic(bob)
seaworld.add_swimmer_pythonic(ralph)
seaworld.add_swimmer_type_check(ralph)

for animal in seaworld.animals:
    print(f'{animal} lives in Sea World')

# Ralph the Painted Dog can't swim, so please do not try to put it in the Sea World habitat
# Ralph the Painted Dog can't swim, so please do not try to put it in the Sea World habitat
# Bob the Penguin lives in Sea World
