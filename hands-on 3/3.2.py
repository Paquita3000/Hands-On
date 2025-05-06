import re

class LogicalParser:
    def __init__(self, input_string):
        token_pattern = r'\b(?:AND|OR|NOT)\b|[01]|\(|\)'
        self.tokens = re.findall(token_pattern, input_string)
        self.pos = 0

    def parse(self):
        try:
            self.expr()
            return self.pos == len(self.tokens)
        except:
            return False

    def expr(self): 
        self.or_expr()

    def or_expr(self): 
        self.and_expr()
        while self.current() == 'OR':
            self.next()
            self.and_expr()

    def and_expr(self): 
        self.not_expr()
        while self.current() == 'AND':
            self.next()
            self.not_expr()

    def not_expr(self):
        if self.current() == 'NOT':
            self.next()
            self.not_expr()
        else:
            self.factor()

    def factor(self):  
        token = self.current()
        if token == '(':
            self.next()
            self.expr()
            if self.current() != ')':
                raise Exception("Missing closing parenthesis")
            self.next()
        elif token in ('0', '1'):
            self.next()
        else:
            raise Exception(f"Unexpected token: {token}")

    def current(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def next(self):
        self.pos += 1

def validar_expresion_logica(expr):
    parser = LogicalParser(expr)
    if parser.parse():
        print(f"Entrada: {expr} -> Expresión válida")
    else:
        print(f"Entrada: {expr} -> Expresión inválida")

validar_expresion_logica("(1 AND 0) OR (NOT 1)")     #valida
validar_expresion_logica("(1 AND (0 OR 1)")          #invalida
validar_expresion_logica("NOT (0 OR 1) AND 1")       #valida
validar_expresion_logica("1 OR OR 0")                #invalida
validar_expresion_logica("NOT NOT 1")                #valida
