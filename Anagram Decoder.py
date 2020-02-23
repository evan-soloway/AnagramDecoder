import random
import sys

class grammatical:
     def vowel_follow_cons(word):
          
          vowels = ["a","e","i","o","u"]
          
          if word[2] not in vowels and word[7] in vowels:
               return True
          if word[2] in vowels and word[7] not in vowels:
               return True
          if word[2] in vowels and word[7] in vowels:
               return True
          else:
               return False

def word_slicer(a_word, og_word,dict_words_list,readable_dict_list):

     dictionary = open("dict.txt", "r")
     
     for dict_word in dictionary:
          if list(dict_word.rstrip('\n')) == a_word and dict_word not in dict_words_list:
               print("\nSlice is: ",*a_word, sep='')
               print("Whole word is: ",*og_word,sep='')
               print("Dictionary word is: ",dict_word[0].upper(),dict_word[1:-1],sep='')

               dict_words_list.append(dict_word)
               readable_dict_list += dict_word[0].upper() + dict_word[1:-1] + ", "
               # (dict_word, a_word)
     
     a_word = a_word[0:-1]

     if len(a_word) > 1:
          word_slicer(a_word, og_word, dict_words_list, readable_dict_list)

     return len(dict_words_list), readable_dict_list

def main():

     try:

          print("\nToototabon! My love!") 
          word = input("\nEnter a word... any word... ")

          if word == None or len(word) <= 1:
               sys.exit()

          anagram_list = []
          num_anagrams = 0
          dict_words_list = []
          readable_dict_list = []

          for num_anagrams in range (1000):

               new_anagram, printable_form = anagram_maker(word)
               
               if new_anagram not in anagram_list and grammatical.vowel_follow_cons(new_anagram) == True:
                    
                    anagram_list.append(new_anagram)
                    print("\n","WORD:", *printable_form)
                    num_dict_words, readable_dict_list = word_slicer(a_word = printable_form, og_word = printable_form, \
                                                                     dict_words_list = dict_words_list, readable_dict_list = readable_dict_list)
                    # print("\nAnagram List:", anagram_list)

          print("\nTotal Number of Whole Anagrams (no slices): " + str(len(anagram_list)))
          print("Total Number of Dictionary Words (w/ slices):", num_dict_words)

          print("Dictionary Words Extrapolated: ", *readable_dict_list)

          again = input("\nDo you want to go again? ")

          again = again.lower()

          if again == "yes" or again == "yeah":
               main()

     except:
          sys.exit()

def anagram_maker(word):
     word = word.lower()
     template = list(word)
     random.shuffle(template)
     list_word = []
     list_word += template
     template = str(template)
     return template, list_word

     

# def slicerOfSlicer(shortWord,OgWord):
        
     
main()
