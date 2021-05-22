import random

class Parachute_Tracker:

    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

        Args:
            self (Parachute): An instance of Parachute.
        """
        self.strikes = 0
        self.correct = False
        self.letter = []
    
    def update_strikes(self):
        """Adds a strike for each wrong answer.

        Args:
            self (Parachute): An instance of Parachute.
        
        Returns:
            Int: strikes up to 4.
        """
        if self.correct == True:
            self.strikes += 1
        
    def is_correct(self):
        """Determines whether the letter guessed is a letter in the word or not.

        Args:
            self (Parachute): an instance of Parachute.

        Returns:
            boolean: True if the letter is in the word; False if it is not.
        """
        if self.letter[0] == letter_in_word: 
            return True

    def get_parachute(self):
        """Prints the parachute according to how many strikes there are.

        Args:
            self (Parachute): An instance of Parachute.
        
        Returns:
            string: the amount of parachute that is left.
        """
        if self.strikes == 0: 
            print("  ___  ")
            print(" /___\ ")
            print(" \   / ")
            print("  \ /  ")
            print("   0   ")
            print("  /|\  ")
            print("  / \  ")
            print()
            print("^^^^^^^")
        elif self.strikes == 1:
            print(" /___\ ")
            print(" \   / ")
            print("  \ /  ")
            print("   0   ")
            print("  /|\  ")
            print("  / \  ")
            print()
            print("^^^^^^^")
        elif self.strikes == 2:
            print(" \   / ")
            print("  \ /  ")
            print("   0   ")
            print("  /|\  ")
            print("  / \  ")
            print()
            print("^^^^^^^")
        elif self.strikes == 3:
            print("  \ /  ")
            print("   0   ")
            print("  /|\  ")
            print("  / \  ")
            print()
            print("^^^^^^^")
        else:
            print("   X   ")
            print("  /|\  ")
            print("  / \  ")
            print()
            print("^^^^^^^")