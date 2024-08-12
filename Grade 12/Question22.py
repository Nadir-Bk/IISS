#Write a Program to search any word in given string/sentence
def find_word(string):
    word = input("Enter the Word to be found: ")
    words = string.split()
    if word in words:
        print(word, "is no:", words.index(word)+1, "word in the string")
    else:
        print(word, "is not a word in the string")
        
s = input("Enter Your String: ")
find_word(s)