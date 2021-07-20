import unittest
from Basic.Book import Book


class TestBook(unittest.TestCase):
    def test_normal(self):
        """
        Test Normal book - clean code
        """
        book_test = Book("https://www.goodreads.com/book/show/3735293-clean-code")
        self.assertEqual(book_test.book_id, "3735293")
        self.assertEqual(book_test.isbn, "9780132350884")
        self.assertEqual(book_test.author, "Robert C. Martin")
        self.assertEqual(book_test.book_url, "https://www.goodreads.com/book/show/3735293-clean-code")
        self.assertEqual(book_test.title, "Clean Code: A Handbook of Agile Software Craftsmanship ")
        self.assertEqual(book_test.author_url, "https://www.goodreads.com/author/show/45372.Robert_C_Martin")
        self.assertEqual(book_test.image_url,
                         "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1436202607i/3735293"
                         "._UY630_SR1200,630_.jpg")

    def test_no_isbn(self):
        """
        Test book without isbn - Getting Real: The Smarter, Faster, Easier Way to Build a Web Application
        :return:
        """
        book_test = Book("https://www.goodreads.com/book/show/447648.Getting_Real")
        self.assertEqual(book_test.book_id, "447648")
        self.assertEqual(book_test.isbn, "null")
        self.assertEqual(book_test.author, "37 Signals")
        self.assertEqual(book_test.book_url, "https://www.goodreads.com/book/show/447648.Getting_Real")
        self.assertEqual(book_test.title, "Getting Real: The Smarter, Faster, Easier Way to Build a Web Application ")
        self.assertEqual(book_test.author_url, "https://www.goodreads.com/author/show/42537.37_Signals")
        self.assertEqual(book_test.image_url,
                         "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1384467434i/447648"
                         "._UY630_SR1200,630_.jpg")


if __name__ == '__main__':
    unittest.main()
