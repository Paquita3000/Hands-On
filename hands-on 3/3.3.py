import re

class CombinedParser:
    def __init__(self, input_string):
        token_pattern = r'\b(?:AND|OR|NOT)\b|[0-9]+|\(|\)|\+|\-|\*|\/'
        self.tokens = re.findall(token_pattern, input_string)
        self.pos = 0

    def parse(self):
        try:
            self.expr()
            return self.pos == len(self.tokens)
        except Exception:
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
        if self.current() == '(':
            self.next()
            self.expr()
            if self.current() != ')':
                raise Exception("Falta paréntesis de cierre")
            self.next()
        else:
            self.logical()

    def logical(self):
        self.term_l()
        while self.current() in ('AND', 'OR'):
            self.next()
            self.term_l()

    def term_l(self):
        if self.current() == 'NOT':
            self.next()
            self.factor_l()
        else:
            self.factor_l()

    def factor_l(self):
        token = self.current()
        if token == '(':
            self.next()
            self.expr()
            if self.current() != ')':
                raise Exception("Falta paréntesis de cierre")
            self.next()
        elif re.fullmatch(r'[0-9]+', token):
            self.next()
        else:
            raise Exception(f"Token inesperado en lógica: {token}")

    def current(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def next(self):
        self.pos += 1

def validar_expresion_combinada(expr):
    parser = CombinedParser(expr)
    if parser.parse():
        print(f"Entrada: {expr} -> Expresión válida")
    else:
        print(f"Entrada: {expr} -> Expresión inválida")

validar_expresion_combinada("(4 + 5) * (2 AND 1)")       # válida
validar_expresion_combinada("(2 AND 3) / (4 - 1")        # inválida
validar_expresion_combinada("NOT (3 + 2) OR 1")          # válida
validar_expresion_combinada("5 * NOT 1")                 # válida
validar_expresion_combinada("(1 OR 0) + 3")              # válida
