import unittest
from unittest import mock
from pizza import CartePizzeria, CartePizzeriaException, Pizza

class CartePizzeriaTests(unittest.TestCase):
    def setUp(self):
        self.carte = CartePizzeria()

    def test_is_empty(self):
        self.assertTrue(self.carte.is_empty())

    def test_nb_pizzas(self):
        self.assertEqual(self.carte.nb_pizzas(), 0)

    def test_add_pizza(self):
        pizza = mock.Mock(spec=Pizza)
        self.carte.add_pizza(pizza)
        self.assertEqual(self.carte.nb_pizzas(), 1)

    def test_remove_pizza(self):
        pizza1 = mock.Mock(spec=Pizza)
        pizza1.name = "Margherita"
        pizza1.ingredients = ["tomato", "mozzarella", "basil"]
        pizza2 = mock.Mock(spec=Pizza)
        pizza2.name = "Pepperoni"
        pizza2.ingredients = ["tomato", "mozzarella", "pepperoni"]
        self.carte.add_pizza(pizza1)
        self.carte.add_pizza(pizza2)

        self.carte.remove_pizza("Margherita")
        self.assertEqual(self.carte.nb_pizzas(), 1)

        with self.assertRaises(CartePizzeriaException):
            self.carte.remove_pizza("Hawaiian")

if __name__ == '__main__':
    unittest.main()