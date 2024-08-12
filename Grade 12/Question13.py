# A binary file "customer.dat" has structure (Customer_number, Name, Discount_Percentage). Write a function countrec() in Python to
# read contents of the file "customer.dat" and display the details of those customer whose Discount_Percentage is above 60.

import pickle

def write():
    with open(file, 'wb+') as f:
        record = []
        n = int(input("Enter No: of Records to Input: "))
        for i in range(n):
            Customer_number = int(input("Enter Customer No: "))
            Name = input("Enter Customer Name: ")
            Discount_Percentage = int(input("Enter Discount Percentage: "))
            data = [Customer_number, Name, Discount_Percentage]
            record.append(data)
        pickle.dump(record, f)
        print("Data written successfully")

def countrec():
    with open(file, 'rb') as f:
        record = pickle.load(f)
        for i in record:
            if i[2] >= 60:
                print(i)
                
file = 'customer.dat'

write()
countrec()