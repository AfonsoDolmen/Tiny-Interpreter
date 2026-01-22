from nodes import (
    MainNode,
    VariableDeclarationNode,
    WriteStatementNode,
    BinaryOperationNode,
    Identifier,
    Literal,
)


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current_token(self):
        """
        Retorna o token atual
        """
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def advance(self):
        """
        Avança para o próximo token
        """
        token = self.current_token()
        self.pos += 1
        return token

    def excpect(self, token_type):
        """
        Verifica o tipo do token esperado
        """
        token = self.current_token()

        if not token or token.type != token_type:
            raise SyntaxError(
                f'Token {token.type} inesperado. Você quis dizer {token_type}?')

        return self.advance()

    def parse_program(self):
        """
        Inicia o parsing
        """
        root = MainNode(nodes=[])
        token = self.current_token()

        # Loop principal
        while self.pos < len(self.tokens):
            token = self.current_token()
            if token.type == "VARIABLE":
                root.nodes.append(self.variable_declaration())
            elif token.type == "WRITE":
                root.nodes.append(self.write_statement())
            elif token.type == "OP":
                root.nodes.append(self.operation_statement())

        return root

    def variable_declaration(self):
        """
        Verifica a gramática de declaração de variável
        variable <IDENTIFIER> = <EXPRESSION>
        """
        self.excpect("VARIABLE")

        identifier = self.excpect("IDENTIFIER")

        self.excpect("OPERATOR")

        value = self.parse_expression()

        return VariableDeclarationNode(
            identifier=Identifier(identifier.value),
            expression=value
        )

    def write_statement(self):
        """
        Verifica a gramática de instrução de escrita
        write <EXPRESSION>
        """
        self.excpect("WRITE")

        value = self.parse_expression()

        return WriteStatementNode(
            expression=value
        )

    def operation_statement(self):
        """
        Verifica a gramática de operação
        op <term> <OPERATOR> <term>
        """
        self.excpect("OP")

        left = self.parse_term()
        operator = self.excpect("OPERATOR").value
        right = self.parse_term()

        return BinaryOperationNode(
            left=left,
            operator=operator,
            right=right
        )

    def parse_expression(self):
        """
        Parse de expressões (combinando termos e operadores)
        """
        # Inicia verificando o primeiro termo
        node = self.parse_term()

        # Enquanto houver operadores, constroi a expressão
        while self.current_token() and self.current_token().type == "OPERATOR":
            # Captura o operador
            operator = self.current_token().value

            # Avança e captura o próximo termo
            self.advance()
            right = self.parse_term()

            # Cria um nó de operação binária
            node = BinaryOperationNode(
                left=node, operator=operator, right=right)

        return node

    def parse_term(self):
        """
        Parse de termos (números, literais, identificadores)
        """
        # Captura o token atual
        token = self.current_token()

        # Verifica o tipo e retorna seu devido nó
        if token.type == "NUMBER":
            self.advance()
            return Literal(int(token.value))
        elif token.type == "LITERAL":
            self.advance()
            return Literal(token.value.strip('"'))
        elif token.type == "IDENTIFIER":
            self.advance()
            return Identifier(token.value)


# DEBUG
if __name__ == "__main__":
    from tokenizer import Tokenizer

    code = "variable x = 10 + 5 variable y = x + 10 write \"Valor de y: \" write y"

    tokenizer = Tokenizer(code)
    parser = Parser(tokenizer.tokens)

    print(parser.parse_program())

    print(f'\nCódigo fonte: "{code}"\n')
