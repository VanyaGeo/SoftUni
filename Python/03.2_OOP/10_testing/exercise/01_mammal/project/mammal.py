class Mammal:
    def __init__(self, name, mammal_type, sound):
        self.name = name
        self.type = mammal_type
        self.sound = sound
        self.__kingdom = "animals"

    def make_sound(self):
        return f"{self.name} makes {self.sound}"

    def get_kingdom(self):
        return self.__kingdom

    def info(self):
        return f"{self.name} is of type {self.type}"



my_dog = Mammal("Felix", "dog", "bark")
print(my_dog.make_sound())
print(my_dog.get_kingdom())
print(my_dog.info())
