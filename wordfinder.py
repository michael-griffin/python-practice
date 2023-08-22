from random import randint

class WordFinder:
    """Word Finder: finds random words from a dictionary.

    >>> wordfinder = WordFinder("words.txt")
    >>> isinstance(wordfinder.word_list, list)
    True

    >>> isinstance(wordfinder.path, str)
    True

    >>> wordfinder.random() in wordfinder.word_list
    True

    """
    def __init__(self, path):
        self.path = path
        self.word_list = self.get_words()
        # self.print_num()

    def __repr__(self):
        return f"<path={self.path} word_list={self.word_list}"

    """Reads in word list from .txt file, trims whitespace on start/end"""
    def get_words(self):
        line_list = []
        with open(self.path, "r") as file:
            for line in file:

                line_list.append(line.strip())
        return line_list

    """prints length of word_list (words read in from file)"""
    def print_num(self):
        print(f"{len(self.word_list)} words read")

    """selects a random word from word_list"""
    def random(self):
        return self.word_list[randint(0,len(self.word_list)-1)]



class SpecialWordFinder(WordFinder):
    """Extends WordFinder to get random words

    >>> special_words = SpecialWordFinder("words.txt")
    >>> special_words.get_random_word() in special_words.valid_words
    True
    """
    def __init__(self, path):
        super().__init__(path)
        valid_words = [word for word in self.word_list if len(word.strip()) != 0 and word[0] != '#']
        self.valid_words = valid_words
    """method which calls parent random(), and then checks whether selected
    line is a real word. If not, tries until it gets one"""
    def get_random_word(self):
        return self.valid_words[randint(0,len(self.valid_words)-1)]


# #test function by calling it a bunch
# word_class = SpecialWordFinder("words.txt")

# print(f"{word_class.word_list}")

# for num in range(20):
#     word_class.get_random_word()