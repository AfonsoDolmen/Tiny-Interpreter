from parser import Node


class Interpreter:
    @staticmethod
    def execute(root_node: Node, env: dict):
        """
        Executa a árvore de sintaxe abstrata (AST)
        """
        for node in root_node.nodes:
            # Verifica os tipos de Nodes
            if node.type == "VariableDeclaration":
                identifier_node = node.nodes[0]
                value_node = node.nodes[1]

                env[identifier_node.value] = int(value_node.value)

            elif node.type == "WriteStatement":
                if node.nodes == Node:
                    value_node = node.nodes
                else:
                    value_node = node.nodes[0]

                # Verifica se é apenas um valor ou uma variável
                if value_node.type == "ValueNode":
                    print(int(value_node.value))
                elif value_node.type == "IdentifierNode":
                    var_name = value_node.value
                    if var_name in env:
                        print(env[var_name])
                    else:
                        raise NameError(f"Variável '{var_name}' não definida.")

            elif node.type == "OperationStatement":
                left_node = node.nodes[0]
                operator_node = node.nodes[1]
                right_node = node.nodes[2]

                left_value = int(left_node.value) if left_node.type == "ValueNode" else env.get(
                    left_node.value, None)
                right_value = int(right_node.value) if right_node.type == "ValueNode" else env.get(
                    right_node.value, None)

                if not isinstance(left_value, int):
                    raise NameError(
                        f"Variável '{left_node.value}' não definida.")
                if not isinstance(right_value, int):
                    raise NameError(
                        f"Variável '{right_node.value}' não definida.")

                if operator_node.value == "+":
                    print(left_value + right_value)
                elif operator_node.value == "-":
                    print(left_value - right_value)
                elif operator_node.value == "*":
                    print(left_value * right_value)
                elif operator_node.value == "/":
                    print(left_value // right_value)


# DEBUG
if __name__ == "__main__":
    from tokenizer import Tokenizer
    from parser import Parser

    code = "variable x = 10 write x variable y = 10 op x + y"
    tokenizer = Tokenizer(code)
    root = Parser.parse(tokenizer.tokens)

    print(f'\nCódigo fonte: "{code}"\n')
    print("Árvore de Sintaxe Abstracta (AST):")
    print(root)

    print("\nSaída da Execução:")
    interpreter_env = dict()
    Interpreter.execute(root, interpreter_env)
