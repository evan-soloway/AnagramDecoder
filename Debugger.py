dictionary = open("file.txt", "r")

for dict_words in dictionary:
     print(list(dict_words.rstrip('\n')))
     print(type(dict_words))

dictionary.close()

