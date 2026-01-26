from dataclasses import dataclass
from typing import Any, List


@dataclass
class Node:
    """Representação de um nó AST"""

    def __repr__(self):
        return "Node()"


@dataclass
class MainNode(Node):
    """Nó principal da AST"""
    nodes: List[Node]

    def __repr__(self):
        return f"MainNode(\n  nodes={repr(self.nodes)}\n)"


@dataclass
class Literal(Node):
    """Representação de valores literais"""
    value: Any

    def __repr__(self):
        return f"Literal(value={repr(self.value)})"


class Identifier(Node):
    """Representação de identificadores"""

    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def __repr__(self):
        return f"Identifier(name={repr(self.name)})"


class VariableDeclarationNode(Node):
    """Representação de declarações de variáveis"""

    def __init__(self, identifier: Identifier, expression: Literal):
        super().__init__()
        self.identifier = identifier
        self.expression = expression

    def __repr__(self):
        return (
            f"VariableDeclarationNode(\n"
            f"  identifier={repr(self.identifier)},\n"
            f"  expression={repr(self.expression)}\n)"
        )


class AssignmentNode(Node):
    def __init__(self, identifier: Identifier, expression: Literal):
        self.identifier = identifier
        self.expression = expression

    def __repr__(self):
        return (
            f"AssignmentNode(\n"
            f"  identifier={repr(self.identifier)},\n"
            f"  expression={repr(self.expression)}\n)"
        )


class WriteStatementNode(Node):
    """Representação de instruções de escrita"""

    def __init__(self, expression):
        super().__init__()
        self.expression = expression

    def __repr__(self):
        return f"WriteStatementNode(expression={repr(self.expression)})"


class BinaryOperationNode(Node):
    """Representação de operações binárias (+ - * /)"""

    def __init__(self, left: Node, operator: str, right: Node):
        super().__init__()
        self.left = left
        self.operator = operator
        self.right = right

    def __repr__(self):
        return (
            f"BinaryOperationNode(\n"
            f"  left={repr(self.left)},\n"
            f"  operator={repr(self.operator)},\n"
            f"  right={repr(self.right)}\n)"
        )


class ConditionalStatementNode(Node):
    def __init__(
        self,
        left_expression: Identifier,
        operator: str,
        right_expression: Any,
        then_branch: List[Any],
        else_branch: List[Any] = None,
    ):
        self.left_expression = left_expression
        self.operator = operator
        self.right_expression = right_expression
        self.then_branch = then_branch
        self.else_branch = else_branch

    def __repr__(self):
        return (
            f"ConditionalStatementNode(\n"
            f"  left_expression={repr(self.left_expression)},\n"
            f"  operator={repr(self.operator)},\n"
            f"  right_expression={repr(self.right_expression)},\n"
            f"  then_branch={repr(self.then_branch)},\n"
            f"  else_branch={repr(self.else_branch)}\n)"
        )
