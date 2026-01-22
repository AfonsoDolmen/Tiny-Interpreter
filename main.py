from tokenizer import Tokenizer
from parser import Parser
from interpreter import Interpreter


class Program:
    def __init__(self, source_code: str):
        self.env = dict()
        self.tokenizer = Tokenizer(source_code)
        self.parser = Parser(self.tokenizer.tokens)

    def run(self):
        """
        Realiza a execução do programa
        """
        root = self.parser.parse_program()
        interpreter = Interpreter(root)

        # Executa a AST
        interpreter.execute()


if __name__ == "__main__":
    """
    variables: declara variáveis
    write: imprime valores
    op: realiza operações aritméticas básicas e atribui o resultado na variável da esquerda (+ - * /)

    Ex: variable x = 10 variable y = 2 write x write y op x + y
    """
    program = Program(
        """
        variable x = 5 + 5
        variable y = 10
        variable result = x * y

        write "O resultado de x * y:"
        write result
        write "Finalizando..."
        """
    )

    program.run()
