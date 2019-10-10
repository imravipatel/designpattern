class Dog:
    """One of the objects to be returned"""

    def speak(self):
        return "Woof!"

    def __str__(self):
        return "Dog"

class DogFactory:
    """Concrete factory"""

    def get_pet(self):
        """Returns a dog object"""
        return Dog()

    def get_food(self):
        """Returns a dog food object"""
        return "Dog Food!"

class Cat:
    """One of the objects to be returned"""

    def speak(self):
        return "Meaow!"

    def __str__(self):
        return "Cat"

class CatFactory:
    """Concrete factory"""

    def get_pet(self):
        """Returns a cat object"""
        return Cat()

    def get_food(self):
        """Returns a cat food object"""
        return "Cat Food!"

class PetStore:
    """PetStore houses our Abstract Factory"""

    def __init__(self, pet_factory=None):
        """pet_factory is our abstract factory"""
        self._pet_factory = pet_factory

    def show_pet(self):
        """Utility method to display the details of the objects returned by the DogFactory"""
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print("Our pet is '{}'".format(pet))
        print("Our pet says hello by '{}'".format(pet.speak()))
        print("Its food is '{}'".format(pet_food))


#Create a Concrete Factory
dog_factory = DogFactory()
cat_factory = CatFactory()

#Create a Pet Store housing our Abstract Factory
shop = PetStore(dog_factory)

#Invoke the utility method to show the details of the pet
shop.show_pet()
