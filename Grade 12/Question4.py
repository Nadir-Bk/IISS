# Write the definition of a Python function named LongLines() which reads the contents of a text file named 'LINES.TXT' and
# displays those lines from the file which have at least 10 words in it.

def Longlines():
    with open("Lines.txt", 'r') as f:
        s = f.readlines()
        for i in s:
            word = i.split()
            if len(word) <= 10:
                print(i)
                
Longlines()