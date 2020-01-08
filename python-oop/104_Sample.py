# polymorphism without inheritance
class Cat:
    def speak(self):
        print('cat speaking')


class Swan:
    def speak(self):
        print('swan speaking')


def execute(pet):
    pet.speak()


pet = Cat()
execute(pet)
pet = Swan()
execute(pet)
