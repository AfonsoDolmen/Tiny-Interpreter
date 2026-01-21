from tokenizer import Tokenizer
from parser import Parser
from interpreter import Interpreter


class Program:
    def __init__(self, source_code: str):
        self.env = dict()
        self.tokenizer = Tokenizer(source_code)

    def run(self):
        """
        Realiza a execução do programa
        """
        root = Parser.parse(self.tokenizer.tokens)
        Interpreter.execute(root, self.env)

        # Limpa as variáveis após a execução
        self.env.clear()


if __name__ == "__main__":
    """
    variables: declara variáveis
    write: imprime valores
    op: realiza operações aritméticas básicas (+ - * /)

    Ex: variable x = 10 variable y = 2 write x write y op x + y
    """
    program = Program(
        "variable x = 10 variable y = 20 write x write y op x + 50")
    program.run()
