#  Create a binary file student.dat to hold students' records like Roll no, Students name, and Address using the list.
# Write functions to write data, read them, and print on the screen.

import pickle

def write(file):
    with open(file, 'wb') as f:
        record = []
        n = int(input("Enter No: of Records to Input: "))
        for i in range(n):
            Roll_no = int(input("Enter Roll No: "))
            Student_name = input("Enter Student Name: ")
            Address = input("Enter Student Address: ")
            data = [Roll_no, Student_name, Address]
            record.append(data)
        pickle.dump(record, f)
        print("Data written successfully")
        
def read(file):
    with open(file, 'rb') as f:
        print(pickle.load(f))
        
file_name = 'student.dat'
write(file_name)
read(file_name)