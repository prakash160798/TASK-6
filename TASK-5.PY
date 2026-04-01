# Task 5: Combined Real-Time System

class User:
    users_count = 0  

    def __init__(self, name, pwd):
        self.__name = name
        self.__pwd = pwd
        User.users_count += 1

    def login(self):
        print(f"{self.__name} logged in")
        return self

    def register(self):
        print(f"{self.__name} registered")
        return self

    def greet(self):
        print("Welcome User")
        return self


class Student(User):
    def greet(self):
        print("Welcome Student")
        return self


class Faculty(User):
    def greet(self):
        print("Welcome Faculty")
        return self


# Run
s1 = Student("Rahul", "123")
f1 = Faculty("Admin", "456")

s1.login().greet().register()
f1.login().greet().register()

print("Total Users:", User.users_count)