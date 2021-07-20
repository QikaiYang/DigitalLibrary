import json
from urllib.request import urlopen
import bs4
import time
import re


class Book:
    def __init__(self, book_url_):
        """
        Constructor of a Book
        :param book_url_: the url of a book
        """
        self.book_url = book_url_
        time.sleep(1)  # sleep to avoid being blocked
        bs_source = urlopen(book_url_)
        self.bs_raw = bs4.BeautifulSoup(bs_source, 'html.parser')
        self.title = self.get_title()
        self.book_id = self.get_book_id()
        self.isbn = self.get_isbn()
        self.author = self.get_author()
        self.author_url = self.get_author_url()
        self.rating = float(self.get_ratings())
        self.rating_count = int(self.get_rating_count())
        self.review_count = int(self.get_review_count())
        self.image_url = self.get_image_url()
        self.similar_books = self.get_similar_books()
        self.json_dict = {}

    def to_json(self):
        """
        Construct a json-format book
        :return: a json-format book
        """
        self.json_dict["bookUrl"] = self.book_url
        self.json_dict["title"] = self.title
        self.json_dict["id"] = self.book_id
        self.json_dict["ISBN"] = self.isbn
        self.json_dict["authorUrl"] = self.author_url
        self.json_dict["author"] = self.author
        self.json_dict["rating"] = self.rating
        self.json_dict["ratingCount"] = self.rating_count
        self.json_dict["reviewCount"] = self.review_count
        self.json_dict["imageUrl"] = self.image_url
        self.json_dict["similarBooks"] = self.similar_books
        return json.dumps(self.json_dict)

    def get_author_list(self):
        """
        Return a list of authors' raw sting
        :return:  a list of authors' raw sting
        """
        if self.bs_raw is None:
            return "-1"
        author = self.bs_raw.find_all('meta', {'property': 'books:author'})
        return author

    def get_title(self):
        """
        Return the title of a book
        :return: a string of the book's title
        """
        if self.bs_raw is None:
            return "-1"
        title = str(self.bs_raw.find('title')).replace("<title>", "").replace("</title>", "")
        title = title[:title.find("by")]
        return title

    def get_book_id(self):
        """
        Return the id of a book
        :return: a string of the book's id
        """
        book_id = re.findall('\d+', self.book_url)[0]
        return book_id

    def get_isbn(self):
        """
        Return the ISBN of a book
        :return: The ISBN of a book
        """
        if self.bs_raw is None:
            return "-1"
        if self.bs_raw.find('meta', {'property': 'books:isbn'}) is None:
            return "-1"
        isbn = str(self.bs_raw.find('meta', {'property': 'books:isbn'})['content'])
        return isbn

    def get_author(self):
        """
        Get the author's name
        :return: The name of the author
        """
        if self.bs_raw is None:
            return "-1"
        author = str(self.bs_raw.find('title')).replace("<title>", "").replace("</title>", "")
        author = author[author.find("by") + 3:]
        return author

    def get_author_url(self):
        """
        Get the author's url
        :return: The url of the author
        """
        if self.bs_raw is None:
            return "-1"
        author_url = self.bs_raw.find('meta', {'property': 'books:author'})['content']
        return author_url

    def get_rating_count(self):
        """
        Get the book's rating count
        :return: The rating count of the book
        """
        if self.bs_raw is None:
            return "-1"
        if self.bs_raw.find('meta', {'itemprop': 'ratingCount'}) is None:
            return "-1"
        return self.bs_raw.find('meta', {'itemprop': 'ratingCount'})['content'].strip()

    def get_review_count(self):
        """
        Get the book's review count
        :return: A book's review count
        """
        if self.bs_raw is None:
            return "-1"
        if self.bs_raw.find('meta', {'itemprop': 'reviewCount'}) is None:
            return "-1"
        return self.bs_raw.find('meta', {'itemprop': 'reviewCount'})['content'].strip()

    def get_ratings(self):
        """
        Get the book's ratings
        :return: A book's ratings
        """
        if self.bs_raw is None:
            return "-1"
        if self.bs_raw.find('span', {'itemprop': 'ratingValue'}) is None:
            return "-1"
        return self.bs_raw.find('span', {'itemprop': 'ratingValue'}).text.strip()

    def get_image_url(self):
        """
        Get the book's image link
        :return: the book's image link
        """
        if self.bs_raw is None:
            return "-1"
        image = self.bs_raw.find('meta', {'property': 'og:image'})['content']
        return str(image)

    def find_title(self, url):
        """
        FInad the title of the book of an url (raw format)
        :param url: url is the input book's url (raw format)
        :return: the title of a book
        """
        source = urlopen(url.find('a')['href'])
        raw = bs4.BeautifulSoup(source, 'html.parser')
        tmp_str = str(raw.find('title')).replace("<title>", "").replace("</title>", "")
        return tmp_str[:tmp_str.find("by")]

    def get_similar_books(self):
        """
        Get the book's similar books
        :return:
        """
        book_urls = self.bs_raw.find_all('li', {'class': 'cover'})
        if len(book_urls) == 0:
            return []
        elif len(book_urls) == 1:
            time.sleep(0.1)
            return [self.find_title(book_urls[0])]
        else:
            time.sleep(0.1)
            return [self.find_title(book_urls[0]), self.find_title(book_urls[1])]
