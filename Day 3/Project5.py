#Accept value of Power and Print Quotients
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
        #print(fact)
    return fact

def nCr(n,r):
    return factorial(n)//(factorial(n-r)*factorial(r))

n=int(input("Enter the power:"))

for i in range(0,n+1):
    print(nCr(n,i),end=" ")

