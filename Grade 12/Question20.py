#Write a Program to generate values from 1 to 10 and then remove all the odd numbers from the list
def num_range(start, stop):
    for i in range(start, stop+1):
        num_list.append(i)
    print(num_list, "is your list")
    
def del_odd(list):
    for i in list:
        if i %2 == 1:
            list.remove(i)
    print(list, "is the list without odd numbers")

num_list = []
n1 = int(input("Enter Start Value: "))
n2 = int(input("Enter Stop Value: "))
num_range(n1,n2)
del_odd(num_list)
