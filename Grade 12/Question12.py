#Write a Program to create a mirror of a given string. For example, ‘wel’ = ‘lew’
s = input("Enter a String: ")
def mirror(string):
    mir = string[::-1]
    print(mir, "is the mirror of", string)
mirror(s)