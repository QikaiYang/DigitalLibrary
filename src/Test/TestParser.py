from Database.Database import Database
from Basic.Parser import Parser
import unittest


class TestParser(unittest.TestCase):
    my_store = Database("https://cs242-97d35-default-rtdb.firebaseio.com/")

    def test_simple_smaller(self):
        """
        Test if the simple operator < works as expected
        """
        parsed = Parser(self.my_store, "rating:  <4 ", "Book")
        self.assertEqual(len(parsed.post_order_calculate(parsed.tree)), 55)
        parsed = Parser(self.my_store, "rating:  <4 ", "Author")
        self.assertEqual(len(parsed.post_order_calculate(parsed.tree)), 11)

    def test_simple_larger(self):
        """
        Test if the simple operator > works as expected
        """
        parsed = Parser(self.my_store, "rating:  >4 ", "Book")
        self.assertEqual(len(parsed.post_order_calculate(parsed.tree)), 77)
        parsed = Parser(self.my_store, "rating:  >4 ", "Author")
        self.assertEqual(len(parsed.post_order_calculate(parsed.tree)), 26)

    def test_simple_equal(self):
        """
        Test if the simple operator > works as expected
        """
        parsed = Parser(self.my_store, "rating:  =4 ", "Book")
        self.assertEqual(len(parsed.post_order_calculate(parsed.tree)), 1)
        parsed = Parser(self.my_store, "rating:  =4 ", "Author")
        self.assertEqual(len(parsed.post_order_calculate(parsed.tree)), 0)

    def test_simple_and(self):
        """
        Test if the operator AND works as expected [simple case]
        """
        parsed = Parser(self.my_store, "rating:  =4 AND >4 ", "Book")
        self.assertEqual(len(parsed.post_order_calculate(parsed.tree)), 0)
        parsed = Parser(self.my_store, "rating:  >3 AND <3", "Author")
        self.assertEqual(len(parsed.post_order_calculate(parsed.tree)), 0)

    def test_hard_and(self):
        """
        Test if the operator AND works as expected [complex case]
        """
        parsed = Parser(self.my_store, "rating:  >4 AND <4.2 ", "Book")
        self.assertEqual(len(parsed.post_order_calculate(parsed.tree)), 48)
        parsed = Parser(self.my_store, "rating:  >3 AND <4.7", "Author")
        self.assertEqual(len(parsed.post_order_calculate(parsed.tree)), 37)

    def test_simple_or(self):
        """
        Test if the operator OR works as expected [simple case]
        """
        parsed = Parser(self.my_store, "rating:  =4 OR >4 ", "Book")
        self.assertEqual(len(parsed.post_order_calculate(parsed.tree)), 78)
        parsed = Parser(self.my_store, "rating:  <0.3 OR >33", "Author")
        self.assertEqual(len(parsed.post_order_calculate(parsed.tree)), 0)

    def test_hard_or(self):
        """
        Test if the operator OR works as expected [complex case]
        """
        parsed = Parser(self.my_store, "rating:  >4 OR <4.2 ", "Book")
        self.assertEqual(len(parsed.post_order_calculate(parsed.tree)), 133)
        parsed = Parser(self.my_store, "rating:  >3 OR <4.7", "Author")
        self.assertEqual(len(parsed.post_order_calculate(parsed.tree)), 37)

    def test_not(self):
        """
        Test if the operator NOT works as expected [complex case]
        """
        parsed = Parser(self.my_store, "ratingCount:  NOT <55 ", "Book")
        self.assertEqual(len(parsed.post_order_calculate(parsed.tree)), 133)
        parsed = Parser(self.my_store, "ratingCount:  NOT <1000", "Author")
        self.assertEqual(len(parsed.post_order_calculate(parsed.tree)), 36)

    def test_complex(self):
        """
        Test if the operator NOT works as expected [complex case]
        """
        parsed = Parser(self.my_store, "ratingCount:  >178 AND NOT =1155 ", "Book")
        self.assertEqual(len(parsed.post_order_calculate(parsed.tree)), 129)


if __name__ == '__main__':
    unittest.main()
