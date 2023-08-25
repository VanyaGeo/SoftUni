from unittest import TestCase, main
from project.plantation import Plantation


class PlantationTests(TestCase):
    def setUp(self) -> None:
        self.plantation = Plantation(5)

    def test_initialization(self):
        self.assertEqual(5, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_size_negative_number_error(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.size = -1
        self.assertEqual("Size must be positive number!", str(ve.exception))

    def test_size_equal_to_zero_number(self):
        self.plantation.size = 0
        self.assertEqual(0, self.plantation.size)

    def test_hire_worker_when_worker_already_hired_error(self):
        self.plantation.workers = ["FirstWorker"]
        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker("FirstWorker")
        self.assertEqual("Worker already hired!", str(ve.exception))

    def test_hire_worker_for_first_time(self):
        result = self.plantation.hire_worker("FirstWorker")
        self.assertEqual("FirstWorker successfully hired.", result)
        self.assertEqual(["FirstWorker"], self.plantation.workers)

    def test_len_plants_amount(self):
        self.plantation.plants = {"worker1": ["rose", "cactus"], "worker2": ["lilly"], "worker3": ["orchid"]}
        self.assertEqual(4, len(self.plantation))
        # self.assertEqual(len(self.plantation.plants), 3) = отнася се за workers (keys)

    def test_len_plants_amount_when_empty(self):
        self.plantation.plants = {}
        self.assertEqual(0, len(self.plantation))

    def test_planting_when_worker_not_in_workers_error(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("FirstWorker", "rose")
        self.assertEqual("Worker with name FirstWorker is not hired!", str(ve.exception))

    def test_planting_plants_more_than_allowed_size_error(self):
        self.plantation.plants = {"1": ["a"], "2": ["b"], "3": ["c"], "4": ["d"], "5": ["e"]}
        self.plantation.workers = ["1", "2", "3", "4", "5"]
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("5", "f")
        self.assertEqual("The plantation is full!", str(ve.exception))
        self.assertEqual({"1": ["a"], "2": ["b"], "3": ["c"], "4": ["d"], "5": ["e"]}, self.plantation.plants)

    def test_planting_plants_when_worker_in_plants(self):
        self.plantation.plants = {"1": ["a"], "2": ["b"], "3": ["c"], "4": ["d"]}
        self.plantation.workers = ["1", "2", "3", "4", "5"]
        result = self.plantation.planting("4", "e")
        self.assertEqual("4 planted e.", result)
        self.assertEqual({"1": ["a"], "2": ["b"], "3": ["c"], "4": ["d", "e"]}, self.plantation.plants)

    def test_planting_plants_when_worker_not_in_plants_but_appears_in_workers(self):
        self.plantation.plants = {"1": ["a"], "2": ["b"], "3": ["c"], "4": ["d"]}
        self.plantation.workers = ["1", "2", "3", "4", "5"]
        result = self.plantation.planting("5", "e")
        self.assertEqual("5 planted it's first e.", result)
        self.assertEqual({"1": ["a"], "2": ["b"], "3": ["c"], "4": ["d"], "5": ["e"]}, self.plantation.plants)

    def test_str_method(self):
        self.plantation.plants = {"1": ["a", "g"], "2": ["b"], "3": ["c"], "4": ["d"]}
        self.plantation.workers = ["1", "2", "3", "4"]
        result = f"Plantation size: 5\n" \
                 f"1, 2, 3, 4\n" \
                 f"1 planted: a, g\n2 planted: b\n3 planted: c\n" \
                 f"4 planted: d"
        self.assertEqual(result, str(self.plantation))
        # from_code = self.plantation.__str__()

    def test_repr_method(self):
        self.plantation.plants = {"1": ["a"], "2": ["b"], "3": ["c"], "4": ["d"]}
        self.plantation.workers = ["1", "2", "3", "4"]
        result = "Size: 5\n" \
                 "Workers: 1, 2, 3, 4"
        self.assertEqual(result, repr(self.plantation))
        # from_code = self.plantation.__repr__()


if __name__ == '__main__':
    main()
