# Write a function, vowelCount () in Python that counts and displays the number of vowels in the text file named Poem.txt.

def vowelCount():
    with open("poem.txt", 'r') as f:
        s = f.read()
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        count = 0
        for i in s:
            if i in vowels:
                count += 1
        print('There are', count, 'vowels used in this file')
vowelCount()