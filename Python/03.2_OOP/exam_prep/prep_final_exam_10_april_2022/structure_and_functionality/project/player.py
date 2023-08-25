class Player:
    ALL_PLAYERS_NAMES = []

    def __init__(self, name: str, age: int, stamina: int = 100):
        self.name = name
        self.age = age
        self.stamina = stamina

    @property
    def need_sustenance(self):
        if self.stamina < 100:
            return True
        return False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Name not valid!")

        if value in Player.ALL_PLAYERS_NAMES:
        # elif value == (player.name for player in Player.all_players_names if player != self):
            raise Exception(f"Name {value} is already used!")

        # self.__class__.all_players_names.append(self)
        Player.ALL_PLAYERS_NAMES.append(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError(f"The player cannot be under 12 years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        # if not 0 <= value <= 100:
        if value < 0 or value > 100:
            raise ValueError(f"Stamina not valid!")
        self.__stamina = value

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"

