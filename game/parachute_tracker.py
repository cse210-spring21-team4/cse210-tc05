class Parachute_Tracker:

    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

        Args:
            self (Parachute): An instance of Parachute.
        """
        self.state_num = 0

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
        