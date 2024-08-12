# Write a user defined function, findType(mtype), that accepts mtype as parameter and displays all the records from the
# binary file CINEMA.DAT, that have the value of Movie Type as mtype.

import pickle

def findType(file, MType):
    file.seek(0)  
    load = pickle.load(file)
    for i in load:
        for key, value in i.items():
            if value[1] == MType:
                print(i)

with open("Cinema.dat", 'wb+') as f:
    records = []
    n = int(input("Enter No: of Records to input: "))
    for i in range(n):
        MNo = int(input("Enter Movie No: "))
        MName = input("Enter Movie Name: ")
        MType = input("Enter Movie Type: ")
        data = {MNo: [MName, MType]}
        records.append(data)
    pickle.dump(records, f)

with open("Cinema.dat", 'rb') as f:
    print("All records:")
    f.seek(0)  
    load = pickle.load(f)
    print(load)
    Mtype = input("Enter Movie Type to Find: ")
    findType(f, Mtype)
