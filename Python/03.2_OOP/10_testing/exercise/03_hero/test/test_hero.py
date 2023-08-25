from unittest import TestCase, main
from project.hero import Hero


class HeroTests(TestCase):
    def setUp(self) -> None:
        self.hero = Hero("Vesko", 3, 50.5, 10.5)
        self.new_hero = Hero("Vanya", 5, 30.5, 5.5)

    def test_initialization(self):
        self.assertEqual("Vesko", self.hero.username)
        self.assertEqual(3, self.hero.level)
        self.assertEqual(50.5, self.hero.health)
        self.assertEqual(10.5, self.hero.damage)

    def test_battle_equal_name_error(self):
        self.new_hero.username = "Vesko"
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.new_hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_hero_health_less_than_zero_error(self):
        self.hero.health = -1
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.new_hero)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest",
                         str(ve.exception))

    def test_battle_hero_health_equal_to_zero_error(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.new_hero)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest",
                         str(ve.exception))

    def test_battle_enemy_health_less_than_zero_error(self):
        self.new_hero.health = -1
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.new_hero)

        self.assertEqual("You cannot fight Vanya. He needs to rest",
                         str(ve.exception))

    def test_battle_enemy_health_equal_to_zero_error(self):
        self.new_hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.new_hero)

        self.assertEqual("You cannot fight Vanya. He needs to rest",
                         str(ve.exception))

    def test_after_battle_hero_and_enemy_health_equal_to_zero(self):
        self.hero.level = 1
        self.hero.health = 100
        self.hero.damage = 100

        self.new_hero.level = 1
        self.new_hero.health = 100
        self.new_hero.damage = 100

        result = self.hero.battle(self.new_hero)

        self.assertEqual("Draw", result)

    def test_after_battle_hero_and_enemy_health_less_than_zero(self):
        self.hero.damage = 50
        self.new_hero.damage = 50
        result = self.hero.battle(self.new_hero)

        self.assertEqual("Draw", result)

    def test_battle_hero_win_enemy_health_less_than_zero(self):
        # self.hero.damage = 20
        self.new_hero.damage = 1
        result = self.hero.battle(self.new_hero)

        self.assertEqual("You win", result)
        self.assertEqual(4, self.hero.level)
        self.assertEqual(50.5, self.hero.health)
        self.assertEqual(15.5, self.hero.damage)

    def test_battle_enemy_win_hero_health_less_than_zero(self):
        self.hero.damage = 1
        self.new_hero.damage = 3
        result = self.hero.battle(self.new_hero)

        self.assertEqual("You lose", result)
        self.assertEqual(6, self.new_hero.level)
        self.assertEqual(32.5, self.new_hero.health)
        self.assertEqual(8, self.new_hero.damage)

    def test_str_method_expected_output(self):
        result = str(self.hero)
        expected_output = f"Hero Vesko: 3 lvl\nHealth: 50.5\nDamage: 10.5\n"

        self.assertEqual(expected_output, result)


if __name__ == '__main__':
    main()
