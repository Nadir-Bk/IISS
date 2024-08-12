# Write a function in python to read lines from “poem.Txt” and display all those words, which has two characters in it.

with open ("poem.txt", 'r') as f:
    s = f.read()
    words = s.split()
    word = []
    for i in words:
        if len(i) == 2:
            word.append(i)
print("Words with 2 characters:")
print(word)
    