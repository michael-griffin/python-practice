from random import randint

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, path):
        self.path = path
        self.word_list = self.get_words()
        self.print_num()

    def get_words(self):

        line_list = []
        with open(self.path, "r") as file:
            for line in file:

                line_list.append(line.strip())
        return line_list

    def print_num(self):
        print(f"{len(self.word_list)} words read")

    def random(self):
        return self.word_list[randint(0,len(self.word_list)-1)]
