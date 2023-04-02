import unittest
from main import Car

class CarTest(unittest.TestCase):
    def setUp(self):
        self.car1 = Car("Toyota", "Corolla", 2021, 1000, 20_000, False)
        self.car2 = Car("Honda", "Civic", 2020, 5000, 15_000, True)
        self.car3 = Car("Ford", "Mustang", 2019, 8000)
        self.car4 = Car("Chevrolet", "Camaro", 2018)

    def test_create(self):
        self.assertIsNotNone(self.car1.company)
        self.assertIsNotNone(self.car1.model)
        self.assertIsNotNone(self.car1.year)
        
        self.assertIsNotNone(self.car2.company)
        self.assertIsNotNone(self.car2.model)
        self.assertIsNotNone(self.car2.year)

        self.assertIsNotNone(self.car3.company)
        self.assertIsNotNone(self.car3.model)
        self.assertIsNotNone(self.car3.year)

        self.assertIsNotNone(self.car4.company)
        self.assertIsNotNone(self.car4.model)
        self.assertIsNotNone(self.car4.year)

        self.assertIsNone(self.car3.get_extraTire())
        self.assertIsNone(self.car4.get_cost())

        self.assertEqual(self.car3.get_km(), 8000)
        self.assertEqual(self.car4.get_km(), 0)

    def test_set_cost(self):
        new_price = 20_000
        self.car1.set_cost(new_price)
        self.assertEqual(20_000, self.car1.get_cost())

    def test_add_km(self):
        self.car1.add_km(1000)
        self.assertEqual(2000,self.car1.get_km())
        new_km = -5000
        try:
            self.car1.add_km(new_km)
        except ValueError as error:
            self.assertEqual(type(error), ValueError)

    def test_get_info(self):
        self.assertEqual(self.car1.get_info(), "Car information: \n Company: Toyota \n Model: Corolla \n Year: 2021 \n Cost: 20000")
        self.assertEqual(self.car2.get_info(), "Car information: \n Company: Honda \n Model: Civic \n Year: 2020 \n Cost: 15000")
        self.assertEqual(self.car3.get_info(), "Car information: \n Company: Ford \n Model: Mustang \n Year: 2019 ")
        self.assertEqual(self.car4.get_info(), "Car information: \n Company: Chevrolet \n Model: Camaro \n Year: 2018 ")

if __name__ == "__main__":
    unittest.main()
