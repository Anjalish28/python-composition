#Return the factorial of the number N
def factorial(N):
    # Your code goes here
    fact= 1
    if N <0:
        print("Sorry, factorial does not exist for negative numbers")
    elif N==0:
        print("Factorial of 0 is 1")
    else:
        for i in range(1,N+1):
            fact=fact*i
        print("Factorial of" , N ,"is", fact)

factorial(N=int(input()))