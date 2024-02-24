# # 1. Create a class c2d vector and use it to create another class representing a 3d vector
# class c2dvec:
#     def __init__(self, i, j):
#         self.icap = i
#         self.jcap = j
#     def __str__(self):
#         return f"{self.icap}i + {self.jcap}j"
# class c3dvec(c2dvec):
#     def __init__(self,i, j, k):
#         super().__init__(i,j)
#         self.kcap = k
#     def __str__(self):
#         return f"{self.icap}i + {self.jcap}j + {self.kcap}k"
# v2d = c2dvec(1, 3)
# v3d = c3dvec(1, 9, 7)
# print(v2d)
# print(v3d)


# # 2. create a class pets from a class animals and further create class dog from pets. Add a method bark to class dog
# class animals:
#     animalType = "Mammal"
#     print("normally walks on 4 legs")
# class pets(animals):
#     color = "White"
#     print("Humans love them and keep them to their home")
# class dog(pets):
#     def bark(self):
#         print("it barks so loud")
# d = dog()
# d.bark()


# # 3. Create a class Employee and add salary and increament properties to it.
# #    Write a method salaryAfterIncreament method with a @property decorator with a setter which changes the value of increament based on the salary
# class Employee:
#     salary = 1000
#     increament = 1.5
#     @property
#     def salaryAfterIncreament(self):
#         return self.salary * self.increament
#     @salaryAfterIncreament.setter
#     def salaryAfterIncreament(self, sai):
#         self.increament = sai/self.salary
# e = Employee()
# print(e.salaryAfterIncreament)
# print(e.increament)
# e.salaryAfterIncreament = 2000
# print(e.increament)


# # 5. Write a class Complex to represent Complex numbers, along with overloaded operators (+) and (*) which adds and multiplies them
# class Complex:
#     def __init__(self, r, i):
#         self.real = r
#         self.imaginary = i
#     def __add__(self, c):
#         return Complex(self.real + c.real, self.imaginary + c.imaginary)
#     def __mul__(self, c):
#         return Complex(self.real*c.real - self.imaginary*c.imaginary, self.real*c.imaginary + self.imaginary*c.real)
#     def __str__(self):
#         return f"{self.real} + {self.imaginary}i"
# c1 = Complex(1, 4)
# c2 = Complex(8, 5)
# print(c1 + c2)
# print(c1 * c2)


# # 5. Write a class vector representing a vector of n dimension. Overload the + and * operator which calculates the sum and the dot product of them
# class vector:
#     def __init__(self, vec):
#         self.vec = vec
#     def __str__(self):
#         str1 = ""
#         index = 0
#         for i in self.vec:
#             str1 += f" {i}a{index} +"
#             index +=1
#         return str1[:-1]
#     def __add__(self,vec2):
#         newList = []
#         for i in range(len(self.vec)):
#             newList.append(self.vec[i] + vec2.vec[i])
#         return vector(newList)
#     def __mul__(self,vec2):
#         sum = 0
#         for i in range(len(self.vec)):
#             sum += self.vec[i] * vec2.vec[i]
#         return sum
# v1 = vector([1, 4, 6])
# v2 = vector([1, 6, 9])
# print(v1)
# print(v2)
# print("The sum of above two vectors are",v1 + v2)
# print("The dot product of above two vectors are",v1 * v2)


# 6. Write __str__() method to print the vector as follows:
# 7i + 8j + 10k Assume vector of dimension 3 for this problem
class vector:
    def __init__(self, vec):
        self.vec = vec
    def __str__(self):
        
        return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"
   
v1 = vector([1, 4, 6])
v2 = vector([1, 6, 9])
print(v1)
print(v2)

# 7. Override the __len__() method ojn vector of problem 5 to display the dimension of the vector
class vector:
    def __init__(self, vec):
        self.vec = vec
    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f" {i}a{index} +"
            index +=1
        return str1[:-1]
    def __add__(self,vec2):
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i] + vec2.vec[i])
        return vector(newList)
    def __mul__(self,vec2):
        sum = 0
        for i in range(len(self.vec)):
            sum += self.vec[i] * vec2.vec[i]
        return sum
    def __len__(self):
        return len(self.vec)
v1 = vector([1, 4, 6])
v2 = vector([1, 6, 9])
print(v1)
print(v2)
print("The sum of above two vectors are",v1 + v2)
print("The dot product of above two vectors are",v1 * v2)
print(len(v1))
print(len(v2))

