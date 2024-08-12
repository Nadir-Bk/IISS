#Grade 11 Practical Questions

#Program 01 [Prime Number] {*Important*}
'''
num = int(input("Enter a Number: "))
if num > 1:
    if num == 2:
        print(num, "is a Prime Number")
    else:
        for i in range(2, num):
            if num % i == 0:
                print(num, "is not a Prime Number")
                break
        else:
            print(num, "is a Prime Number")
else:
    print(num, "is not a Prime Number")
'''

#Program 02 [Multiplication Table]
'''
table = int(input("Enter Your Desired Multiplication Table: "))
output_range = int(input("Enter the No: of Products Required: "))
for i in range(1, output_range + 1):
    print(table, '*', i, '=', table*i)
'''

#Program 03 [Menu Driven Calculator]  Incomplete
'''
print("Welcome to Simple Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Quotient")

choice = int(input("Enter No: of Your Operator: "))

if choice == 1:
    sum = 0
    n = int(input("Enter No: of Values to be Added: "))
    for i in range(n):
        num = int(input("Enter Your Value to be Added: "))
        sum += num
    print("Your Sum is", sum)
        
if choice == 2:
    n = int(input("Enter No: of Values to be Subtracted: "))
    num_1 = int(input("Enter Your Initial Number: "))
    difference = num_1
    for i in range(n - 1):
        num = int(input("Enter Your Value to be Subtracted: "))
        difference -= num
    print("Your Difference is", difference)

if choice == 3:
    product = 0
    n = int(input("Enter No: of Values to be Multiplied: "))
    for i in range(n):
        num = int(input("Enter Your Values to be Multiplied: "))
        product *= num
        print("Your Product is", product)
        
if choice == 4:
    n = int(input("Enter No: of Values to be Divided: "))
    num_1 = int(input("Enter Your Initial Number: "))
    quotient = num_1
    for i in range(n - 1):
        num = int(input("Enter Your Value to be Divided: "))
        quotient /= num
    print("Your Quotient is", quotient)
'''        

#Program 04 [Sum Of Even and Odd Numbers]
'''
print("To Find Sum of Even and Odd Numbers Till a Specified Number")
Range = int(input("Enter The Range to be Added Till: "))
even = 0
odd = 0
for i in range(0, Range, 2):
    even += i
for i in range(1, Range, 2):
    odd += i
print("The Sum of Even Numbers Till", Range,  "is", even)
print("The Sum of Odd Numbers Till", Range,  "is", odd)
'''

#Program 05 [Factorial]
'''
num = int(input("Enter a Number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial of", num, "is", factorial)
'''

#Program 06 [Fibonacci Series]
'''
n = int(input("Enter Range of the Series to be Output: "))
print("Fibonacci Series: ", end = " ")
a = 1
b = 0
c = 0
for i in range(n):
    print(c, end = ", ")
    c = a + b
    a = b
    b = c
'''

#Program 07 [Armstrong Number]   {*Important*}
'''
n = int(input("Enter a Number: "))
sum = 0
num = 0
temp = n
while temp > 0:
    num = temp % 10
    sum += num**3
    temp = temp // 10
if sum == n:
    print(n, "is an Armstrong Number")
if sum != n:
    print(n, "is not an Armstrong Number")
'''

#Program 08 [Palindrome]
'''
string = input("Enter a String: ")

if string[::-1] == string:
    print(string, "is a Palindrome")
else:
    print(string, "is not a Palindrome")
'''

#Program 09 [Sum of Two Numbers]
'''
num_1 = input("Enter First Number: ")
num_2 = input("Enter First Number: ")
print(num_1 + num_2)
'''
#Program 10 [Star Pattern (Ascending)]  {*Important*}
#Ascending
'''
n = int(input("Enter no: of Lines: "))
for i in range(n + 1):
    for j in range(i):
        print("*", end = " ")
    print()
'''
#Descending
'''
n = int(input("Enter no: of Lines: "))
list = []
for e in range(1, n+1):
    list.append(e)
print (list)
for i in list[::-1]:
    for j in range(i):
        print("*", end = " ")
    print()
'''

