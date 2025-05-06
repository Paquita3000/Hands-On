import ply.lex as lex

tokens = (
    'INT', 'RETURN', 'ID', 'NUMBER','OPERATOR', 'DELIMITER', 'STRING', 'COMMENT'
)

reserved = {
    'int': 'INT',
    'return': 'RETURN'
}

def t_OPERATOR(t):
    r'[+\-*/=<>]'
    return t

def t_STRING(t):
    r'"([^"\\]|\\.)*"'
    return t

def t_COMMENT(t):
    r'//.*|/\*[\s\S]*?\*/'
    pass

def t_DELIMITER(t):
    r'[{}();,]'
    return t

def t_ID(t):
    r'[a-zA-ZáéíóúÁÉÍÓÚñÑ_][a-zA-Z0-9áéíóúÁÉÍÓÚñÑ_]*'
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
    with open("codigo3.txt", "r", encoding="utf-8") as file:
        data = file.read()
    lexer.input(data)
    counts = {token: 0 for token in tokens}
    for tok in lexer:
        counts[tok.type] += 1
        print(tok)
    print(counts)
    