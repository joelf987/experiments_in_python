import re

sentence = input("Enter a sentence: \n")
# oldWord = input("Which word do you want to replace? ")
# newWord = input("Enter the replacing word ")
# print("Sentence with word replaced: ", sentence.replace(oldWord, newWord))

print("Character count: ", len(re.findall("\\w", sentence)))