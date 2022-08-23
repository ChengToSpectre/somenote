import random

word1 = "i am line"
word2 = word1.upper()
word3 = word1.lower()
word4 = word1.title()
words = [word1,word2,word3,word4]
line = '-'*40
endReturn = line+words[random.randint(0,3)]+line
print(endReturn)