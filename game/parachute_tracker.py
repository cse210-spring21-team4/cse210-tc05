import random

class Parachute:

    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

        Args:
            self (Parachute): An instance of Parachute.
        """
        self.strikes = 0
    
    def update_strikes(self):
        """Adds a strike for each wrong answer.

        Args:
            self (Parachute): An instance of Parachute.
        
        Returns:
            Int: strikes up to 4.
        """
        

    def get_parachute(self):
        """Prints the parachute according to how many strikes there are.

        Args:
            self (Parachute): An instance of Parachute.
        
        Returns:
            string: the amount of parachute that is left.
        """
    
    def is_correct(self):
        """Determines whether the letter guessed is a letter in the word or not.

        Args:
            self (Parachute): an instance of Parachute.

        Returns:
            boolean: True if the letter is in the word; False if it is not.
