'''Q13. Find a Word

Take a sentence and a word.
Find the position of that word using .find().

Example:
Sentence: I love Python
Word: Python
Position = 7
'''

sentence = input("Enter the sentence: ")
word = input("Enter the word: ")

position = sentence.find(word)
print("Position =", position)
