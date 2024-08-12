#  A list contains following record of customer. [Employee_name, department] 
# Write the following user defined functions to perform given operations on the stack name 'Hospital': 
# (i) Push_Emp() –To Push Employee names of those customers who are  in 'Ent' department
# (ii) Pop_Emp() –To Pop the names of Employee from the stack and display them. Also, display "Underflow" when there are no
# Employee in the stack. 

Emp_Name = input("Enter Employee Name: ")
Department = input("Enter Department Name: ")
data = [Emp_Name, Department]
    
def Push_Emp():
    if data[1] == 'ent':
        Hospital.append(data)
        print("Your Stack:", Hospital)
    
def Pop_Emp():
    if Hospital == []:
        print("Stack is underflow")
    else:
        print(Hospital.pop(), "is deleted")
        
Hospital = []
Push_Emp()
Pop_Emp()