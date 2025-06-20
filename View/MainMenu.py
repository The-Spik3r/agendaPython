from os import system

from .ContactView import ContactView
from .UserView import UserView


class MainMenu:
    def menu(self):
        while True:
            system("cls")
            print(" Bienvenido a la agenda de contactos ".center(50, "#"))
            print("1. Login de usuario")
            print("2. Registro de usuario")
            print("3. Listar Usuarios")
            print("4. dar de baja un usuario")
            print("5. Salir del programa")
            print("-" * 50)
            option = input("Ingrese una opcion: ")
            if option == "1":
                user_view = UserView()
                validation = user_view.login_menu()
                if validation[0] == True:
                    user = validation[1]
                    ContactView(user).menu()
                else:
                    print(" Usuario o contraseña incorrecta ".center(50, "!"))
                    input(" Presione enter para continuar ".center(50, "!"))
            elif option == "2":
                user_view = UserView()
                validation = user_view.add_user_menu()
            elif option == "3":
                user_view = UserView()
                validation = user_view.list_users()
            elif option == "4":
                 user_view = UserView()
                 validation = user_view.login_menu()
                 if validation[0] == True:
                    user = validation[1]
                    UserView(user).remove_user_menu()
                 else:
                    print(" Usuario o contraseña incorrecta ".center(50, "!"))
                    input(" Presione enter para continuar ".center(50, "!"))
                
            elif option == "5":
                print(" Saliendo del programa... ".center(50, "#"))
                input(" Presione enter para continuar ".center(50, "!"))
                break


if __name__ == "__main__":
    main_menu = MainMenu()
    main_menu.menu()
