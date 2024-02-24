class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self,num2):
        print("Lets add")
        return self.num + num2.num
    
    def __mul__(self,num2): # it called when we initialize the object and make 
        print("Lets multiply")
        return self.num * num2.num
    
n1 = Number(4)
n2 = Number(6)
sum = n1 + n2
product = n1 * n2
print(sum)
print(product)

# ************** methods are already defined in according to operators *************
# p1 + p2 --> p1.__add__(p2)        or        p1 + p2 --> p1.__add__(self,p2)
# p1 - p2 --> p1.__sub__(p2)        or        p1 - p2 --> p1.__sub__(self,p2)
# p1 * p2 --> p1.__mul__(p2)        or        p1 * p2 --> p1.__mul__(self,p2)
# p1 / p2 --> p1.__truediv__(p2)    or    p1 / p2 --> p1.__truediv__(self,p2)
# p1 || p2 --> p1.__floordiv__(p2)  or  p1 || p2 --> p1.__floordiv__(self,p2)

# this is calld operator overloading when we write [print(a + b)] outside the class where (a,b) are objects of class
# and simultaneously def a function in class --> def __add__(self,..,..) then (+) operator don't print the sum of a and b
# but prints or gives output according to the this __add__ defined function.
# so, whatever be there in that function (+) operator perform that task  
