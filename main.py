class Parser:
    def __init__(self, input_string):
        self.input = input_string
        self.pos = 0

    def current_char(self):
        if self.pos < len(self.input):
            return self.input[self.pos]
        return None

    def read_char(self):
        if self.pos < len(self.input):
            ch = self.input[self.pos]
            self.pos += 1
            return ch
        return None

    def symb(self):
        """<Символ> ::= a | b | c | ..."""
        ch = self.current_char()
        if ch and ch.isalpha() and ch.islower():
            self.read_char()
            return True
        return False

    def operator(self):
        """<Оператор> ::= + | -"""
        ch = self.current_char()
        if ch in ('+', '-'):
            self.read_char()
            return True
        return False

    def brack_continuation(self):
        """<ПродолжениеСкобочное> ::= <Оператор><Символ><ПродолжениеСкобочное> | Ω"""
        while self.operator():
            if not self.symb():
                return False
        return True

    def brack_expression(self):
        """<СкобочноеВыражение> ::= <Символ><Оператор><Символ><ПродолжениеСкобочное>"""
        if self.symb() and self.operator() and self.symb():
            return self.brack_continuation()
        return False

    def continuation(self):
        """<Продолжение> ::= - <ПодВыражение2> | + <ПодВыражение1> | Ω"""
        ch = self.current_char()
        if ch == '-':
            self.read_char()
            return self.sub_expression2()
        elif ch == '+':
            self.read_char()
            return self.sub_expression1()
        return True

    def sub_expression1(self):
        """<ПодВыражение1> ::= <Символ><Продолжение>"""
        if self.symb():
            return self.continuation()
        return False

    def sub_expression2(self):
        """<ПодВыражение2> ::= <Символ><Продолжение> | (<СкобочноеВыражение>)<Продолжение>"""
        ch = self.current_char()
        if self.symb():
            return self.continuation()
        elif ch == '(':
            self.read_char()
            if self.brack_expression() and self.current_char() == ')':
                self.read_char()
                return self.continuation()
        return False

    def initial_continuation(self):
        """<ПродолжениеНачальное> ::= - <ПодВыражение2> | + <ПодВыражение1>"""
        ch = self.current_char()
        if ch == '-':
            self.read_char()
            return self.sub_expression2()
        elif ch == '+':
            self.read_char()
            return self.sub_expression1()
        return False

    def expression(self):
        """<Выражение> ::= <Символ><ПродолжениеНачальное>"""
        if self.symb():
            return self.initial_continuation()
        return False

    def parse(self):
        """Запуск парсера"""
        return self.expression() and self.pos == len(self.input)


# Пример использования
#input_string1 = "a-b-(c-d)+b+e-f"
#input_string2 = "a-(b+c+d)"
#input_string3 = "a-b+(c+d)"
#input_string4 = "(a+b)"
#input_string5 = "a+b+"
while True:
    input_string = input("Введите выражения (или F для завершения): ")
    if input_string == "F":
        break
    parser = Parser(input_string)
    if parser.parse():
        print(f"Выражение '{input_string}' корректно.")
    else:
        print(f"Выражение '{input_string}' некорректно.")
