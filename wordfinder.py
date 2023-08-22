class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    #__init__ should take a file path
        #file should have 1 word per line
        #one attribute should be list of these words
    def __init__(self, path):
        self.path = path
        self.word_list = self.get_words()
        self.print_num()

    #get words doesn't add to word_list/return a word list.
    def get_words(self):
        #should read through self.path, then return a list of words
        #"words.txt"

        #initialize empty list, word_list
        with open(self.path, "r") as file:
            for line in file:

        #should return a list
    #done
    def print_num(self):
        print(f"{len(self.word_list)} words read")
