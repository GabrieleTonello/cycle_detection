import unittest, random
from LinkedList import List
from main import has_cycle



class TestHasCycle(unittest.TestCase):
    
    def test_with_cycle(self):
        list = List()
        list.append_list([1,2,3,4,5,6,7,8,9])
        list.create_cycle(0)
        self.assertEqual(has_cycle(list), 1, "Should return 1")

    def test_without_cycle(self):
        list = List()
        list.append_list([1,2,3,4,5,6,7,8,9])
        self.assertEqual(has_cycle(list), 0, "Should return 0")

    def test_empty_list(self):
        list = List()
        self.assertEqual(has_cycle(list), 0, "Should return 0")

    def test_with_cycle_and_long_list(self):
        list = List()
        for number in range(1000):
            list.append(random.randint(0,10000))
        list.create_cycle(900)
        self.assertEqual(has_cycle(list), 1, "Should return 1")

    def test_without_cycle_and_long_list(self):
        list = List()
        for number in range(1000):
            list.append(random.randint(0,10000))
        self.assertEqual(has_cycle(list), 0, "Should return 0")

if __name__ == '__main__':
    unittest.main()