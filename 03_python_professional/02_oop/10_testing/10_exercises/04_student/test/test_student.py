from unittest import TestCase

from project.student import Student


class StudentTests(TestCase):
    def test_initialising_with_no_initial_courses(self):
        student = Student("TestName")

        self.assertEqual("TestName", student.name)
        self.assertEqual(dict(), student.courses)

    def test_initialising_with_initial_courses(self):
        student = Student("TestName", {"some_course": ["some_note"]})

        self.assertEqual("TestName", student.name)
        self.assertEqual({"some_course": ["some_note"]}, student.courses)

    def test_enrolling_adds_not_existing_course_with_not_adding_note_command(self):
        student = Student("TestName", {})

        result = student.enroll("some_course", "some_note", "N")

        self.assertEqual("Course has been added.", result)
        self.assertEqual([], student.courses["some_course"])
        
    def test_enrolling_adds_not_existing_course_and_notes_with_Y_command(self):
        student = Student("TestName", {})

        result = student.enroll("some_course", ["some_note_1, some_note_2"], "Y")

        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(["some_note_1, some_note_2"], student.courses["some_course"])

    def test_enrolling_adds_not_existing_course_and_notes_with_empty_command(self):
        student = Student("TestName", {})

        result = student.enroll("some_course", ["some_note_1, some_note_2"], "")

        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(["some_note_1, some_note_2"], student.courses["some_course"])

    def test_updating_notes_in_existing_course_when_enrolling(self):
        student = Student("TestName", {"some_course": []})

        result = student.enroll("some_course", ["some_note_1, some_note_2"], "")

        self.assertIn("some_course", student.courses)
        self.assertEqual(["some_note_1, some_note_2"], student.courses["some_course"])
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_add_notes_adds_note_to_existing_course(self):
        student = Student("TestName", {"some_course": []})

        result = student.add_notes("some_course", "n_1")

        self.assertEqual("Notes have been updated", result)
        self.assertEqual(["n_1"], student.courses["some_course"])

    def test_add_notes_to_not_existing_course_raises(self):
        student = Student("TestName", {"some_course": []})

        with self.assertRaises(Exception) as ex:
            student.add_notes("some_course_1", "n_1")

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_not_existing_course_raises(self):
        student = Student("TestName", {"some_course": []})

        with self.assertRaises(Exception) as ex:
            student.leave_course("some_course_1")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_remove_existing_course_when_leave(self):
        student = Student("TestName", {"some_course": []})
        self.assertIn("some_course", student.courses)

        result = student.leave_course("some_course")

        self.assertEqual({}, student.courses)
        self.assertEqual("Course has been removed", result)
