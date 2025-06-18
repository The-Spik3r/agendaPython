from os import system
from Controllers.UserController import UserController
from Model.DTO.UserForCreation import UserForCreation
from Model.DTO.UserForLogin import UserForLogin
from Model.DTO.UserForView import UserForView


class UserView:
    
    def __init__(self, user =None):
        self.user_logged = user
        
    def add_user_menu(self):
        system("cls")
        print(" Alta de usuario ".center(50, "#"))
        print("-" * 50)
        username = input("Ingrese el nombre de usuario: ")
        print("-" * 50)
        password = input("Ingrese la contraseña: ")
        print("-" * 50)
        email = input("Ingrese el email: ")
        print("-" * 50)
        name = input("Ingrese el nombre: ")
        print("-" * 50)
        surname = input("Ingrese el apellido: ")
        print("-" * 50)
        user_for_creation = UserForCreation(username, password, email, name, surname)
        user_controller = UserController()
        user_controller.add_user(user_for_creation)
        input(" Presione enter para continuar ".center(50, "!"))

    def login_menu(self):
        system("cls")
        print(" Login de usuario ".center(50, "#"))
        print("-" * 50)
        username = input("Ingrese el nombre de usuario: ")
        print("-" * 50)
        password = input("Ingrese la contraseña: ")
        print("-" * 50)
        input(" Presione enter para continuar ".center(50, "!"))
        user_controller = UserController()
        user_for_login = UserForLogin(username, password)
        validation = user_controller.login(user_for_login)
        return validation

    def list_users(self):
        system("cls")
        print(" Listado de usuarios ".center(50, "#"))
        user_controller = UserController()
        users = user_controller.get_users()
        for user in users:
            print(user)
        print("#" * 50)
        input(" Presione enter para continuar ".center(50, "!"))
        
    def remove_user_menu(self):
        system("cls")
        print(" Baja de usuario ".center(50, "#"))
        print("-" * 50)
        print("-" * 50)
        user_controller = UserController()
        user_controller.remove_user(self.user_logged)
        print(" Usuario dado de baja correctamente ".center(50, "!"))
        input(" Presione enter para continuar ".center(50, "!"))
        

