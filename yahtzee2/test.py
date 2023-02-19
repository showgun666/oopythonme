import unittest
from unittest.mock import Mock
from unittest import TestCase

class CarShop:

    @staticmethod
    def get_owner_info(a_obj, reg_number):
        return a_obj.get_info(reg_number)    

 

class TestCar(TestCase):
    def test_get_owner_info(self):
        "Testing"
        shop = CarShop()
        mock = Mock()
        mock.get_info = Mock(return_value="Marie")

        print(self.assertEqual(shop.get_owner_info(mock, "ABC 124"), "Marie"))
 
if __name__ == '__main__':
    unittest.main()