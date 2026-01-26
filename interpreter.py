from typing import List

from nodes import (
    Node,
    MainNode,
    Literal,
    Identifier,
    VariableDeclarationNode,
    AssignmentNode,
    WriteStatementNode,
    BinaryOperationNode,
    ConditionalStatementNode,
)


class Interpreter:
    def __init__(self, root: MainNode):
        self.root = root
        self.env = {}

    def execute(self, root: List[Node] = None):
        """
        Executa a árvore de sintaxe abstrata (AST)
        """
        root = root or self.root
        nodes = getattr(root, 'nodes', root)

        for node in nodes:
            # Verifica os tipo de nó
            if isinstance(node, VariableDeclarationNode):
                self.declare_variable(node)
            elif isinstance(node, AssignmentNode):
                self.assignment_operation(node)
            elif isinstance(node, WriteStatementNode):
                self.write_statement(node)
            elif isinstance(node, BinaryOperationNode):
                self.operation_statement(node)
            elif isinstance(node, ConditionalStatementNode):
                self.conditional_statement(node)

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

    def assignment_operation(self, node: AssignmentNode):
        """
        Atribuição de valores
        """
        identifier = node.identifier.name
        value = self.evaluate(node.expression)

        if identifier not in self.env:
            raise NameError(f'Variável \"{identifier}\" não declarada!')

        self.env[identifier] = value

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

    def conditional_statement(self, node: ConditionalStatementNode):
        """
        Executa bloco condicional simples (if/else)
        """
        left_expr = self.evaluate(node.left_expression)
        operator = node.operator
        right_expr = self.evaluate(node.right_expression)

        # Operadores possíveis
        operators = {
            '==': lambda a, b: a == b,
            '!=': lambda a, b: a != b,
            '<=': lambda a, b: a <= b,
            '>=': lambda a, b: a >= b,
            '<': lambda a, b: a < b,
            '>': lambda a, b: a > b,
        }

        if operator not in operators:
            raise SyntaxError(f'Operador {operator} inválido!')

        # Caso o operador seja correto, executa o bloco responsável
        if operators[operator](left_expr, right_expr) and node.then_branch:
            self.execute(node.then_branch)
        else:
            self.execute(node.else_branch)


# DEBUG
if __name__ == "__main__":
    from tokenizer import Tokenizer
    from parser import Parser

    code = """
    variable x = 10
    variable y = 10

    write x
    write y
    
    x = 10 + 10

    if x == 20 then write "x é igual a 20" else write "x não é igual a 20" end
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
