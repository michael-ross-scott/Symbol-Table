import copy


class TableEntry:
    variable = ""
    value = ""

    def __init__(self, variable, value):
        self.variable = variable
        self.value = value

    def getVariable(self):
        return self.variable

    def getValue(self):
        return self.value


class Table:
    table = []
    size = 5

    def getVariable(self,value):
        list = value.split(" ")
        return value[0]

    def __init__(self):
        for i in range(self.size):
            self.table.append([])

    def hashFunc(self, variable):
        hash_val = abs(hash(variable)) % 5
        return hash_val

    def insert(self, variable, var_value):
        index = self.hashFunc(variable)

        key = TableEntry(variable, var_value)
        chained_entries = self.table[index]

        if len(chained_entries) == 0:
            chained_entries.append(key)
        elif chained_entries[0].getVariable() == variable:
            chained_entries[0] = key
        else:
            length = len(chained_entries)
            for i in range(length):
                if chained_entries[i].getVariable() == variable:
                    chained_entries[i] = key
                    return
            chained_entries.append(key)

    def find(self, variable):
        if len(self.table) == 0:
            return False
        else:
            index = self.hashFunc(variable)
            chained_entries = self.table[index]
            if len(chained_entries) != 0:
                for i in chained_entries:
                    if i.getVariable() == variable:
                        return i.getValue()
            return False

    def clear(self):
        for i in range(len(self.table)):
            self.table[i] = []


class SymTable:
    list = []

    def __init__(self):
        self.list = []
        self.counter = 0
        self.sym_table = Table()

    def beginscope(self):
        if self.counter != 0:
            new_sym_table = copy.deepcopy(self.sym_table)
            self.list.append(new_sym_table)
        self.counter += 1
        return "beginscope"

    def endscope(self):
        if self.counter > 1:
            self.sym_table = self.list.pop()
        else:
            self.sym_table.clear()
        self.counter -= 1
        return "endscope"

    def define(self, variable, value):
        self.sym_table.insert(variable, value)
        return "define " + variable + " " + value

    def use(self, variable):
        value = self.sym_table.find(variable)
        if value == False:
            return "use " + variable + " = undefined"
        else:
            return "use " + variable + " = " + value



