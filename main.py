include #!/usr/bin/python
import sys
import table
sym_table = table.SymTable()


def executeInstructions(instruction):
    list = instruction.split(" ")
    if list[0] == "beginscope":
        print(sym_table.beginscope())
    elif list[0] == "endscope":
        print(sym_table.endscope())
    elif list[0] == "define":
        variable = list[1]
        value = list[2]
        print(sym_table.define(variable, value))
    elif list[0] == "use":
        variable = list[1]
        print(sym_table.use(variable))


def main():
    file = open(sys.argv[1])
    lines = file.readlines()
    for i in lines:
        executeInstructions(i[:-1])


main()
