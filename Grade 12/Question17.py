# Write a menu-driven python program to implement stack operation.

stack = []
print("Stack Operation")
print("1. Push")
print("2. Pop")
print("3. Peek")
print("4. Display")
print("5. Exit")
while True:
    choice = int(input("Enter Choice No: "))
    if choice == 1:
        element = input("Enter Element to Insert: ")
        stack.append(element)
    if choice == 2:
        if stack == []:
            print("Stack is underflow")
        else:
            s = stack.pop()
            print("Deleted Element is", s)
    if choice == 3:
        if stack == []:
            print("Stack is underflow")
        else:
            s = stack[-1]
            print(s, "is top element")
    if choice == 4:
        n = len(stack)
        for i in range(n-1, -1, -1):
            print(stack[i])
    if choice == 5:
        break