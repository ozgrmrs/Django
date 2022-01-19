import os
os.system('cls' if os.name == 'nt' else 'clear')

# def print_type(data):
#     for i in data:
#         print(i, type(i))

# test = [123, 'Barry', [1,2,3], (1,2,3), {1,2,3}, True, lambda x: x, {"name": "Barry", "age":44}]

# print_type(test)

# How to define classes

# class Person:
#     name = 'Barry'
#     age = 44

# person1 = Person()
# person2 = Person()

# # print(person1.name)
# # print(person2.name)

# # Person.job = "teacher"
# # print(person1.job)
# # print(person2.job)

# # class attributes vs instance attributes

# person1.name = "Aaron"
# print(person1.name)
# print(person2.name)

# SELF keyword

# class Person:
#     name = 'Barry'
#     age = 44

#     def test(self):
#         print('test')

#     def set_details(self, name, age, location):
#         self.name = name
#         self.age = age
#         self.location = location

#     def get_details(self):
#         print("name", self.name, self.age, self.location)
    

# person1 = Person()
# # person1.test()
# # Person.test(person1)
# # person1.get_details()
# person1.set_details('Aaron',35, 'Usak')
# person1.get_details()

# Static method

# class Person:
#     name = 'Barry'
#     age = 44
    
#     def set_details(self, name, age, location):
#         self.name = name
#         self.age = age
#         self.location = location

#     def get_details(self):
#         print("name", self.name, self.age, self.location)

#     @staticmethod
#     def salute():
#         print('Hi there!')

# person1 = Person()
# person1.salute()

# special methods

# class Person:
#     company = "Clarusway"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"Name: {self.name}      Age : {self.age}"

#     def __len__(self):
#         return self.age

#     def get_details(self):
#         print("name", self.name, self.age)

# person1 = Person('Barry',44)
# person1.get_details()

# lst = [1,2,3]
# print(lst)

# print(person1)
# print(len(lst))
# print(len(person1))
# print(len(person1.name))

# # encapsulation and abstraction

# class Person:
#     company = "Clarusway"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self._id = 5000
#         self.__id2 = 4000

#     def __str__(self):
#         return f"Name: {self.name}      Age : {self.age}"

#     def get_details(self):
#         print("name", self.name, self.age)

# person1 = Person('Barry',44)
# person1._id = 6000
# print(person1._id)
# # print(person1.__id2)
# print(person1._Person__id2)

# lst = [4,2,8,1]
# lst.sort()
# print(lst)

# inheritance and polymorphism

class Person:
    company = "Clarusway"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}      Age : {self.age}"

    def get_details(self):
        print("name", self.name, self.age)

class Employee(Person):

     def __init__(self, name, age, path):
        self.name = name
        self.age = age
        self.path= path

emp1 = Employee('Aaron',35,'FS')

print(emp1.company)