# Write a menu driven program with Insert Record, Search Record, Update Record, Display Record in a Binary file

print("Options")
print("1. Insert a Record")
print("2. Search a Record")
print("3. Update a Record")
print("4. Display a Record")
print("5. Exit")

import pickle

def insert_1(file):
    while True:
        with open(file, 'wb+') as f:
            try:
                record = pickle.load(f)
                print(record)
                f.seek(0)
                index = int(input("Enter Index position for Record to be inserted: "))
            except:
                print("There is no Record in the file")
                record = []
            finally:
                Roll_no = int(input("Enter Roll No: "))
                Student_name = input("Enter Student Name: ")
                Address = input("Enter Student Address: ")
                data = [Roll_no, Student_name, Address]
                try:
                    record.insert(index, data)
                except:
                    record.append(data)
                finally:
                    pickle.dump(record, f)
                    exit = input("Do you want to insert again (Y/N)?: ")
                    if exit == 'N':
                        break

def search_2(file):
    while True:
        with open(file, 'rb') as f:
            try:
                content = pickle.load(f)
                header = input("Enter the Field you want to search the Record:")
                if header == 'Roll_no':
                    search = int(input("Enter Roll No to Search:"))
                    for i in content:
                        if i[0] == search:
                            print("Record Found:")
                            print(i)
                        else:
                           print("Record Not Found")
                if header == 'Student_name':
                    search = input("Enter Student Name to Search: ")
                    for i in content:
                        if i[1] == search:
                            print("Record Found:")
                            print(i)
                        else:
                            print("Record Not Found")
                if header == 'Address':
                    search  = input("Enter Address to Search: ")
                    for i in content:
                        if i[2] == search:
                            print("Record Found:")
                            print(i)
                        else:
                            print("Record Not Found")
            except:
                print("File Not Found")
            finally:
                exit = input("Do you want to search again (Y/N)?: ")
                if exit == 'N':
                    break
            
def update_3(file):
    with open(file, 'wb+') as f:
        
        try:
            record = pickle.load(f)
            print(record)
            f.seek(0)
            index = int(input("Enter Index position for Record to be updated: "))
            print(record[index])
            Roll_no = int(input("Enter Roll No: "))
            Student_name = input("Enter Student Name: ")
            Address = input("Enter Student Address: ")
            data = [Roll_no, Student_name, Address]
            try:
                record[index] = data
                pickle.dump(f, record)
            except:
                print("Invalid Index Position")
        except:
            print("There is no Record in the file to update")
            record = []
                        
def display_4(file):
    with open(file, 'rb') as f:
        try:
            record = pickle.load(f)
            print(record)
        except:
            print("File Not Found")

while True:
    choice = int(input("Enter your Desired Choice No: "))
    if choice == 1:
        insert_1(input("Enter File Name: "))
    if choice == 2:
        search_2(input("Enter File Name: "))
    if choice == 3:
        update_3(input("Enter File Name: "))
    if choice == 4:
        display_4(input("Enter File Name: "))
    if choice == 5:
        break
        