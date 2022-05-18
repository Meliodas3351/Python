def findMaxWord(x):
    new = x.split()
    max_length = 0
    max_word = ""
    for word in new:
        if len(word) > max_length:
            max_length = len(word)
            max_word = word
    return max_word

string = input("Please enter a string ")
maxWord = findMaxWord(string)
print(maxWord)