from dataclasses import dataclass
from typing import Any, List


@dataclass
class Node:
    """
    Representação de um nó AST
    """

    def __repr__(self):
        return f"Node()"


@dataclass
class MainNode(Node):
    """
    Nó principal da AST
    """
    nodes: List[Node]


@dataclass
class Literal(Node):
    """
    Represemtação de valores literais
    """
    value: Any

    def __repr__(self):
        return f'Literal(value={self.value})'


class Identifier(Node):
    """
    Representação de identificadores
    """

    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def __repr__(self):
        return f'Identifier(name={self.name})'


class VariableDeclarationNode(Node):
    """
    Representação de declarações de variáveis
    """

    def __init__(self, identifier: Identifier, expression: Literal):
        super().__init__()
        self.identifier = identifier
        self.expression = expression

    def __repr__(self):
        return f'VariableDeclarationNode(identifier={self.identifier}, expression={self.expression})'


class WriteStatementNode(Node):
    """
    Representação de instruções de escrita
    """

    def __init__(self, expression):
        super().__init__()
        self.expression = expression

    def __repr__(self):
        return f'WriteStatementNode(expression={self.expression})'


class BinaryOperationNode(Node):
    """
    Representação de operações binárias (+ - * /)
    """

    def __init__(self, left: Node, operator: str, right: Node):
        super().__init__()
        self.left = left
        self.operator = operator
        self.right = right

    def __repr__(self):
        return f'BinaryOperationNode(left={self.left}, operator={self.operator}, right={self.right})'
