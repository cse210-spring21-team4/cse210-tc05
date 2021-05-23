import random

class Word_Select:

    def Word_Select(self):
        # reads the file and splits it into a list
        word_file = open("wordlist.10000.txt", "r")
        content = word_file.read()
        content_list = content.split()
        # picks a word
        picked_word = random.sample(content_list,1)
        # converts list length 1 into a string
        final_word = ""
        for ele in picked_word:
            final_word = ele
        # returns string
        return final_word