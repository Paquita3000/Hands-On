import ply.lex as lex

tokens = (
    'INT', 'RETURN', 'ID', 'NUMBER',
)

reserved = {
    'int': 'INT',
    'return': 'RETURN'
}

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t\n'

def t_error(t):
    print(f"Caracter ilegal: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

if __name__ == "__main__":
    with open("codigo1.txt", "r") as file:
        data = file.read()
    lexer.input(data)
    for tok in lexer:
        print(tok)
        
