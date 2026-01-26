from dataclasses import dataclass
import re

# Definição dos tipos de tokens
TOKEN_TYPE = {
    # Keywords
    "VARIABLE": re.compile(r'variable', re.IGNORECASE),
    "WRITE": re.compile(r'write', re.IGNORECASE),
    "IF": re.compile(r'if', re.IGNORECASE),
    "THEN": re.compile(r'then', re.IGNORECASE),
    "ELSE": re.compile(r'else', re.IGNORECASE),
    "END": re.compile(r'end', re.IGNORECASE),

    # Operadores de comparação
    "EQ": re.compile(r'=='),
    "NEQ": re.compile(r'!='),
    "LTE": re.compile(r'<='),
    "GTE": re.compile(r'>='),
    "LT": re.compile(r'<'),
    "GT": re.compile(r'>'),
    "ASSIGN": re.compile(r'='),

    # Literais
    "LITERAL": re.compile(r'"[^"]*"'),
    "NUMBER": re.compile(r'\d+'),

    # Operadores
    "OPERATOR": re.compile(r'[+\-*/]'),

    # Identificadores
    "IDENTIFIER": re.compile(r'[a-zA-Z_]\w*', re.IGNORECASE),
}

# Regex dinâmico
TOKEN_MATCH = re.compile('|'.join(
    f'(?P<{key}>{pattern.pattern})' for key, pattern in TOKEN_TYPE.items()))


@dataclass
class Token:
    """
    Especificação de tipo de token
    """
    type: str
    value: str
    position: int
    end: int


class Tokenizer:
    def __init__(self, source_code: str):
        self.source_code = source_code
        self.tokens = []
        self.position = 0

        # Inicia o processo de tokenização
        self.eat()

    def advance(self):
        """
        Avança para próxima posição
        """
        self.position += 1

    def eat(self):
        """
        Verifica e define tipos de tokens
        """
        while self.position < len(self.source_code):
            match = TOKEN_MATCH.match(self.source_code, self.position)

            # Verifica se encontrou um token válido
            if match and match.lastgroup in TOKEN_TYPE.keys():
                # Avança o ponteiro
                self.position = match.end()

                # Cria o novo token e adiciona a lista
                token = Token(
                    type=match.lastgroup,
                    value=match.group(match.lastgroup),
                    position=match.start(),
                    end=match.end(),
                )
                self.tokens.append(token)

            # Avança para a próxima posição da string
            self.advance()


# DEBUG
if __name__ == "__main__":
    code = "if 2 == 5 then write \"Then Executado\" else write \"Else Executado!\" end"
    tokenizer = Tokenizer(code)

    print(30 * "=", "Código Fonte", 30 * "=")
    print(code)

    print(30 * "=", "Tokens Gerados", 30 * "=")
    for tok in tokenizer.tokens:
        print(tok)
