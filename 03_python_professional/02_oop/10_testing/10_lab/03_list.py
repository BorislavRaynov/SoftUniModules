class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)
 
    def get_data(self):
        return self.__data
 
    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()
 
    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a
 
    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]
 
    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")
 
        self.get_data().insert(index, el)
 
    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]
 
    def get_index(self, el):
        return self.get_data().index(el)


from unittest import TestCase, main


class IntegerListTests(TestCase):
    def test_init_with_wrong_data(self):
        integers = IntegerList(1.5, 2.5, '5', 'asdasd')
        expected = []

        self.assertEqual(expected, integers._IntegerList__data)

    def test_init_data_with_no_arguments(self):
        integers = IntegerList()
        expected = []

        self.assertEqual(expected, integers._IntegerList__data)

    def test_init_data_with_correct_arguments(self):
        integers = IntegerList(-10, -1, 2, 8, 9)
        expected = [-10, -1, 2, 8, 9]

        self.assertEqual(expected, integers._IntegerList__data)

    def test_get_data(self):
        integers = IntegerList(-10, -1, 2, 8, 9)

        res = integers.get_data()
        expected = [-10, -1, 2, 8, 9]

        self.assertEqual(expected, res)

    def test_add_with_wrong_data_raises(self):
        integers = IntegerList(-10, -1, 2, 8, 9)

        with self.assertRaises(ValueError) as ex:
            integers.add('5')

        self.assertEqual("Element is not Integer", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            integers.add(2.5)

        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_add_with_correct_data_return_old_and_new_data(self):
        integers = IntegerList(-10, -1, 2, 8, 9)

        result = integers.add(5)
        expected = [-10, -1, 2, 8, 9, 5]
        self.assertEqual(expected, result)

    def test_remove_index_with_wrong_index_raises(self):
        integers = IntegerList(-10, -1, 2)

        with self.assertRaises(IndexError) as ex:
            integers.remove_index(3)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_remove_index_return_correct_element(self):
        integers = IntegerList(-10, -1, 2)

        result = integers.remove_index(2)

        self.assertEqual(2, result)

    def test_remove_index_removes_wright_element(self):
        integers = IntegerList(-10, -1, 2)

        integers.remove_index(2)

        result = integers.get_data()
        self.assertEqual([-10, -1], result)

    def test_get_with_wrong_index_raises(self):
        integers = IntegerList(-10, -1, 2)

        with self.assertRaises(IndexError) as ex:
            integers.get(3)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_returns_correct_element(self):
        integers = IntegerList(-10, -1, 2)

        result = integers.get(2)

        self.assertEqual(2, result)

    def test_insert_with_wrong_index(self):
        integers = IntegerList(-10, -1, 2)

        with self.assertRaises(IndexError) as ex:
            integers.insert(3, 2)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_with_wrong_element(self):
        integers = IntegerList(-10, -1, 2)

        with self.assertRaises(ValueError) as ex:
            integers.insert(0, '5')

        self.assertEqual("Element is not Integer", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            integers.insert(0, 2.5)

        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_insert_inserts_element_on_correct_index(self):
        integers = IntegerList(-10, -1, 2)

        integers.insert(1, 12)
        self.assertEqual([-10, 12, -1, 2], integers._IntegerList__data)

    def test_get_biggest_return_biggest_element(self):
        integers = IntegerList(-10, -1, 2)

        result = integers.get_biggest()

        self.assertEqual(2, result)

    def test_get_index_returns_correct_index_of_the_given_element(self):
        integers = IntegerList(-10, -1, 2)

        result = integers.get_index(2)

        self.assertEqual(2, result)


if __name__ == "__main__":
    main()
