# Write a program to implement a stack for these book_details (book_no,book_name). That is, now each item node of the stack
# contains two types of information- a book number and book name. Just implement all the stack operation using functions to push,
# pop and display operations.

def Push_book():
    n = int(input("Enter No: of Records to Input: "))
    for i in range(n):
        book_no = int(input("Enter Book No: "))
        book_name = input("Enter Book Name: ")
        data = [book_no, book_name]
        book_details.append(data)
    
def Pop_book():
    if book_details == []:
        print("Stack is underflow")
    else:
        print(book_details.pop(), "is deleted")

def display():
    n = len(book_details)
    for i in range(n-1, -1, -1):
        print(book_details[i])
        
book_details = []
Push_book()
Pop_book()
display()