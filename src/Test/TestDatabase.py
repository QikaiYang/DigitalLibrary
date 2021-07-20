from Database.Database import Database
import unittest


class TestBook(unittest.TestCase):
    my_store = Database("https://cs242-97d35-default-rtdb.firebaseio.com/")

    def test_get(self):
        """
        Test if the get() function returns all the book or authors
        """
        self.assertEqual(len(self.my_store.get("Author")), 42)
        self.assertEqual(len(self.my_store.get("Book")), 140)

    def test_get_smaller_easy(self):
        """
        Test if the get_smaller() function returns all the book or authors
        """
        self.assertEqual(len(self.my_store.get_smaller("Author", "rating", 1)), 0)
        self.assertEqual(len(self.my_store.get_smaller("Author", "ratingCount", 0)), 0)
        self.assertEqual(len(self.my_store.get_smaller("Author", "reviewCount", 0)), 0)
        self.assertEqual(len(self.my_store.get_smaller("Book", "rating", 1)), 0)
        self.assertEqual(len(self.my_store.get_smaller("Book", "ratingCount", 0)), 0)
        self.assertEqual(len(self.my_store.get_smaller("Book", "reviewCount", 0)), 0)

    def test_get_smaller_hard(self):
        """
        Test if the get_smaller() function returns all the book or authors
        """
        self.assertEqual(len(self.my_store.get_smaller("Author", "rating", 4.4)), 36)
        self.assertEqual(len(self.my_store.get_smaller("Author", "ratingCount", 100)), 0)
        self.assertEqual(len(self.my_store.get_smaller("Author", "reviewCount", 50)), 3)
        self.assertEqual(len(self.my_store.get_smaller("Book", "rating", 4.4)), 119)
        self.assertEqual(len(self.my_store.get_smaller("Book", "ratingCount", 1000)), 23)
        self.assertEqual(len(self.my_store.get_smaller("Book", "reviewCount", 57)), 25)

    def test_get_larger_easy(self):
        """
        Test if the get_larger() function returns all the book or authors
        """
        self.assertEqual(len(self.my_store.get_larger("Author", "rating", 5)), 0)
        self.assertEqual(len(self.my_store.get_larger("Author", "ratingCount", 10000000)), 0)
        self.assertEqual(len(self.my_store.get_larger("Author", "reviewCount", 10000000)), 0)
        self.assertEqual(len(self.my_store.get_larger("Book", "rating", 0)), 133)
        self.assertEqual(len(self.my_store.get_larger("Book", "ratingCount", 3000)), 90)
        self.assertEqual(len(self.my_store.get_larger("Book", "reviewCount", 2000)), 27)

    def test_get_larger_hard(self):
        """
        Test if the get_larger() function returns all the book or authors
        """
        self.assertEqual(len(self.my_store.get_larger("Author", "rating", 4.4)), 1)
        self.assertEqual(len(self.my_store.get_larger("Author", "ratingCount", 100)), 37)
        self.assertEqual(len(self.my_store.get_larger("Author", "reviewCount", 50)), 34)
        self.assertEqual(len(self.my_store.get_larger("Book", "rating", 4.1)), 50)
        self.assertEqual(len(self.my_store.get_larger("Book", "ratingCount", 1000)), 110)
        self.assertEqual(len(self.my_store.get_larger("Book", "reviewCount", 57)), 107)

    def test_get_equal_easy(self):
        """
        Test if the get_equal() function returns all the book or authors
        """
        self.assertEqual(len(self.my_store.get_equal("Author", "rating", 4.4)), 0)
        self.assertEqual(len(self.my_store.get_equal("Author", "ratingCount", 100)), 0)
        self.assertEqual(len(self.my_store.get_equal("Author", "reviewCount", 50)), 0)
        self.assertEqual(len(self.my_store.get_equal("Book", "rating", 4.1)), 4)
        self.assertEqual(len(self.my_store.get_equal("Book", "ratingCount", 1000)), 0)
        self.assertEqual(len(self.my_store.get_equal("Book", "reviewCount", 57)), 1)

    def test_get_equal_hard(self):
        """
        Test if the get_equal() function returns all the book or authors
        """
        self.assertEqual(len(self.my_store.get_equal("Author", "rating", 4.2)), 2)
        self.assertEqual(len(self.my_store.get_equal("Author", "ratingCount", 9771)), 0)
        self.assertEqual(len(self.my_store.get_equal("Author", "reviewCount", 59)), 0)
        self.assertEqual(len(self.my_store.get_equal("Book", "rating", 4.7)), 0)
        self.assertEqual(len(self.my_store.get_equal("Book", "ratingCount", 9771)), 1)
        self.assertEqual(len(self.my_store.get_equal("Book", "reviewCount", 57)), 1)


if __name__ == '__main__':
    unittest.main()
