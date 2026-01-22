from nodes import (
    MainNode,
    Literal,
    Identifier,
    VariableDeclarationNode,
    WriteStatementNode,
    BinaryOperationNode,
)


class Interpreter:
    def __init__(self, root: MainNode):
        self.root = root
        self.env = {}

    def execute(self):
        """
        Executa a árvore de sintaxe abstrata (AST)
        """
        for node in self.root.nodes:
            # Verifica os tipo de nó
            if isinstance(node, VariableDeclarationNode):
                self.declare_variable(node)
            elif isinstance(node, WriteStatementNode):
                self.write_statement(node)
            elif isinstance(node, BinaryOperationNode):
                self.operation_statement(node)

    def declare_variable(self, node: VariableDeclarationNode):
        """
        Declaração de variáveis
        """
        identifier = node.identifier
        expression = node.expression

        # Verifica se a variável já foi criada
        if self.env.get(identifier.name, None):
            raise NameError(f'{identifier.name} já foi declarada!')

        # Realiza a atribuição de acordo com a expressão
        if isinstance(expression, BinaryOperationNode):
            self.env[identifier.name] = self.evaluate(expression)
        elif isinstance(expression, Literal):
            self.env[identifier.name] = expression.value

    def write_statement(self, node: WriteStatementNode):
        """
        Executa a instrução de escrita
        """
        expression = node.expression

        if isinstance(expression, BinaryOperationNode):
            print(self.evaluate(expression))
        elif isinstance(expression, Identifier):
            if not self.env.get(expression.name, None):
                raise ValueError(f'Variável {expression.name} não declarada!')

            print(self.env[str(expression.name)])
        else:
            print(expression.value)

    def operation_statement(self, node: BinaryOperationNode):
        """
        Executa a instrução de cálculo
        """
        left_identifier = None

        result = self.evaluate(node)

        if isinstance(node.left, Identifier):
            left_identifier = node.left

        if left_identifier:
            self.env[left_identifier.name] = result

    def evaluate(self, node):
        """
        Avalia as expressões e retorna o resultado
        """
        left = node.left
        operator = node.operator
        right = node.right

        # Avalia o tipo
        if isinstance(left, BinaryOperationNode):
            # Se for uma expressão binária, avalie novamente
            left = self.evaluate(left)
        if isinstance(right, BinaryOperationNode):
            right = self.evaluate(right)

        # Caso for um identificador
        if isinstance(left, Identifier):
            left = self.env[left.name]
        if isinstance(right, Identifier):
            right = self.env[right.name]

        # Caso for valores
        if isinstance(left, Literal):
            left = left.value

        if isinstance(right, Literal):
            right = right.value

        # Realiza a operação
        match operator:
            case '+': return left + right
            case '-': return left - right
            case '*': return left * right
            case '/': return left // right

        return None


# DEBUG
if __name__ == "__main__":
    from tokenizer import Tokenizer
    from parser import Parser

    code = "variable x = 10 op x + 10 write x"

    tokenizer = Tokenizer(code)
    parser = Parser(tokenizer.tokens)
    root = parser.parse_program()

    print(f'\nCódigo fonte: "{code}"\n')
    print("Árvore de Sintaxe Abstracta (AST):")
    print(root)

    print("\nSaída da Execução:")
    interpreter = Interpreter(root)
    interpreter.execute()