#Program 11 [The Longest Substring of a Sentence and Remove Vowels from it]
'''
string = input("Enter a String: ")
final_word = ""
length = 0
words = string.split()
for i in words:
    if len(i) > length:
        length = len(i)
        word = i
for i in word:
    if i in "aeiou" or i in "AEIOU":
        final_word += ""
    else:
        final_word += i
print("The Longest Substring is", word, "and has", length, "Characters")
print(final_word, "is the Substring without vowels")
'''

#Program 12 [No: of Words Starting with Vowels]
'''
string = input("Enter a String: ")
words = string.split()
count = 0
for i in words:
    if i[0] in "aeiou" or i[0] in "AEIOU":
        count += 1
    else:
        count += 0
print("No: of Words starting with a vowel are", count, "words")
'''

#Program 13 [Find Largest Substring]
'''
string = input("Enter a String: ")
max_substring = ""
length = 0
words = string.split()
for i in words:
    if len(i) > length:
        length = len(i)
        max_substring = i
print("Largest word is", max_substring, "with", length, "characters")
'''

#Program 14 [Find Occurrence of "is" in a String]
'''
string = input("Enter a String: ")
words = string.split()
print("No: of times the word 'is' occurs in the string is", words.count(is))
'''

#Program 15 [String Without Vowels]
'''
string = input("Enter a String: ")
Consonant = ""
for i in string:
    if i in "aeiou" or i in "AEIOU":
        Consonant += ""
    else:
        Consonant += i
print(string, "without Vowels is", Consonant)
'''

#Program 16 [Case Study: No of Words, Characters, % of Alphanum Characters]
'''
print("Sentence Analysis for Nursery Kids")
string = input("Enter a Sentence: ")
words = len(string.split())
alphanum = 0
for i in string:
    if i.isalnum():
        alphanum += 1
    else:
        alphanum +=  0
percent = alphanum*100/len(string)
print("No: of Words =", words)
print("No: of Characters =", len(string))
print("Percentage of Alphanumeric Characters =", percent, "%")
'''

#Program 17 [Unique and Duplicate Elements in List]
'''
List = []
n = int(input("Enter No: of Elements to Enter in the List: "))
for i in range(n):
    ele = input("Enter Element: ")
    List.append(ele)
print("Your List is", List)
unique = []
duplicate = []
for i in List:
    if List.count(i) >= 2:
        if i in duplicate:
            break
        else:
            duplicate.append(i)
    if List.count(i) < 2:
        unique.append(i)
print("Unique Numbers in the List: ", unique)
print("Duplicate Numbers in the List:", duplicate)
'''

#Program 18 [Sum of Elements Ending with 3]
'''
List = []
n = int(input("Enter No: of Elements to Enter in the List: "))
for i in range(n):
    ele = int(input("Enter Element: "))
    List.append(ele)
print("Your List is", List)
sum = 0
for i in List:
    if i % 10 == 3:
        sum += i
    else:
        sum += 0
print("Sum of Elements with Digit 3 is", sum)
'''

#Program 19 [Square if int; Change case if str in List]
'''
List = []
n = int(input("Enter No: of Elements to Enter in the List: "))
for i in range(n):
    ele = input("Enter Element: ")
    List.append(ele)
print("Your List is", List)
for i in List:
    if i.isnumeric():
        square = int(i)*int(i)
        print(square)
    if i.islower():
        print(i.upper())
    if i.isupper():
        print(i.lower())
'''

#Program 20 [Count a Word in a Sentence]
'''
string = input("Enter a Sentence: ")
words = string.split()
word = input("Enter Word to be Counted: ")
print(words.count(word))
'''

#Program 21 [Check Length Of String and If Same Last and First Character of String]
'''
List = []
n = int(input("Enter No: of Elements to Enter in the List: "))
for i in range(n):
    ele = str(input("Enter String: "))
    List.append(ele)
print("Your List is", List)
for i in List:
    if len(i) > 1:
        print("String Length of", i, "=", len(i))
        if i[0] == i[-1]:
            print("The First and Last Characters are the Same in this String")
        else:
            print("The First and Last Characters are not Same in this String")
    else:
        print("String Length of", i, "=", len(i))
'''


