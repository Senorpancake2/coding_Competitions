import sys
import math
import string

#map() applies a function to each item in al iterable
#split() seperates a single string by whitespace, so you can use each part separately

numbers = ["2","5","7"]
print("\nOriginal numbers as strings", numbers)

#Use map() as a quick way to iterate the list and convert strings to numbers
#map() takes 2 arguements to apply int to each string in the list

result = map(int,numbers)
print(result)

converted = list(result)

print(converted)

print("\n--- Using standard input ---\n")

line = sys.stdin.readline().rstrip()   #rstrip() removes unwated special characters # readline() reads the line
print("Line:",line)

split_line = line.split() # uses empty spaces to make the split
print("After split():", split_line)

a, b = map(int,split_line)

print("a = ", a)
print("b = ", b)

for l in sys.stdin:
    line = l.rstrip()

    a, b = map(int,line.split())

    temp_var = a+b
    b = a*b
    a = temp_var
    
    print("result",a,b)


