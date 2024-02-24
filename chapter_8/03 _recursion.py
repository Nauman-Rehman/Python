def fact_recursive(n):
    if(n==1 or n==0):
        return 1
    return n*fact_recursive(n-1) # it calls itself with value n-1 again and again

f = int(input("Enter the number: "))
print(fact_recursive(f))