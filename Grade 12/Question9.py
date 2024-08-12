# Write a program to store customer data into a binary file cust.dat using a dictionary and print them on screen after reading
# them. The customer data contains ID as key, and name, city as values

import pickle
def write(file):
    with open(file, 'wb+') as f:
        record = []
        n = int(input("Enter No: of Records to Input: "))
        for i in range(n):
            ID = int(input("Enter ID: "))
            Name = input("Enter Customer Name: ")
            City = input("Enter City: ")
            data = {ID:[Name, City]}
            record.append(data)
        pickle.dump(record, f)
        f.seek(0)
        print(pickle.load(f))
write('cust.dat')
