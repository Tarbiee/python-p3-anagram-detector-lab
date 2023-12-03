# your code goes here!

class Anagram:

    def __init__(self,word):
        self.word = word

    def match(self, words):
        list = []
        for char in words:
            if sorted(self.word) == sorted(char):
                list.append(char)
        return list
