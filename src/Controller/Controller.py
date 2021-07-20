from View.View import View
from Processor.Processor import Processor
from API.API import api
from Basic.Parser import Parser


class Controller:
    def __init__(self):
        """
        Constructor for the controller
        """
        self.my_ui = View()
        self.my_processor = None

    def begin(self):
        """
        The begin stage of the digital library
        :return: Nothing
        """
        self.my_ui.main_menu()

    def main_process(self):
        """
        The main process stage of the digital library. This process have 3 branches that the user could choice.
        :return: Nothing
        """
        if self.my_ui.choice == 1:
            self.my_ui.input_url()
            self.my_ui.input_num_books_authors()
            self.my_processor = Processor(self.my_ui.num_books, self.my_ui.num_authors, self.my_ui.url)
            self.my_processor.get_all_books_and_authors()
        elif self.my_ui.choice == 2:
            self.my_processor = Processor(0, 0, "")
            record = self.my_ui.select_book_or_author()
            if record == 0:
                print(self.my_processor.data_storage.get("Author"))
            else:
                print(self.my_processor.data_storage.get("Book"))
        elif self.my_ui.choice == 3:
            self.my_processor = Processor(0, 0, "")
            self.my_ui.import_data_to_which_folder()
            self.my_processor.import_json_file(self.my_ui.kind, self.my_ui.address)
        elif self.my_ui.choice == 4:
            raw = self.my_ui.get_choice()
            self.my_processor = Processor(self.my_ui.num_books, self.my_ui.num_authors, self.my_ui.url)
            my_parser = None
            if raw[0] == 0:
                my_parser = Parser(self.my_processor.data_storage, raw[1], "Author")
            else:
                my_parser = Parser(self.my_processor.data_storage, raw[1], "Book")
            print(my_parser.post_order_calculate(my_parser.tree))
        else:
            self.my_processor = Processor(self.my_ui.num_books, self.my_ui.num_authors, self.my_ui.url)
            api(self.my_processor.data_storage)
