import re

class Parser:
    def __init__(self, input_string):
        self.tokens = re.findall(r'\d+|[()+\-*/]', input_string.replace(' ', ''))
        self.pos = 0

    def parse(self):
        try:
            self.expr()
            if self.pos < len(self.tokens):
                return False
            return True
        except:
            return False

    def expr(self):
        self.term()
        while self.current() in ('+', '-'):
            self.next()
            self.term()

    def term(self):
        self.factor()
        while self.current() in ('*', '/'):
            self.next()
            self.factor()

    def factor(self):
        token = self.current()
        if token is None:
            raise Exception("Unexpected end of input")
        if token == '(':
            self.next()
            self.expr()
            if self.current() != ')':
                raise Exception("Missing closing parenthesis")
            self.next()
        elif re.fullmatch(r'\d+', token):
            self.next()
        else:
            raise Exception(f"Unexpected token: {token}")

    def current(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def next(self):
        self.pos += 1

def validar_expresion(expr):
    parser = Parser(expr)
    if parser.parse():
        print(f"Entrada: {expr} -> Expresión válida")
    else:
        print(f"Entrada: {expr} -> Expresión inválida")


validar_expresion("(4 + 5) * 2")
validar_expresion("3 - (2 + )")
validar_expresion("7 / (3 - 3")     
validar_expresion("2 + 3 *")     
validar_expresion("10 + (2 * 3)")  