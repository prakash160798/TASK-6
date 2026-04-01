

# Task 1: Encapsulation (User Class)

class User:
    def __init__(self):
        self.__user_name = None  
        self.__pwd = None    

    def set_user(self, user_name, pwd):
        self.__user_name = user_name
        self.__pwd = pwd

    def get_user(self):
        return self.__user_name  

    def register(self):
        print(f"Registering user: {self.__user_name}")

    def login(self):
        print(f"Logging in: {self.__user_name}")

u = User()
u.set_user("john", "1234")
u.register()
u.login()