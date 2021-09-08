import random

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self,file_name):
        """Open user provide file that has one word per line and print the number of words"""
        self.file_name = open(file_name)
        #Opening a file, getting a file object, not a file (actual file), bottom line better better name. 

        self.words_container = self.read_file()
        #keep simple just words 

        print (f"{len(self.words_container)} words read")

    def read_file(self):
        """read the user provide file, count the words in the file and return the word count"""
        self.words_container = []
        # Make a local varibale, not attr on obj, looks like assign to words-contain, not being explicit 


        for line in self.file_name:
            cleaned_line = line.split('\n')
            self.words_container.append(cleaned_line[0])

        #print(self.words_container, 'read_file of words_container')

        #Good case of list comphrension, easier to read, and same result
        return self.words_container
              

    def random_word(self):
        """Generate a single word from a file name, the single word needs to display at random"""

        # BETTER DOCSTRING, need to explain what returning, from perspective returns a list of words from the word list 

        #print(self.words_container, 'Word Container')
        #['cat/n' 'dog/n'] .join(/n)

        # import random file 
        # random.choice(self.file_name)
        return random.choice(self.words_container)


class SpecialWordFinder(WordFinder):
    # def __init__(self, file_name):
    #     """Recharacterize txt file, open file and remove unecessary syntax, # or excess space."""
    #     super().__init__(file_name)
            
        

    def read_file(self):
        """Read the user provide file, remove new line characters and comments(#), count the words in the file and returns an array"""

        #Know what you want to pass in the instance method 
        unclean = super().read_file()
        # return unclean

        #loop through super created array, need a new array variable
        #Create conditional logic to remove unwanted characters
        #Return a new array 
            # if word[0] == # skip
            # if word[0] == ""
            #      skip
            # else 
            #   add to new array
        # return new array
        special_chars_removed = []
        for word in unclean:
            print(word)
            if word == "":
                continue 
            if word.startswith('#') or "\n" in word:
                continue
            else:
                special_chars_removed.append(word)
        print(special_chars_removed, 'special words')
        # Once again could use list comphrension 
        return special_chars_removed

        #Great example of polymorphism, override and just read file
        #repr function prints the representation of value, show quotes and all of its glory 
