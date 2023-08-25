from unittest import TestCase, main
from car_manager import Car


class CarTests(TestCase):
    def setUp(self):
        self.car = Car('BMW', 'M3', 10, 60)

    def test_initialization(self):
        self.assertEqual('BMW', self.car.make)
        self.assertEqual('M3', self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(60, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_valid_value(self):
        self.car.make = 'Audi'

        self.assertEqual('Audi', self.car.make)

    def test_make_invalid_value(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.car.make = 0

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_valid_value(self):
        self.car.model = 'A4'

        self.assertEqual('A4', self.car.model)

    def test_model_invalid_value(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.car.model = 0

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_valid_value(self):
        self.car.fuel_consumption = 15

        self.assertEqual(15, self.car.fuel_consumption)

    def test_fuel_consumption_invalid_value(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -1

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_valid_value(self):
        self.car.fuel_capacity = 75

        self.assertEqual(75, self.car.fuel_capacity)

    def test_fuel_capacity_invalid_value(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -1

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_valid_value_positive_number(self):
        self.car.fuel_amount = 20

        self.assertEqual(20, self.car.fuel_amount)

    def test_fuel_amount_valid_value_zero(self):
        self.car.fuel_amount = 0

        self.assertEqual(0, self.car.fuel_amount)

    def test_fuel_amount_invalid_value(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_valid_value_less_than_capacity(self):
        self.car.refuel(10)
        self.assertEqual(10, self.car.fuel_amount)

    def test_refuel_valid_value_more_than_capacity(self):
        self.car.refuel(65)
        self.assertEqual(60, self.car.fuel_amount)

    def test_refuel_invalid_value_negative_value(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-10)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_invalid_value_zero(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_drive_successful(self):
        self.car.fuel_amount = 50
        distance = 100
        self.car.drive(distance)
        self.assertEqual(40, self.car.fuel_amount)

    def test_drive_not_successful(self):
        self.car.fuel_amount = 0
        distance = 100
        with self.assertRaises(Exception) as ex:
            self.car.drive(distance)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == '__main__':
    main()
