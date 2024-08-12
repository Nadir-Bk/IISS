# Write a menu-driven program implementing user-defined functions to perform different functions as on csv file “students.csv”.
# Each record consists of a list with field elements as sid, s_name, Stream, ClassTeacher,address respectively
# (i) Write a single record to csv. 
# (ii) Write all the records in one single go onto the csv. 
# (iii) Display the contents of the csv file. 
# (iv)STUDENT_SEARCH ():Takes the sid as the input and displays all the student records.

import csv

def write1():
    with open(file, 'w+') as f:
        wr = csv.writer(f)
        St_Id = int(input("Enter Student ID: "))
        St_Name = input("Enter Student Name: ")
        Game_Name = input("Enter Game Name: ")
        Result = input("Enter Won or Lost the Game: ")
        data = [St_Id, St_Name, Game_Name, Result]
        wr.writerow(data)
        
def writeall():
    with open(file, 'w+') as f:
        wr = csv.writer(f)
        n = int(input("Enter No: of Records to input: "))
        for i in range(n):
            St_Id = int(input("Enter Student ID: "))
            St_Name = input("Enter Student Name: ")
            Game_Name = input("Enter Game Name: ")
            Result = input("Enter Won or Lost the Game: ")
            data = [St_Id, St_Name, Game_Name, Result]
            wr.writerow(data)
        
def display():
    with open(file, 'r') as f:
        record = csv.reader(f)
        for i in record:
            print(i)

def search():
    while True:
        with open(file, 'r') as f:
            record = csv.reader(f)
            sid = int(input("Enter Student ID to view: "))
            for i in record:
                if len(i) == 4 and i[0] == str(sid):
                    print(i)
        choice = input("Do you want to search another record? (Y/N): ")
        if choice == 'N':
            break
        
file = 'students.csv'
write1()
writeall()
search()