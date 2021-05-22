import random

class Word_Select:

    def Word_Select():
        # reads the file and splits it into a list
        word_file = open("wordlist.10000.txt", "r")
        content = word_file.read()
        content_list = content.split()
        # returns 1 picked word 
        return random.sample(content_list,1)









