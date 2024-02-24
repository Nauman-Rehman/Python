class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self,num2):
        print("Lets add")
        return self.num + num2.num
    
    def __mul__(self,num2): # it called when we initialize the object and make 
        print("Lets multiply")
        return self.num * num2.num

    def __str__(self): # it is use to print the input number (9)
        return f"Decimal Number: {self.num}"
    
    def __len__(self):
        return 1
    
n = Number(9)
print(n)
print(len(n))