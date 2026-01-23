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
            raise NameError(
                f'Variável \"{identifier.name}\" já foi declarada!')

        # Realiza a atribuição de acordo com a expressão
        self.env[identifier.name] = self.evaluate(expression)

    def write_statement(self, node: WriteStatementNode):
        """
        Executa a instrução de escrita
        """
        print(self.evaluate(node.expression))

    def operation_statement(self, node: BinaryOperationNode):
        """
        Executa a instrução de cálculo
        """
        return self.evaluate(node)

    def evaluate(self, node):
        """
        Avalia os tipos e expressões, retorna o valor
        """
        # Avalia o tipo
        if isinstance(node, Literal):
            return node.value

        if isinstance(node, Identifier):
            if node.name in self.env:
                return self.env[node.name]
            raise NameError(f'Variável \"{node.name}\" não foi declarada!')

        if isinstance(node, BinaryOperationNode):
            left = self.evaluate(node.left)
            operator = node.operator
            right = self.evaluate(node.right)

            # Realiza a operação
            match operator:
                case '+': return left + right
                case '-': return left - right
                case '*': return left * right
                case '/':
                    if right != 0:
                        return left // right
                    else:
                        raise ZeroDivisionError("Divisão por zero!")

                case _: raise ValueError(f'Operador {operator} inválido!')

        return None


# DEBUG
if __name__ == "__main__":
    from tokenizer import Tokenizer
    from parser import Parser

    code = """
    variable x = 10
    write "Teste"
    write 10 + 5 - 2 * 3
    """

    tokenizer = Tokenizer(code)
    parser = Parser(tokenizer.tokens)
    root = parser.parse_program()

    print(f'\nCódigo fonte: "\n{code}\n"\n')
    print("Árvore de Sintaxe Abstracta (AST):")
    print(root)

    print("\nSaída da Execução:")
    interpreter = Interpreter(root)
    interpreter.execute()
