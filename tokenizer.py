from dataclasses import dataclass
import re

# Definição dos tipos de tokens
TOKEN_TYPE = {
    "VARIABLE": re.compile(r'variable', re.IGNORECASE),
    "WRITE": re.compile(r'write', re.IGNORECASE),
    "OP": re.compile(r'op', re.IGNORECASE),
    "NUMBER": re.compile(r'\d+'),
    "LITERAL": re.compile(r'"[^"]*"'),
    "OPERATOR": re.compile(r'[+\-*/=]'),
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
                    position=match.start()
                )
                self.tokens.append(token)

            # Avança para a próxima posição da string
            self.advance()


# DEBUG
if __name__ == "__main__":
    code = "variable x = 10 op x + 10"
    tokenizer = Tokenizer(code)

    print(30 * "=", "Código Fonte", 30 * "=")
    print(code)

    print(30 * "=", "Tokens Gerados", 30 * "=")
    for tok in tokenizer.tokens:
        print(tok)
