# Given two numbers X and Y, where X = floor(A/2) and Y = ceil(A/2).
# Find the value of A.

# Input Format

# An integer is is taken as input in line 1.
# An integer is is taken as input in line 2.
# All inputs are already taken and passed to the function as input parameters.
# You are not supposed to take any input.

# Constraints

# NA

# Output Format

# Return the output value.

# Sample Input 0

# 5
# 6
# Sample Output 0

# 11
# Sample Input 1

# 21
# 22
# Sample Output 1

# 43
n=int(input())
n1=int(input())
def finding(X,Y):
    if X==Y:
        A=2*X
    else:
        A=2*X+1
    return A
c=finding(n,n1)
print(c)