import os

class Console:
    """A code template for a computer console. The responsibility of this 
    class of objects is to control CLI display, This includes clearing the
    screen, coordinating the printing of game screen instances (with the
    parachute, word letters/blanks, and prompt), and receiving user input.
    
    Stereotype:
        Service Provider, Interfacer

    Attributes:
        director (Director): An instance of the class of objects known as Director.
        guess (string): A one-character string of promted user input.
    """


    def __init__(self):
        """The class constructor.
        
        Args:
            self (Console): an instance of Console.
        """
        self.guess = ""

    def clear_screen(self):
        """Detects OS type and sends appropriate console command to clear screen.

        Args: 
            self (Console): An instance of Console.
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_word(self, word):
        """Uses word_track object to print word line.

        Args: 
            self (Console): An instance of Console.
        """
        pass

    def print_chute(self, chute):
        """Uses parachute object to print parachute.

        Args: 
            self (Console): An instance of Console.
        """
        pass
     
    def print_and_prompt(self):
        """Gets text input from the user through the screen.

        Args: 
            self (Console): An instance of Console.
        """
        while True:
            self.clear_screen()
            self.print_word("foo")
            self.print_chute("bar")

            letter = input("Guess a letter [a-z]: ").lower().strip()
            if letter.isalpha() and len(letter) == 1:
                break
        self.guess = letter