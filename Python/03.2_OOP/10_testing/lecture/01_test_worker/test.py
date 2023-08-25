from unittest import TestCase, main
# from test_worker import Worker  # This line needs to be commented if submitting to judge


class WorkerTests(TestCase):

    def test_correct_initialization(self):
        worker = Worker("Vanya", 1000, 100)
        self.assertEqual("Vanya", worker.name)
        self.assertEqual(1000, worker.salary)
        self.assertEqual(100, worker.energy)
        self.assertEqual(0, worker.money)

    def test_work_with_energy(self):
        worker = Worker("Vanya", 1000, 100)
        worker.work()
        self.assertEqual(1000, worker.money)
        self.assertEqual(99, worker.energy)

    def test_work_with_energy_again(self):
        worker = Worker("Vanya", 1000, 100)
        worker.work()
        worker.work()
        self.assertEqual(2000, worker.money)
        self.assertEqual(98, worker.energy)

    def test_work_with_0_energy(self):
        worker = Worker("Vanya", 1000, 0)
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_work_with_negative_energy(self):
        worker = Worker("Vanya", 1000, -1)
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_rest(self):
        worker = Worker("Vanya", 1000, 100)
        worker.rest()
        self.assertEqual(101, worker.energy)

    def test_rest_again(self):
        worker = Worker("Vanya", 1000, 100)
        worker.rest()
        worker.rest()
        self.assertEqual(102, worker.energy)

    def test_get_info(self):
        worker = Worker("Vanya", 1000, 100)
        self.assertEqual("Vanya has saved 0 money.", worker.get_info())


if __name__ == '__main__':
    main()