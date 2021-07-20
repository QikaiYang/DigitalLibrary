import json

from Basic.Book import Book
from Basic.Author import Author
from View.View import View
from Database.Database import Database
import time
import random

database_url = "https://cs242-97d35-default-rtdb.firebaseio.com/"


class Processor:
    def __init__(self, book_num, author_num, url):
        """
        Construct a Processor given the number of books and authors as well as the start url
        the input numbers will be passed to variable num_book and num_author
        """
        self.book_url_array = []
        self.author_url_array = []
        self.num_book = book_num
        self.num_author = author_num
        self.start_url = url
        self.data_storage = Database(database_url)
        self.my_ui = View()

    def get_all_books_and_authors(self):
        """
        Return nothing
        Get all the urls of books and authors that we are going to process and store in book_array and authors
        """
        url_book_tmp = self.start_url
        while len(self.book_url_array) < self.num_book or len(self.author_url_array) < self.num_author:
            time.sleep(1)  # need to sleep to avoid being blocked
            tmp_book = Book(url_book_tmp)
            if len(self.book_url_array) <= self.num_book:
                if url_book_tmp not in self.book_url_array:
                    self.book_url_array.append(url_book_tmp)
                    tmp_book = Book(url_book_tmp)
                    self.data_storage.write("Book", tmp_book.to_json())
                    self.my_ui.print_info_book(tmp_book, len(self.book_url_array), len(self.author_url_array))

            time.sleep(1)  # need to sleep to avoid being blocked

            if len(self.author_url_array) <= self.num_author:
                authors = tmp_book.get_author_list()
                if authors[0]['content'] not in self.author_url_array:
                    self.author_url_array.append(authors[0]['content'])
                    tmp_author = Author(authors[0]['content'])
                    self.data_storage.write("Author", tmp_author.to_json())
                    self.my_ui.print_info_author(tmp_author, len(self.book_url_array), len(self.author_url_array))

            list_urls = tmp_book.bs_raw.find_all('li', {'class': 'cover'})
            if len(list_urls) > 0:  # Avoid empty list causing errors
                url_book_tmp = list_urls[random.randint(0, len(list_urls) - 1)].find('a')['href']
            else:
                url_book_tmp = self.start_url

    def import_json_file(self, category, address):
        """
        Import a json file to the database's specified folder
        :param category: The type of the data inside the file (book or author?)
        :param address: the address of the input json file
        :return: Nothing
        """
        with open(address) as f:
            data = json.load(f)
        self.data_storage.write(category, data)
