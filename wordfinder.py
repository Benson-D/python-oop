class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self,file_name):
        """Open user provide file that has one word per line and print the number of words"""
        self.file_name = open(file_name)
        self.word_count = self.read_file()
        print (f"{self.word_count} words read")

    def read_file(self):
        """read the user provide file, count the words in the file and return the word count"""
        word_count = 0
        for line in self.file_name:
            word_count += 1
        return word_count