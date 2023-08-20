from project.student_report_card import StudentReportCard
from unittest import TestCase, main


class TestStudentReportCard(TestCase):
    def setUp(self):
        self.card = StudentReportCard("Test", 10)

    def test_init_valid_data(self):
        self.assertEqual("Test", self.card.student_name)
        self.assertEqual(10, self.card.school_year)
        self.assertEqual({}, self.card.grades_by_subject)

    def test_set_empty_name_raise(self):
        with self.assertRaises(ValueError) as ve:
            self.card.student_name = ''

        self.assertEqual("Student Name cannot be an empty string!", str(ve.exception))

    def test_set_zero_year_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.card.school_year = 0

        self.assertEqual("School Year must be between 1 and 12!", str(ve.exception))

    def test_set_above_year_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.card.school_year = 13

        self.assertEqual("School Year must be between 1 and 12!", str(ve.exception))

    def test_set_year_with_upper_limit(self):
        self.card.school_year = 12

        self.assertEqual(12, self.card.school_year)

    def test_set_year_with_lower_limit(self):
        self.card.school_year = 1

        self.assertEqual(1, self.card.school_year)

    def test_add_grade_to_not_existing_subject_create(self):
        self.card.add_grade("math", 4)

        self.assertEqual({"math": [4]}, self.card.grades_by_subject)

    def test_add_grade_to_existing_subject_update(self):
        self.card.add_grade("math", 4)

        self.card.add_grade("math", 6)

        self.assertEqual({"math": [4, 6]}, self.card.grades_by_subject)

    def test_average_grade_by_subject_valid_result(self):
        self.card.add_grade("math", 4)
        self.card.add_grade("math", 6)
        self.card.add_grade("bio", 3)
        self.card.add_grade("bio", 5)

        result = self.card.average_grade_by_subject()
        expected = f"math: 5.00\nbio: 4.00"

        self.assertEqual(expected, result)

    def test_average_grade_for_all_subjects_valid_result(self):
        self.card.add_grade("math", 4)
        self.card.add_grade("math", 6)
        self.card.add_grade("bio", 5)
        self.card.add_grade("bio", 5)

        result = self.card.average_grade_for_all_subjects()
        expected = f"Average Grade: 5.00"

        self.assertEqual(expected, result)

    def test__repr__correct_result(self):
        self.card.add_grade("math", 4)
        self.card.add_grade("math", 6)
        self.card.add_grade("bio", 5)
        self.card.add_grade("bio", 5)

        result = str(self.card)
        expected = f"Name: Test\nYear: 10\n----------\nmath: 5.00\nbio: 5.00\n----------\nAverage Grade: 5.00"

        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
