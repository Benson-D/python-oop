class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    

    # __init__ has start 
    # need to two pointers when to keep tab of the default,
    # one to generate  

    # Can have a default number for start 
    def __init__(self, start = 0):
        """Function start value has a default of zero, otherwise set to user provided start value"""
        # For python, can have self.start = self.generate_new_start = start
        self.start = start 
        self.following_number = start 

    def __repr__(self):
        return f"<serial generator start = {self.start}>"

    # use second point to update the generater
    def generate(self):
        """Increments start value by one, and returns previous start value"""
        self.following_number += 1
        return self.following_number - 1
    
    # use second point to relocated back to beginning point or start
    def reset(self):
        """Resets start value back to the original start value or by the user provided start value"""
        self.following_number = self.start



