import sys
import os

def run():
    print("Welcome to the Basic Programming Language")
    print("Type 'quit' to exit")
    print("Type 'help' to get help")
    print("Type 'list' to list all the commands")
    print("Type 'run' to run the program")
    print("Type 'clear' to clear the screen")
    print("Type 'save' to save the program")
    print("Type 'load' to load the program")
    print("Type 'new' to start a new program")
    print("Type 'edit' to edit the program")
    print("Type 'delete' to delete the program")

    program = []
    variables = {}
    
    while True:
        command = input(">>> ")
        if command == "quit":
            sys.exit()
        elif command == "help":
            print("Esta é minha pequenha linguagem de programação baseada em BASIC")
            print("You can use the following commands:")
            print("1. print - Exibe uma mensagem na tela (Exemplo: print 'Hello, World!')")
            print("2. input - Recebe um valor do usuario (Exemplo: input 'Qual seu nome ')")
            print("3. let - Salva um valor a uma variavel (Exemplo: let x = 10)")
            print("4. if - Condição (Exemplo if x > 10 then print 'x e maior que 10')")
            print("5. goto - Vai para uma linha especifica (Exemplor: goto 10)")
            print("6. end - Termina o programa")
            print("7. list - Lista todos os comandos no programa")
            print("8. run   - Executa o programa")
            print("9. clear - Limpa a tela")
            print("10. save - Salva o programa")
            print("11. load - Carrega o programa")
            print("12. new - Inicia um novo programa")
            print("13. edit - Edita o programa atual")
            print("14. delete - Deleta o programa atual")
            print("15. quit - Sair do programa atual")
        elif command == "list":
            for line in program:
                print(line)
        elif command == "run":
            for line in program:
                if line.startswith("print"):
                    expr = line[6:].strip()
                    if expr in variables:
                        print(variables[expr])
                    else:
                        print(eval(expr, {}, variables))
                elif line.startswith("input"):
                    var = line[6:].strip()
                    value = input(var + ": ")
                    variables[var] = value
                elif line.startswith("let"):
                    var, expr = line[4:].split("=", 1)
                    var = var.strip()
                    expr = expr.strip()
                    variables[var] = eval(expr, {}, variables)
                elif line.startswith("if"):
                    condition, action = line[3:].split("then", 1)
                    if eval(condition.strip(), {}, variables):
                        program.append(action.strip())
                elif line.startswith("goto"):
                    # Implement goto logic if needed
                    pass
                elif line.startswith("end"):
                    break
        elif command == "clear":
            os.system("cls")
        elif command == "save":
            filename = input("Enter the filename: ")
            with open(filename, "w") as file:
                for line in program:
                    file.write(line + "\n")
        elif command == "load":
            filename = input("Enter the filename: ")
            with open(filename, "r") as file:
                program = file.readlines()
        elif command == "new":
            program = []
        elif command == "edit":
            line_number = int(input("Enter the line number: "))
            line = input("Enter the line: ")
            program[line_number - 1] = line
        elif command == "delete":
            line_number = int(input("Enter the line number: "))
            del program[line_number - 1]
        else:
            if command.startswith("let"):
                var, expr = command[4:].split("=", 1)
                var = var.strip()
                expr = expr.strip()
                if expr.startswith("input"):
                    prompt = expr[6:].strip().strip("'")
                    variables[var] = input(prompt + ": ")
                else:
                    variables[var] = eval(expr, {}, variables)
            else:
                program.append(command)

if __name__ == "__main__":
    run()
