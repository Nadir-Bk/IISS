# Ram is a Python programmer working in a school. For the Annual Sports Event, he has created a csv file named Result.csv, to store
# the results of students in different sports events.
# Accept() – to accept a record from the user and add it to the file Result.csv. The column headings should also be added on top of the
# csv file. 
# wonCount() – to count the number of students who have won any event. As a Python expert, help him complete the task.

import csv

def Accept():
    with open(file, 'w+') as f:
        wr = csv.writer(f)
        n = int(input("Enter No: of Records to Input: "))
        for i in range(n):
            St_Id = int(input("Enter Student ID: "))
            St_Name = input("Enter Student Name: ")
            Game_Name = input("Enter Game Name: ")
            Result = input("Enter Won or Lost the Game: ")
            data = [St_Id, St_Name, Game_Name, Result]
            wr.writerow(data)
            
def wonCount():
    with open(file, 'r') as f:
        record = csv.reader(f)
        count = 0
        for i in record:
            print(i)
            if len(i) == 4 and i[3] == 'Won':
                count += 1
        print(count, "Students have won an event")
        
file = 'Result.csv'
Accept()
wonCount()