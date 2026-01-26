from typing import List

from tokenizer import Token

from nodes import (
    MainNode,
    VariableDeclarationNode,
    AssignmentNode,
    WriteStatementNode,
    BinaryOperationNode,
    Identifier,
    Literal,
    ConditionalStatementNode,
)


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.root = MainNode(nodes=[])
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

    def backward(self):
        """
        Retrocede o ponteiro para o token anterior
        """
        token = self.current_token()
        self.pos -= 1
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

    def expect_any(self, types: List[str]):
        """
        Verifica vários tipos de tokens
        """
        current_token = self.current_token()

        if current_token.type in types:
            return self.advance()
        else:
            raise SyntaxError(
                f'Esperado {types}. Mas foi especificado {current_token.type}')

    def parse_program(self):
        """
        Inicia o parsing
        """
        # Loop principal
        while self.pos < len(self.tokens):
            node = self.evaluate_token()

            if not isinstance(node, Token):
                self.root.nodes.append(node)

        return self.root

    def evaluate_token(self):
        """
        Avalia o tipo do token
        """
        token = self.current_token()

        match token.type:
            case "VARIABLE": return self.variable_declaration()
            case "WRITE": return self.write_statement()
            case "ASSIGN": return self.assign_operator()
            case 'IF': return self.conditional_statement()
            case _: return self.advance()

    def variable_declaration(self):
        """
        Verifica a gramática de declaração de variável
        variable <IDENTIFIER> = <EXPRESSION>
        """
        self.excpect("VARIABLE")

        identifier = self.excpect("IDENTIFIER")

        self.excpect("ASSIGN")

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

    def assign_operator(self):
        """
        Verifica a gramática de atribuição

        <IDENTIFIER> = <EXPRESSION>
        """
        self.backward()
        identifier = self.excpect('IDENTIFIER')

        self.advance()

        expression = self.parse_expression()

        return AssignmentNode(
            identifier=Identifier(identifier.value),
            expression=expression,
        )

    def conditional_statement(self):
        """
        Verifica a gramática de condicionais

        if <EXPRESSION> <OPERATOR> <EXPRESSION> then
        """
        # Blocos if/else
        true_branch = []
        else_branch = []

        self.excpect('IF')

        left_expr = self.parse_expression()
        operator = self.expect_any(['EQ', 'NEQ', 'LTE', 'GTE', 'LT', 'GT'])
        right_expr = self.parse_expression()

        self.excpect('THEN')

        current_branch = true_branch

        # Atribui o nó ao seu bloco responsável
        while self.current_token().type != 'END':
            if self.current_token().type == 'ELSE':
                self.advance()
                current_branch = else_branch
                continue

            node = self.evaluate_token()

            if node:
                current_branch.append(node)

        self.advance()

        # Retorna o nó de estrutura condicional
        return ConditionalStatementNode(
            left_expression=left_expr,
            operator=operator.value,
            right_expression=right_expr,
            then_branch=true_branch,
            else_branch=else_branch if else_branch else None,
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

    code = "if 5 == 2 then variable x = 2 write x else write \"Não é igual\" end"

    tokenizer = Tokenizer(code)
    parser = Parser(tokenizer.tokens)

    print(parser.parse_program())

    print(f'\nCódigo fonte: "{code}"\n')
