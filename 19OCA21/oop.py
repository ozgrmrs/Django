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

class Person:
    name = 'Barry'
    age = 44

    def test(self):
        print('test')

    def set_details(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location

    def get_details(self):
        print("name", self.name, self.age, self.location)
    

person1 = Person()
# person1.test()
# Person.test(person1)
# person1.get_details()
person1.set_details('Aaron',35, 'Usak')
person1.get_details()