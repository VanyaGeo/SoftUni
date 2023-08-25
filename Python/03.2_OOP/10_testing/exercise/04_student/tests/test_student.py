from unittest import TestCase, main
from project.student import Student


class StudentTests(TestCase):
    def setUp(self) -> None:
        self.student_1 = Student("Vesko")
        self.student_2 = Student("Vanya", {"Python": ["note1"]})

    def test_initialization(self):
        self.assertEqual("Vesko", self.student_1.name)
        self.assertEqual({}, self.student_1.courses)

        self.assertEqual("Vanya", self.student_2.name)
        self.assertEqual({"Python": ["note1"]}, self.student_2.courses)

    def test_enroll_course_when_name_is_in_courses(self):
        result = self.student_2.enroll("Python", ["note2"], "")

        self.assertEqual(["note1", "note2"], self.student_2.courses["Python"])
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_enroll_course_when_name_not_in_courses(self):
        result = self.student_1.enroll("JavaScript", ["note2"])

        self.assertEqual(["note2"], self.student_1.courses["JavaScript"])
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_course_when_name_not_in_courses_with_add_course_note_(self):
        result = self.student_1.enroll("JavaScript", ["note2"], "Y")

        self.assertEqual(["note2"], self.student_1.courses["JavaScript"])
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_course_when_name_not_in_courses_without_adding_the_notes(self):
        result = self.student_1.enroll("JavaScript", ["note1"], "NO_NOTE")

        self.assertEqual([], self.student_1.courses["JavaScript"])
        self.assertEqual("Course has been added.", result)

    def test_add_notes_to_existing_course_in_courses(self):
        result = self.student_2.add_notes("Python", "note2")

        self.assertEqual(["note1", "note2"], self.student_2.courses["Python"])
        self.assertEqual("Notes have been updated", result)

    def test_add_notes_to_non_existing_course_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student_1.add_notes("JavaScript", "note1")

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_existing_course(self):
        result = self.student_2.leave_course("Python")

        self.assertEqual({}, self.student_2.courses)
        self.assertEqual("Course has been removed", result)

    def test_leave_non_existing_course_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student_1.leave_course("JavaScript")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == '__main__':
    main()
