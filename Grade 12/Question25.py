# Write a function in Python to read a text file, Alpha.txt and displays those lines which begin with the word ‘You’

with open ("Alpha.txt", 'r') as f:
    s = f.readlines()
    for i in s:
        word = i.split()
        if word[0] == 'You':
            print(i)