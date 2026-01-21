# Tiny Interpreter

Tiny Interpreter é um pequeno interpretador escrito em Python, desenvolvido com fins educacionais.
O projeto implementa as principais etapas de um interpretador, incluindo:

- Tokenização do código-fonte (lexer);
- Parser para estruturação das instruções;
- Construção e execução de uma AST (Árvore de Sintaxe Abstrata).

Atualmente, a linguagem permite:
- Declaração de variáveis;
- Impressão de valores literais ou armazenados em variáveis;
- Operações aritméticas simples.

--------------------------------------------------

## Como utilizar

1. Edite a variável responsável por armazenar o código-fonte no arquivo principal:
```
code = "SEU CÓDIGO AQUI"
```

Exemplo

variable x = 10
write x

Saída esperada: 10

2. Execute o interpretador:
```
python main.py
```

--------------------------------------------------

## TODO

- Avaliação baseada em expressões;
- Estruturas condicionais simples e compostas (if / else if / else);
- Refatoração e simplificação da AST;
- Melhor tratamento de erros sintáticos e semânticos;
- Outros aprimoramentos conforme a evolução do projeto.

--------------------------------------------------

## Motivação

Sempre fui fascinado por tecnologia e por entender como as coisas funcionam “por baixo dos panos”.
Durante meus estudos sobre compiladores e interpretadores, surgiu a ideia de colocar esses conceitos em prática,
construindo um interpretador simples do zero, com foco em aprendizado e experimentação.

--------------------------------------------------

## Referências

Compiladores: Princípios, Técnicas e Ferramentas — Alfred V. Aho et al.
https://www.amazon.com.br/Compiladores-princ%C3%ADpios-ferramentas-Alfred-Aho/dp/8588639246

Crafting Interpreters
https://craftinginterpreters.com/representing-code.html

Abstract Syntax Tree — Wikipédia
https://en.wikipedia.org/wiki/Abstract_syntax_tree
