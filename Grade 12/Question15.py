# Consider the following CSV file (emp.csv): 
# (i) Write python function DISPEMP() to read the content of file emp.csv and display only those records where salary is 4000 or above. 
# (ii) Write a python function DISPEMP_2() to read the content of file emp.csv and count how many employee are earning less than
# 5000.
# (iii)write a python function SNAMES() to read the content of file emp.csv and display the employee record whose name begins with
# “s” also show no. of employee with first letter ”s” out of total record.

import csv
with open('emp.csv', 'w+') as f:
    for i in range(2):
        wr = csv.writer(f)
        ide = int(input("id"))
        name = input("name")
        sa = int(input("Salary"))
        data = [ide, name, sa]
        wr.writerow(data)
        
def DISPEMP():
    with open(file, 'r') as f:
        record = csv.reader(f)
        for i in record:
            if len(i) == 3 and i[2] >= '4000':
                print(i)
                
def DISPEMP_2():
    with open(file, 'r') as f:
        record = csv.reader(f)
        for i in record:
            if len(i) == 3 and i[2] < '5000':
                print(i)
                
def SNAMES():
    with open(file, 'r') as f:
        record = csv.reader(f)
        count = 0
        for i in record:
            if len(i) == 3:
                for j in i[1]:
                    if j.startswith("S"):
                        print(i)
                        count += 1
                    
file = 'emp.csv'
DISPEMP()
DISPEMP_2()
SNAMES()