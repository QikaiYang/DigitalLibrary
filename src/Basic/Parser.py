from Database.Database import Database
import lark
from lark import Lark
import json

grammar = """
start: term

term: and | or | not | operator
and: term " " "AND" " " term | operator " " "AND" " " term | operator " " "AND" " "  operator
or: term " " "OR" " " term | operator " " "OR" " " term | operator " " "OR" " "  operator
not: "NOT" " " term | "NOT" " " operator
    
operator:| smaller | equal | larger
 
equal: "=" MYSTR 
larger: ">" MYSTR 
smaller: "<" MYSTR 

MYSTR: (LETTER | DIGIT) (LETTER | DIGIT | ".")*

%import common.DIGIT
%import common.LETTER
%ignore " "
"""


class Parser:
    def __init__(self, db_, command_, type_):
        """
        Constructor of the parser
        :param db_: the database
        :param command_: the command input by user
        :param type_: the type of data to get
        """
        self.parser = Lark(grammar)
        self.db = db_
        self.command = command_
        self.category = type_
        self.prop = self.command[:self.command.find(":")].replace(" ", "")
        try:
            self.tree = self.parser.parse(self.command[self.command.find(":") + 1:])
        except:
            raise NameError('Illegal command!')
        if (self.command[:self.command.find(":")]).replace(" ", "") not in \
                ["rating", "ratingCount", "reviewCount", "bookId"]:
            raise NameError('Illegal given property!')

    def post_order_calculate(self, tree):
        """
        Given a parsed tree, calculate the desired list of books or authors and return it
        :param tree: the parsed tree in lark format
        :return: a list of books or authors with specified property
        """
        if isinstance(tree, lark.Token):  # leaf
            return float(tree)
        else:  # internal node
            dic_cat = {"Author": "name", "Book": "title"}
            if tree.data == "smaller":
                return self.db.get_smaller(self.category, self.prop, self.post_order_calculate(tree.children[0]))
            elif tree.data == "larger":
                return self.db.get_larger(self.category, self.prop, self.post_order_calculate(tree.children[0]))
            elif tree.data == "equal":
                return self.db.get_equal(self.category, self.prop, self.post_order_calculate(tree.children[0]))
            elif tree.data == "and":
                return list(
                    set(self.post_order_calculate(tree.children[0])) & set(self.post_order_calculate(tree.children[1])))
            elif tree.data == "or":
                return list(
                    set(self.post_order_calculate(tree.children[0])) | set(self.post_order_calculate(tree.children[1])))
            elif tree.data == "not":
                all_stuff = self.db.get(self.category)
                child_data = self.post_order_calculate(tree.children[0])
                print(len(child_data))
                result = []
                for k in list(all_stuff.keys()):
                    tmp = json.loads(all_stuff[k])
                    if tmp[dic_cat[self.category]] not in child_data:
                        result.append(tmp[dic_cat[self.category]])
                return list(set(result))
            else:
                return self.post_order_calculate(tree.children[0])
