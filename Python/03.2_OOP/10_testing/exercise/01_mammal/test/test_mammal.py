from unittest import TestCase, main
from project.mammal import Mammal


class MammalTests(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal("Felix", "dog", "bark")

    def test_initialization(self):
        self.assertEqual("Felix", self.mammal.name)
        self.assertEqual("dog", self.mammal.type)
        self.assertEqual("bark", self.mammal.sound)
        self.assertEqual("animals", self.mammal.get_kingdom())
        # self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound(self):
        self.assertEqual("Felix makes bark", self.mammal.make_sound())

    def test_get_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info(self):
        self.assertEqual("Felix is of type dog", self.mammal.info())


if __name__ == "__main__":
    main()