# Tiny Interpreter

Tiny Interpreter é um pequeno interpretador escrito em Python, desenvolvido com fins educacionais.
O projeto implementa as principais etapas de um interpretador, incluindo:

- Tokenização do código-fonte (lexer);
- Parser para estruturação das instruções;
- Construção e execução de uma AST (Árvore de Sintaxe Abstrata).

Atualmente, a linguagem permite:
- Declaração de variáveis;
- Atribuição de valores;
- Impressão de valores literais ou armazenados em variáveis;
- Operações aritméticas simples;
- Estrutura condicional simples (if/else);

--------------------------------------------------

## Como utilizar

1. Edite o paramêtro da instância de Program em main.py:
```python
program = Program("""Seu código aqui""")
```

#### 1.1 Exemplo 2:
```text
variable x = 10
write x
```
```text
Saída esperada: 10
```

#### 1.2 Exemplo 2:
```text
variable a = 10
variable b = 20

variable result = a + 10

if result == b then write "Variável result é igual b!" else write "Não são iguais" end
```
```text
Saída esperada:

Variável result é igual b!
```

2. Execute o interpretador:
```
python main.py
```

--------------------------------------------------

## TODO

- Avaliação baseada em expressões; ✅
- Precedência de operadores;
- Estruturas condicionais simples e compostas (if / else if / else) - 50% implementado😅;
- Refatoração e simplificação da AST; ✅
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
