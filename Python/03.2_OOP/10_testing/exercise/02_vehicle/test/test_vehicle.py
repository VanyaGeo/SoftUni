from unittest import TestCase, main
from project.vehicle import Vehicle


class VehicleTests(TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(10.5, 100.5)

    def test_default_fuel_consumption(self):
        self.assertEqual(1.25, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_initialization(self):
        self.assertEqual(10.5, self.vehicle.fuel)
        self.assertEqual(10.5, self.vehicle.capacity)
        self.assertEqual(100.5, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_more_fuel_error(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(9)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_less_fuel_successful(self):
        self.vehicle.drive(8)

        self.assertEqual(0.5, self.vehicle.fuel)

    def test_refuel_more_fuel_error(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(0.1)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_less_fuel_successful(self):
        self.vehicle.fuel = 3
        self.vehicle.refuel(3)

        self.assertEqual(6, self.vehicle.fuel)

    def test_str_expected_result(self):
        result = self.vehicle.__str__()
        expected_result = "The vehicle has 100.5 horse power with 10.5 fuel left" \
                          " and 1.25 fuel consumption"

        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    main()