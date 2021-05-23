import random


class Word_Tracker:

    def _init_(self):
        self.selectedWord = ''
        self.listCorrectLetters = []

    def setSelectedWord(self, selectedWord):
        self.selectedWord = selectedWord

    def trackLetter(self, letter):
        self.listCorrectLetters.append(letter)

    def printSelectedWord(self):
        return self.selectedWord
