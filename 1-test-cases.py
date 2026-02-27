import sys
import math
import string

#Read number of text cases from stdin
Test_line = sys.stdin.readline().rstrip() #Default is string

print(Test_line)

T = int(Test_line)
print("number of test cases", T)

for i in range(T):
    
    
    a, b = map(int,line.split())


    result_1 = a+b
    result_2 = a*b


    print("Result:", result_1, result_2 )