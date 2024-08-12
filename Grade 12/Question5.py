# Write a function count_Dwords() in Python to count the words ending with a digit in a text file "Details. txt".

def count_Dwords():
    with open("Details.txt", 'r') as f:
        s = f.read()
        words = s.split()
        count = 0
        num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        for i in words:
            if i[-1] in num:
                count +=1
        print(count, 'words end with a digit')
count_Dwords()