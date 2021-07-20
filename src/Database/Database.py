from firebase import firebase
import json

from typing import List


class Database:
    def __init__(self, url_):
        """
        Constructor of the database based on Firebase Cloud Storage
        :param url_: input database link
        """
        self.url = url_
        self.fb = firebase.FirebaseApplication(self.url, None)

    def write(self, category, stuff):
        """
        Write a stuff under category to the database
        :param category: The category of the stuff - the folder of the database
        :param stuff: The stuff to be written
        :return:
        """
        self.fb.post("/" + category, stuff)

    def get(self, category):
        """
        Export all the data under the category of the database
        :param category: The folder to be exported
        :return:
        """
        return self.fb.get("/" + category, None)

    def get_equal(self, category, prop, value):
        """
        Get the specified data with "=" under the category
        :param category:  The category of the stuff - the folder of the database
        :param prop: The property of the stuff - ISBN, reviewCount, rating, ratingCount
        :param value: The value to compare with
        :return: A list of qualified stuff
        """
        all_stuff = self.fb.get("/" + category, None)
        dic_cat = {"Author": "name", "Book": "title"}
        result = []
        for k in list(all_stuff.keys()):
            tmp = json.loads(all_stuff[k])
            if tmp[prop] == value:
                result.append(tmp[dic_cat[category]])
        return list(set(result))

    def get_smaller(self, category, prop, value):
        """
        Get the specified data with "<" under the category
        :param category:  The category of the stuff - the folder of the database
        :param prop: The property of the stuff - ISBN, reviewCount, rating, ratingCount
        :param value: The value to compare with
        :return: A list of qualified stuff
        """
        all = self.fb.get("/" + category, None)
        dicc = {"Author": "name", "Book": "title"}
        result = []
        for k in list(all.keys()):
            tmp = json.loads(all[k])
            if tmp[prop] < value:
                result.append(tmp[dicc[category]])
        return list(set(result))

    def get_larger(self, category, prop, value):
        """
        Get the specified data with "<" under the category
        :param category:  The category of the stuff - the folder of the database
        :param prop: The property of the stuff - ISBN, reviewCount, rating, ratingCount
        :param value: The value to compare with
        :return: A list of qualified stuff
        """
        all = self.fb.get("/" + category, None)
        dicc = {"Author": "name", "Book": "title"}
        result = []
        for k in list(all.keys()):
            tmp = json.loads(all[k])
            if tmp[prop] > value:
                result.append(tmp[dicc[category]])
        return list(set(result))
