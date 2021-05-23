import os
from game.word_tracker import Word_Tracker
from game.parachute_tracker import Parachute_Tracker

class Console:
    """A code template for a computer console. The responsibility of this 
    class of objects is to control CLI display. This includes clearing the
    screen, coordinating the printing of game screen instances (with the
    parachute, word letters/blanks, and prompt), and receiving user input.
    
    Stereotype:
        Service Provider, Interfacer

    Attributes:
        director (Director): An instance of the class of objects known as Director.
        word_tracker (Word_Tracker): An instance of the class of objects known as Director.
        parachute_tracker (Parachute_Tracker): An instance of the class of objects known as Director.
        guess (string): A one-character string of promted user input.
    """


    def __init__(self):
        """The class constructor.
        
        Args:
            self (Console): an instance of Console.
        """
        self.guess = ""
        self.parachute_tracker = Parachute_Tracker()
        self.word_tracker = Word_Tracker()

    def clear_screen(self):
        """Detects OS type and sends appropriate console command to clear screen.

        Args: 
            self (Console): An instance of Console.
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_word(self, word_progress):
        """Uses word_progess object to print word line.

        Args: 
            self (Console): An instance of Console.
        """
        pass

    def write(self, word_progress):
        """Performs all output to console, prompts user input.

        Args: 
            self (Console): An instance of Console.
        """
        prompt = "\nGuess a letter [a-z]: "
        while True:
            self.clear_screen()
            self.print_word(word_progress)
            self.parachute_tracker.get_parachute()

            letter = input(prompt).lower().strip()
            if letter.isalpha() and len(letter) == 1 and (letter not in word_progress):
                break

            prompt = "\nPlease enter a letter [a-z]\nyou have not guessed yet: "
            
        self.guess = letter

    def read(self):
        """Returns user's letter guess as one-character string.

        Args: 
            self (Console): An instance of Console.
        """
        return self.guess