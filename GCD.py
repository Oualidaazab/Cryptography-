#!/bin/python3
import  os
from  math import  gcd 
from functools  import reduce 

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The  function accepts INTEGER_ARRAY a as parameter.
# 
# we want to check if there exist a subset wher the conditions below are correct 
# if b is not empty  
#ther is no exist integer which divides all element is b  x=x>1   GCD==1
# ther is no  equal number (integers) in this subset 
def solve(a): #  123 
    # Write your code here   
    A=list(set(a)) 
    g=reduce(gcd,A)     
    if g==1 :
       return "YES" 
    else : 
        return "NO" 

 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        a_count = int(input().strip())

        a = list(map(int, input().rstrip().split()))

        result = solve(a)

        fptr.write(result + '\n')

    fptr.close()
# reduce mean 
gcd(unique_A[0],
    gcd(unique_A[1],
        gcd(unique_A[2], ...)))

# we can use  while loop   or for loop  

g = unique_A[0]
i = 1
while i < len(unique_A):
    g = gcd(g, unique_A[i])
    i += 1
# for loop 
from math import gcd

g = unique_A[0]
for x in unique_A[1:]:
    g = gcd(g, x)

if g == 1:
    print("YES")
else:
    print("NO")


