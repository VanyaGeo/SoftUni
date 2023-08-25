from unittest import TestCase, main
from list import IntegerList


class IntegerListTests(TestCase):
    def setUp(self):
        self.int_list = IntegerList(1, 2.5, 3, "four", 5, True, 6.1, 7)

    def test_initialization(self):
        # result = self.int_list.get_data()  # == еднакво с долния ред при скрити атрибути
        result = self.int_list._IntegerList__data
        expected_result = [1, 3, 5, 7]

        self.assertEqual(expected_result, result)

    def test_initialization_empty_args(self):
        self.int_list = IntegerList()
        result = self.int_list.get_data()
        expected_result = []

        self.assertEqual(expected_result, result)

    def test_add_int(self):
        self.int_list.add(9)
        result = self.int_list.get_data()
        expected_result = [1, 3, 5, 7, 9]

        self.assertEqual(expected_result, result)

    def test_add_float_error(self):
        with self.assertRaises(ValueError) as value_err:
            self.int_list.add(9.1)

        self.assertEqual("Element is not Integer", str(value_err.exception))

    def test_add_string_error(self):
        with self.assertRaises(ValueError) as value_err:
            self.int_list.add("a")

        self.assertEqual("Element is not Integer", str(value_err.exception))

    def test_add_boolean_error(self):
        with self.assertRaises(ValueError) as value_err:
            self.int_list.add(True)

        self.assertEqual("Element is not Integer", str(value_err.exception))

    def test_remove_index_valid_index(self):
        self.int_list.remove_index(3)
        result = self.int_list.get_data()
        expected_result = [1, 3, 5]

        self.assertEqual(expected_result, result)

    def test_remove_index_invalid_index(self):
        with self.assertRaises(IndexError) as index_err:
            self.int_list.remove_index(4)

        self.assertEqual("Index is out of range", str(index_err.exception))

    def test_get_valid_index(self):
        result = self.int_list.get(1)
        expected_result = 3

        self.assertEqual(expected_result, result)

    def test_get_invalid_index(self):
        with self.assertRaises(IndexError) as index_err:
            self.int_list.get(4)

        self.assertEqual("Index is out of range", str(index_err.exception))

    def test_insert_valid_index_valid_type(self):
        self.int_list.insert(3, 6)
        result = self.int_list.get_data()
        expected_result = [1, 3, 5, 6, 7]

        self.assertEqual(expected_result, result)

    def test_insert_valid_index_invalid_type(self):
        with self.assertRaises(ValueError) as value_err:
            self.int_list.insert(2, "a")

        self.assertEqual("Element is not Integer", str(value_err.exception))

    def test_insert_invalid_index(self):
        with self.assertRaises(IndexError) as index_err:
            self.int_list.insert(4, 9)

        self.assertEqual("Index is out of range", str(index_err.exception))

    def test_get_biggest(self):
        result = self.int_list.get_biggest()
        expected_result = 7

        self.assertEqual(expected_result, result)

    def test_get_index(self):
        result = self.int_list.get_index(3)
        expected_result = 1

        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    main()









