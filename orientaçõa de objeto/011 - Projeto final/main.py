from conf import menu, login, cadastro, menu_
import os

sair = None

while sair != 0:
    try:
        escolha = menu()

        match escolha:
            case 1:
                if login():
                    menu_login()
    
            case 2:
                cadastro()

            case 3:
                sair = 0

            case _:
                print("OPÇÃO INVALIDA")
                os.system("pause")
                os.system("cls")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        os.system("pause")
        os.system("cls")