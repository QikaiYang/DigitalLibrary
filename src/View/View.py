from pip._vendor.distlib.compat import raw_input
import validators


class View:
    def __init__(self):
        """Constructor"""
        self.choice = -1
        self.url = ""
        self.num_books = -1
        self.num_authors = -1
        self.kind = -1
        self.address = ""

    def main_menu(self):
        """
        Show the main menu to the user
        :return Nothing
        """
        print("Welcome to Qikai's digital library. This is the main menu.")
        print("1. Scraping data")
        print("2. Export scrapped data")
        print("3. Import a json file")
        print("4. Parse and execution")
        print("5. Visits API")
        self.choice = int(raw_input("Your selection:"))

    def input_url(self):
        """
        Show the input url UI to the user
        :return Nothing
        """
        print("Please input your start url")
        self.url = raw_input("Your start url:")

    def input_num_books_authors(self):
        """
        Show the UI of inputing number of books and authors
        :return Nothing
        """
        print("Please input number of books")
        self.num_books = int(raw_input("Number of books to be scrapped:"))
        print("Please input number of authors")
        self.num_authors = int(raw_input("Number of authors to be scrapped:"))
        if self.num_books > 200:
            print("WARNING!!! Number of books exceeds 200")
        if self.num_authors > 50:
            print("WARNING!!! Number of authors exceeds 50")

    def select_book_or_author(self):
        """
        Show the UI of choosing which data to present
        :return An integer choosing result
        """
        print("What kind of data are you trying to import? 0 for author. 1 for book.")
        choose = int(raw_input("Your selection. Export Book or Author?:"))
        return choose

    def import_data_to_which_folder(self):
        """
        Show the UI to choose which kind of file to import
        :return: Nothing
        """
        print("What kind of data are you trying to import? 0 for author. 1 for book.")
        self.kind = int(raw_input("Your selection:"))
        print("What is the address of your input json file?")
        self.address = raw_input("Address to json file:")

    def print_info_author(self, author, current_num_books, current_num_authors):
        """
        Show the information of a scrapped author
        :return Nothing
        """
        print("Author is added: ", author.name)
        if author.image_url == "-1":
            print("Warning! This author doesn't have an image url.")
        print("# of scrapped books is", current_num_books)
        print("# of scrapped authors is", current_num_authors)
        print("==============================================================================")

    def print_info_book(self, book, current_num_books, current_num_authors):
        """
        Show the information of a scrapped book
        :return Nothing
        """
        print("Book is added: ", book.title)
        if book.isbn == "-1":
            print("Warning! This author doesn't have an ISBN.")
        print("# of scrapped books is", current_num_books)
        print("# of scrapped authors is", current_num_authors)
        print("==============================================================================")

    def get_choice(self):
        """
        Get the choice of book or author
        :return Nothing
        """
        print("Which kind of dat do you want to query? 0 for Author, 1 for Book")
        select = int(raw_input("Enter your choice here:"))
        query = raw_input("Please enter your query here:")
        return select, query
