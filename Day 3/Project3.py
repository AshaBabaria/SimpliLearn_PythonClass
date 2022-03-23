nA=4
nB=6
nC=10
fact1=1
fact2=1
fact3=1

#Logic for finding factorial of a number
for i in range(1,nA+1):
    fact1=fact1*i
for i in range(1,nB+1):
    fact2=fact2*i
for i in range(1,nC+1):
    fact3=fact3*i
#Print all factorial of
print("Factorial of ",nA,"is",fact1)
print("Factorial of ",nB,"is",fact2)
print("Factorial of ",nC,"is",fact3)

"""
#Finding factorial using function

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact


print("4!=",factorial(4))
print("6!=",factorial(6))
print("10!=",factorial(10))

"""
