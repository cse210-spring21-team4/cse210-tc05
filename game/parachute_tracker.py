class Parachute_Tracker:
    """A code template for a parachute display. The responsibility of this
    class of objects is to display an image of a parachuting stick figure,
    adjusted for the amount of incorrect answers the user has provided.
    
    Stereotype:
        Service Provider

    Attributes:
        director (Director): An instance of the class of objects known as Director.
        guess (string): A one-character string of promted user input.
    """

    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

        Args:
            self (Parachute): An instance of Parachute.
        """
        self.state_num = 0

    def add_strike(self):
        """Increments state_num by 1.

        Args:
            self (Parachute): An instance of Parachute.
        """
        self.state_num += 1

    def get_parachute(self):
        """Prints the parachute according to how many strikes there are.

        Args:
            self (Parachute): An instance of Parachute.
        
        Returns:
            string: the amount of parachute that is left.
        """
        parachute = "\n  ___  \n /___\  \n \   / \n  \ /  \n   0   \n  /|\  \n  / \  \n \n^^^^^^^"
        if self.state_num == 1:
            parachute = "\n /___\  \n \   / \n  \ /  \n   0   \n  /|\  \n  / \  \n \n^^^^^^^"
        elif self.state_num == 2:
            parachute = "\n \   / \n  \ /  \n   0   \n  /|\  \n  / \  \n \n^^^^^^^"
        elif self.state_num == 3:
            parachute = "\n  \ /  \n   0   \n  /|\  \n  / \  \n \n^^^^^^^"
        elif self.state_num == 4:
            parachute = "\n   X   \n  /|\  \n  / \  \n \n^^^^^^^"
        return parachute
        