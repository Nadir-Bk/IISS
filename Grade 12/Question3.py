# Write a function ETCount() in Python, which should read each character of a text file “TESTFILE.TXT” and then count and
# display the count of occurrence of alphabets E and T individually (including small cases e and t too).

def ETCount():
    with open("TESTFILE.txt", 'r') as f:
        s = f. read()
        ECount = 0
        TCount = 0
        for i in s:
            if i == 'e' or i == 'E':
                ECount += 1
            if i == 't' or i == 'T':
                TCount += 1
        print("The Letter E and e occurs", ECount, "times")
        print("The Letter T and t occurs", TCount, "times")
ETCount()