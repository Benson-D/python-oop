import random

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self,file_name):
        """Open user provide file that has one word per line and print the number of words"""
        self.file_name = open(file_name)
        #self.word_count = self.read_file()
        self.words_container = self.read_file()
        print (f"{len(self.words_container)} words read")

    def read_file(self):
        """read the user provide file, count the words in the file and return the word count"""
        self.words_container = []
        for line in self.file_name:
            cleaned_line = line.split('\n')
            self.words_container.append(cleaned_line[0])

        #print(self.words_container, 'read_file of words_container')
        return self.words_container
              

    def random_word(self):
        """Generate a single word from a file name, the single word needs to display at random"""
        #print(self.words_container, 'Word Container')
        #['cat/n' 'dog/n'] .join(/n)

        # import random file 
        # random.choice(self.file_name)
        return random.choice(self.words_container)