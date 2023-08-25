from unittest import TestCase, main
from project.movie import Movie


class MovieTests(TestCase):
    def setUp(self) -> None:
        self.movie = Movie("Barbie", 2023, 5.5)
        self.other = Movie("Batman", 2022, 6.5)

    def test_initialization(self):
        self.assertEqual("Barbie", self.movie.name)
        self.assertEqual(2023, self.movie.year)
        self.assertEqual(5.5, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_name_empty_string_error(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ""

        self.assertEqual("Name cannot be an empty string!", str(ve.exception))

    def test_error_year_earlier_than_1887(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1886
        self.assertEqual("Year is not valid!", str(ve.exception))

    def test_year_equal_to_1887(self):
        self.movie.year = 1887
        self.assertEqual(1887, self.movie.year)

    def test_add_actor_when_actor_has_not_been_added_before(self):
        self.movie.add_actor("Someone")
        self.assertEqual(["Someone"], self.movie.actors)

    def test_error_add_actor_when_actor_already_has_been_added(self):
        self.movie.add_actor("Someone")
        result = self.movie.add_actor("Someone")
        self.assertEqual("Someone is already added in the list of actors!", result)
        self.assertEqual(["Someone"], self.movie.actors)

    def test_method_gt_returning_first_better_than_other(self):
        result = self.movie > self.other
        self.assertEqual('"Batman" is better than "Barbie"', result)

    def test_method_gt_returning_other_better_than_first(self):
        self.assertEqual('"Batman" is better than "Barbie"', self.other.__gt__(self.movie))

    def test_repr_return_message(self):
        self.movie.actors = ["First", "Second", "Third"]
        expected = f"Name: Barbie\nYear of Release: 2023\nRating: 5.50\nCast: First, Second, Third"
        # actual_result = self.movie.__repr__()
        actual_result = str(self.movie)
        self.assertEqual(expected, actual_result)


if __name__ == "__main__":
    main()