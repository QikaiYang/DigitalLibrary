import json
from urllib.request import urlopen
import bs4
import time
import re


class Author:
    def __init__(self, author_url_):
        """
        Constructor of a author
        :param author_url_: input author url
        """
        self.author_url = author_url_
        time.sleep(1)  # sleep to avoid being blocked
        bs_source = urlopen(author_url_)
        self.bs_raw = bs4.BeautifulSoup(bs_source, 'html.parser')
        self.name = self.get_name()
        self.author_id = self.get_author_id()
        self.rating = float(self.get_ratings())
        self.rating_count = int(self.get_rating_count())
        self.review_count = int(self.get_review_count())
        self.image_url = self.get_image_url()
        self.author_books = self.get_authored_books()
        self.related_authors = self.get_similar_authors()
        self.json_dict = {}

    def to_json(self):
        """
        Return a json-format author string
        :return: a json-format author string
        """
        self.json_dict["name"] = self.name
        self.json_dict["authorUrl"] = self.author_url
        self.json_dict["id"] = self.author_id
        self.json_dict["rating"] = self.rating
        self.json_dict["ratingCount"] = self.rating_count
        self.json_dict["reviewCount"] = self.review_count
        self.json_dict["imageUrl"] = self.image_url
        self.json_dict["relatedAuthors"] = self.related_authors
        self.json_dict["authorBooks"] = self.author_books
        return json.dumps(self.json_dict)

    def get_name(self):
        """
        Get the name of the author
        :return: the name of the author
        """
        if self.bs_raw is None:
            return "-1"
        name = str(self.bs_raw.find('title')).replace("<title>", "").replace("</title>", "")
        name = name[:name.find("(")]
        return name

    def get_author_id(self):
        """
        Get the id of the author
        :return: the id of the author
        """
        author_id = re.findall('\d+', self.author_url)[0]
        return author_id

    def get_rating_count(self):
        """
        Get the author's rating count
        :return: The rating count of the author
        """
        if self.bs_raw is None:
            return "-1"
        if self.bs_raw.find('span', {'itemprop': 'ratingCount'}) is None:
            return "-1"
        return self.bs_raw.find('span', {'itemprop': 'ratingCount'})['content'].strip()

    def get_review_count(self):
        """
        Get the author's review count
        :return: A author's review count
        """
        if self.bs_raw is None:
            return "-1"
        if self.bs_raw.find('span', {'itemprop': 'reviewCount'}) is None:
            return "-1"
        return self.bs_raw.find('span', {'itemprop': 'reviewCount'})['content'].strip()

    def get_ratings(self):
        """
        Get the author's ratings
        :return: A author's ratings
        """
        if self.bs_raw is None:
            return "-1"
        if self.bs_raw.find('span', {'itemprop': 'ratingValue'}) is None:
            return "-1"
        return self.bs_raw.find('span', {'itemprop': 'ratingValue'}).text.strip()

    def get_image_url(self):
        """
        Get the author's image link
        :return: the author's image link
        """
        if self.bs_raw is None:
            return "-1"
        image = self.bs_raw.find('meta', {'property': 'og:image'})['content']
        return str(image)

    def get_authored_books(self):
        """
        Get the author's books
        :return: a string represents the author's books
        """
        if self.bs_raw is None:
            return "-1"
        description = str(self.bs_raw.find('meta', {'property': 'og:description'})['content'])
        description = description[description.find("Author of "):]
        return description

    def get_similar_authors(self):
        """
        Get the author's similar authors
        :return: the author's similar authors
        """
        if self.bs_raw is None:
            return "-1"
        tmp = self.bs_raw.find('a', {'class': 'leftAlignedImage'})
        if tmp is None:
            return []
        authors = [tmp['title']]
        return authors
