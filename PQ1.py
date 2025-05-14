# Programming Question 1: Write a program to change all the negative numbers in the input array to its square.

# Input Format
# Size of the array and space separated array input is taken as input and an array is made out of the inputs.
# This array is given as input parameter to the function.
# You are not supposed to take any input.

# Constraints
# NA

# Output Format
# Return the modified list.

# Sample Input 0
# 6
# 1 -2 3 -4 5 -6
# Sample Output 0
# 1 4 3 16 5 36

# Sample Input 1
# 5
# -10 -20 -30 -40 -50
# Sample Output 1
# 100 400 900 1600 2500

n=int(input())
n1=input()
l = list(map(int,n1.split()))
for i in range(len(l)):
    if l[i]<0:
        l[i]=l[i]*l[i]
print(' '.join(map(str, l)))