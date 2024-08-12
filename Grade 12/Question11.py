# Write a function to write data into a binary file marks.dat and display the records of students who scored more than 95 marks.
# Write a function to count records from the binary file marks.dat

import pickle

def write(file):
    with open(file, 'wb') as f:
        record = []
        n = int(input("Enter No: of Records to Input: "))
        for i in range(n):
            Roll_no = int(input("Enter Roll No: "))
            Student_name = input("Enter Student Name: ")
            Mark = int(input("Enter Student Mark: "))
            data = [Roll_no, Student_name, Mark]
            record.append(data)
        pickle.dump(record, f)
        print("Data written successfully")
        
def mark(file, score):
    with open(file, 'rb') as f:
        record = pickle.load(f)
        for i in record:
            if i[2] >= int(score):
                print(i)
                
def count_rec(file):
    with open(file, 'rb') as f:
        record = pickle.load(f)
        count = 0
        for i in record:
            count += 1
        print("There are", count, "records in the file", file)
        
file_name = 'marks.dat'
marks = 95

write(file_name)
mark(file_name, marks)
count_rec(file_name)
    