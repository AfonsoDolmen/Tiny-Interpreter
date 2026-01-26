from tokenizer import Tokenizer
from parser import Parser
from interpreter import Interpreter


class Program:
    def __init__(self, source_code: str):
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
    if <expressão> <operador> <expressão> then ... else end

    Ex: variable x = 10 variable y = 2 write x write y op x + y
    """
    program = Program(
        """
        write "Bem vindo a minha linguagem!"

        variable x = 10
        variable y = 10
        variable result = x * 2

        write "Valor de x: "
        write x
        
        write "Valor de y: "
        write y

        write "Valor de x * y:"
        write result

        if result > y then write "O resultado é maior que y!" else write "O resultado é menor que y" end
        """
    )

    program.run()
