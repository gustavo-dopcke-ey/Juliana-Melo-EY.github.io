==================================
Formas de Documentar Código
==================================


==========
Code Block
==========

Como já mencionado anteriormente, existem duas formas de documentar código, uma delas é usando code blocks.

Code block consiste num bloco de código em que podemos escolher a linguagem e a documentação mostrará o código formatado de acordo com as especificidades da linguagem.

Para criar code blocks usaremos os seguintes comandos::

    .. code-block:: linguagem do código
        :linenos:

Depois é só colocar o código seguindo a identação de **:linenos:**

O exemplo abaixo usa code block para documentar um código python.

.. code-block:: python
    :linenos:

    from typing import Iterator

    # This is an example
    class Math:
        @staticmethod
        def fib(n: int) -> Iterator[int]:
            """Fibonacci series up to n"""
            a, b = 0, 1
            while a < n:
                yield a
                a, b = b, a + b


    result = sum(Math.fib(42))
    print("The answer is {}".format(result))


Code Block com legenda
======================

O processo é basicamente o mesmo que o detalhado acima, a única diferença é que inserimos o parametro ``:caption::``::

    .. code-block:: json
        :caption: Code Blocks com legenda.




.. code-block:: json
    :caption: Code Blocks com legenda.

    {
      "session_name": "shorthands",
      "windows": [
        {
          "panes": [
            {
              "shell_command": "echo 'This is an intentionally very long line because I want to make sure that we are handling scrollable code blocks correctly.'"
            }
          ],
          "window_name": "long form"
        }
      ]
    }


Linhas Destacadas
========================

Para ter um code block com linhas destacadas, é necessário usar o seguinte parâmetro ``:emphasize-lines: (número das linhas a serem destacadas)``::

    .. code-block:: python
        :linenos:
        :emphasize-lines: 3,5

.. code-block:: python
    :linenos:
    :emphasize-lines: 3,5

    def some_function():
        interesting = False
        print("This line is highlighted.")
        print("This one is not...")
        print("...but this one is.")
        print(
            "This is an intentionally very long line because I want to make sure that we are handling scrollable code blocks correctly."
        )


A segunda forma de documentar códicos é através da geração automática, logo, com o Sphinx é possível documentar funções, classes e métodos do seu código uma única vez e gerar uma documentação completa a partir disso.

==================
Geração Automática
==================

Antes de mais nada, é importante verificar se a extensão *sphinx.ext.autodoc* foi colocada no arquivo **conf.py**. Uma vez que o arquivo de configuração possui a extensão, a geração automática já pode ser feita.


O código que será documentado precisa seguir o seguinte padrão de comentário:

.. code-block:: python
    :linenos:

    def calculate_sum(a, b):
    """
    This function calculates the sum of two numbers.

    :param a: The first number.
    :type a: int
    :param b: The second number.
    :type b: int
    :return: The sum of the two numbers.
    :rtype: int
    :example:

    >>> calculate_sum(2, 3)
    5
    >>> calculate_sum(0, 0)
    0
    >>> calculate_sum(-1, 1)
    0
    """
    return a + b

Na geração automática é possível documentar funções, classes e módulos.


O parâmetro **automodule** é usado para importar um módulo do seu código e documentar todas as funções, classes e métodos dentro dele. Para usá-la, basta adicionar a seguinte linha à sua documentação RST::

    .. automodule:: module_name


O parâmetro **autoclass** é usado para documentar uma classe específica. Para usá-la, basta adicionar a seguinte linha à sua documentação RST::

    .. autoclass:: class_name


O parâmetro **autofunction** é usado para documentar uma função específica. Para usá-la, basta adicionar a seguinte linha à sua documentação RST::


    .. autofunction:: function_name

O arquivo.py que será documentado precisa estar fora do  diretório **Sphinx**, por isso é aconselhada a criação de um novo diretório. Nesse diretório ficará a pasta **Sphinx** com todos os arquivos de sua documentação e os códigos que serão lidos através do autodoc

No exemplo abaixo vemos a documentação do módulo **my_module**:

.. automodule:: my_module
   :members:



