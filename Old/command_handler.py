import sys
from utils import Buffer, Variables

class CommandHandler:
    def __init__(self):
        self.program = []
        self.variables = Variables()
        self.buffer = Buffer()

    def handle_command(self, command):
        if command == "help":
            self.show_help()
        elif command == "list":
            self.list_program()
        elif command == "run":
            self.run_program()
        elif command == "save":
            self.save_program()
        elif command == "load":
            self.load_program()
        elif command == "new":
            self.program = []
        elif command == "edit":
            self.edit_program()
        elif command == "delete":
            self.delete_program()
        else:
            self.program.append(command)

    def show_help(self):
        print("Esta é minha pequenha linguagem de programação baseada em BASIC")
        print("You can use the following commands:")
        print("1. print - Exibe uma mensagem na tela (Exemplo: print 'Hello, World!')")
        print("2. input - Recebe um valor do usuario (Exemplo: input 'Qual seu nome ')")
        print("3. let - Salva um valor a uma variavel (Exemplo: let x = 10)")
        print("4. if - Condição (Exemplo if x > 10 then print 'x e maior que 10')")
        print("5. goto - Vai para uma linha especifica (Exemplo: goto 10)")
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
        print("16. for - Loop (Exemplo: for i = 1 to 10 do print i endfor)")

    def list_program(self):
        for line in self.program:
            print(line)

    def run_program(self):
        i = 0
        while i < len(self.program):
            line = self.program[i]
            if line.startswith("print"):
                self.handle_print(line)
            elif line.startswith("input"):
                self.handle_input(line)
            elif line.startswith("let"):
                self.handle_let(line)
            elif line.startswith("if"):
                self.handle_if(line)
            elif line.startswith("goto"):
                self.handle_goto(line)
            elif line.startswith("end"):
                break
            elif line.startswith("for"):
                self.handle_for(line)
            i += 1

    def handle_print(self, line):
        expr = line[6:].strip()
        if expr in self.variables.data:
            print(self.variables.data[expr])
        else:
            print(eval(expr, {}, self.variables.data))

    def handle_input(self, line):
        var = line[6:].strip()
        value = input(var + ": ")
        self.variables.data[var] = value

    def handle_let(self, line):
        var, expr = line[4:].split("=", 1)
        var = var.strip()
        expr = expr.strip()
        self.variables.data[var] = eval(expr, {}, self.variables.data)

    def handle_if(self, line):
        condition, action = line[3:].split("then", 1)
        if eval(condition.strip(), {}, self.variables.data):
            self.program.append(action.strip())

    def handle_goto(self, line):
        # Implement goto logic if needed
        pass

    def handle_for(self, line):
        parts = line[4:].split()
        var = parts[0]
        start = int(parts[2])
        end = int(parts[4])
        body = " ".join(parts[6:-1])
        self.buffer.append(body)
        for value in range(start, end + 1):
            self.variables.data[var] = value
            for buf_line in self.buffer.lines:
                if buf_line.startswith("print"):
                    self.handle_print(buf_line)
                elif buf_line.startswith("input"):
                    self.handle_input(buf_line)
                elif buf_line.startswith("let"):
                    self.handle_let(buf_line)
                elif buf_line.startswith("if"):
                    self.handle_if(buf_line)
                elif buf_line.startswith("goto"):
                    self.handle_goto(buf_line)
                elif buf_line.startswith("end"):
                    break
        self.buffer.clear()

    def save_program(self):
        filename = input("Digite o nome do arquivo: ")
        with open(filename, "w") as file:
            for line in self.program:
                file.write(line + "\n")

    def load_program(self):
        filename = input("Digite o nome do arquivo: ")
        with open(filename, "r") as file:
            self.program = file.readlines()

    def edit_program(self):
        line_number = int(input("Digite o numero da linha: "))
        line = input("Digite o numero da linha: ")
        self.program[line_number - 1] = line

    def delete_program(self):
        line_number = int(input("Digite o numero da linha: "))
        del self.program[line_number - 1]