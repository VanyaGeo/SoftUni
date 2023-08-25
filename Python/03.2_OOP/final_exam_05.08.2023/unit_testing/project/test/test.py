from unittest import TestCase, main
from project.second_hand_car import SecondHandCar


class SecondHandCarTests(TestCase):
    def setUp(self) -> None:
        self.second_hand_car = SecondHandCar("Model1", "Car_type1", 1000, 1000.5)
        self.second_hand_car2 = SecondHandCar("Model2", "Car_type2", 900, 900.5)

    def test_initialization(self):
        self.assertEqual("Model1", self.second_hand_car.model)
        self.assertEqual("Car_type1", self.second_hand_car.car_type)
        self.assertEqual(1000, self.second_hand_car.mileage)
        self.assertEqual(1000.5, self.second_hand_car.price)
        self.assertEqual([], self.second_hand_car.repairs)

    def test_price_less_than_1_error(self):
        with self.assertRaises(ValueError) as ve:
            self.second_hand_car.price = 0.5
        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))
        # self.assertEqual(1000.5, self.second_hand_car.price)

    def test_price_equal_to_1_error(self):
        with self.assertRaises(ValueError) as ve:
            self.second_hand_car.price = 1.0
        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))
        # self.assertEqual(1000.5, self.second_hand_car.price)

    def test_mileage_less_than_100_error(self):
        with self.assertRaises(ValueError) as ve:
            self.second_hand_car.mileage = 99
        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))

    def test_mileage_equal_to_100_error(self):
        with self.assertRaises(ValueError) as ve:
            self.second_hand_car.mileage = 100
        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))

    def test_set_promotional_price_greater_than_price_error(self):
        with self.assertRaises(ValueError) as ve:
            self.second_hand_car.set_promotional_price(1001)
        self.assertEqual('You are supposed to decrease the price!', str(ve.exception))

    def test_set_promotional_price_equal_to_price_error(self):
        with self.assertRaises(ValueError) as ve:
            self.second_hand_car.set_promotional_price(1000.5)
        self.assertEqual('You are supposed to decrease the price!', str(ve.exception))

    def test_set_promotional_price_successful(self):
        result = self.second_hand_car.set_promotional_price(500)
        self.assertEqual(500, self.second_hand_car.price)
        self.assertEqual('The promotional price has been successfully set.', result)

    def test_need_repair_greater_price_not_successful(self):
        result = self.second_hand_car.need_repair(501, "description")
        self.assertEqual(1000.5, self.second_hand_car.price)
        self.assertEqual('Repair is impossible!', result)

    def test_need_repair_successful(self):
        result = self.second_hand_car.need_repair(200.5, "description")
        self.assertEqual(1201, self.second_hand_car.price)
        self.assertEqual(["description"], self.second_hand_car.repairs)
        self.assertEqual('Price has been increased due to repair charges.', result)

    def test_method_gt_returning_different_types(self):
        result = self.second_hand_car > self.second_hand_car2
        self.assertEqual('Cars cannot be compared. Type mismatch!', result)

    def test_method_gt_returning_same_car_types(self):
        self.second_hand_car2 = SecondHandCar("Model2", "Car_type1", 900, 900.5)
        self.assertTrue(self.second_hand_car > self.second_hand_car2)
        self.assertFalse(self.second_hand_car2 > self.second_hand_car)

    def test_str_method_representation(self):
        result = "Model Model1 | Type Car_type1 | Milage 1000km\nCurrent price: 1000.50 | Number of Repairs: 0"
        self.assertEqual(result, str(self.second_hand_car))


if __name__ == '__main__':
    main()