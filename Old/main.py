import sys
import os
from command_handler import CommandHandler

def main():
    print("Bem vindo a linguagem de programação neoBASIC")
    print("Type 'quit' para sair")
    print("Type 'help' para obter ajuda")
    print("Type 'list' para listar os comandos no programa")
    print("Type 'run' para executar o programa")
    print("Type 'clear' para limpar a tela")
    print("Type 'save' para salvar o programa")
    print("Type 'load' para carregar um programa")
    print("Type 'new' para iniciar um novo programa")
    print("Type 'edit' para editar programa")
    print("Type 'delete' para deletar o programa")

    command_handler = CommandHandler()

    while True:
        command = input(">>> ")
        if command == "quit":
            sys.exit()
        elif command == "clear":
            os.system("cls")
        else:
            command_handler.handle_command(command)

if __name__ == "__main__":
    main()