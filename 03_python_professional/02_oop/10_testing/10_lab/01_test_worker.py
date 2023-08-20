class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


from unittest import TestCase, main


class WorkerTests(TestCase):
    def test_validity_of_the_init_data(self):
        worker = Worker("Test", 1000, 100)

        self.assertEqual("Test", worker.name)
        self.assertEqual(1000, worker.salary)
        self.assertEqual(100, worker.energy)
        self.assertEqual(0, worker.money)

    def test_energy_increase_after_rest(self):
        worker = Worker("Test", 1000, 100)

        worker.rest()

        self.assertEqual(101, worker.energy)

    def test_work_with_negative_energy_raises(self):
        worker = Worker("Test", 1000, -1)

        with self.assertRaises(Exception) as ex:
            worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_work_with_zero_energy_raises(self):
        worker = Worker("Test", 1000, 0)

        with self.assertRaises(Exception) as ex:
            worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_money_increased_after_work_(self):
        worker = Worker("Test", 1000, 100)

        worker.work()

        self.assertEqual(1000, worker.money)

    def test_energy_decreased_after_work(self):
        worker = Worker("Test", 1000, 100)

        worker.work()

        self.assertEqual(99, worker.energy)

    def test_get_info(self):
        worker = Worker("Test", 1000, 100)

        result = worker.get_info()
        expected = "Test has saved 0 money."

        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
