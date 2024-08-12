# Write a method COUNTLINES() in Python to read lines from text file ‘TESTFILE.TXT’ and display
# the lines which are not starting with any vowel.

def COUNTLINES():
    with open('TESTFILE.txt', 'r') as f:
        count = 0
        s = f.readlines()
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for i in s:
            if i[0] not in vowels:
                count += 1
                print(count)

COUNTLINES()