class Node:
    def __init__(self, type: str, value=None, nodes=None):
        self.type = type
        self.value = value
        self.nodes = list(nodes) if nodes is not None else []

    def __repr__(self):
        return f"Node(type={self.type}, value={self.value}, nodes={self.nodes})"


class Parser:
    @staticmethod
    def parse(tokens, root=None):
        """
        Monta a árvore de sintaxe abstrata (AST)
        """
        # Cria o node principal se não existir
        if not root:
            root = Node("MainNode")

        for pos, token in enumerate(tokens):
            # Verifica os tipos de tokens
            if token.type == "VARIABLE":
                keyword = token.value
                identifier = tokens[pos + 1] if pos + 1 < len(tokens) else None
                value = tokens[pos + 3] if pos + 3 < len(tokens) else None

                root.nodes.append(Node(
                    "VariableDeclaration",
                    value=keyword,
                    nodes=[
                        Node("IdentifierNode", value=identifier.value),
                        Node("ValueNode", value=value.value)
                    ]
                ))

            elif token.type == "WRITE":
                keyword = token.value
                value = tokens[pos + 1] if pos + 1 < len(tokens) else None

                root.nodes.append(Node(
                    "WriteStatement",
                    value=keyword,
                    nodes=[Node("ValueNode", value=value.value) if value.type == "NUMBER" else Node(
                        "IdentifierNode", value=value.value)]
                ))
            elif token.type == "OP":
                keyword = token.value
                left = tokens[pos + 1] if pos + 1 < len(tokens) else None
                operator = tokens[pos + 2] if pos + 2 < len(tokens) else None
                right = tokens[pos + 3] if pos + 3 < len(tokens) else None

                root.nodes.append(Node(
                    "OperationStatement",
                    value=keyword,
                    nodes=[
                        Node("ValueNode", value=left.value) if left.type == "NUMBER" else Node(
                            "IdentifierNode", value=left.value),
                        Node("OperatorNode", value=operator.value),
                        Node("ValueNode", value=right.value) if right.type == "NUMBER" else Node(
                            "IdentifierNode", value=right.value)
                    ]
                ))

        return root


# DEBUG
if __name__ == "__main__":
    from tokenizer import Tokenizer

    code = "variable x = 10 write x op x + 10"
    tokenizer = Tokenizer(code)

    root = Parser.parse(tokenizer.tokens)

    print(f'\nCódigo fonte: "{code}"\n')
    print(root)
