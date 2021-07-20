import unittest
from Basic.Author import Author


class TestAuthor(unittest.TestCase):
    def test_normal(self):
        """
        Test author Ian Goodfellow (normal Test)
        """
        author_test = Author("https://www.goodreads.com/author/show/15182060.Ian_Goodfellow")
        self.assertEqual(author_test.name, "Ian Goodfellow ")
        self.assertEqual(author_test.author_id, "15182060")
        self.assertEqual(author_test.author_url, "https://www.goodreads.com/author/show/15182060.Ian_Goodfellow")

    def test_not_famous_author(self):
        """
        Test author Austin Frakt
        """
        author_test = Author("https://www.goodreads.com/author/show/8261139.Austin_Frakt")
        self.assertEqual(author_test.name, "Austin Frakt ")
        self.assertEqual(author_test.author_id, "8261139")
        self.assertEqual(author_test.author_url, "https://www.goodreads.com/author/show/8261139.Austin_Frakt")


if __name__ == '__main__':
    unittest.main()
