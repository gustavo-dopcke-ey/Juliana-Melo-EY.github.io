==================================
Como Documentar Arquivos de Texto?
==================================
.. _como_documentar_texto:

Nessa página apresentamos os principais comandos necessários para documentar texto na Sphinx.

Edição de texto
===============

O arquivo.rst funciona como se fosse um bloco de notas, logo, para inserir texto basta colar ou escreve-lo no arquivo. Porém, além de inserir textos, também é possível formatá-lo.

A seguir, temos uma tabela com os principais comandos para formatação de texto, lembrando que uma explicação mais detalhada pode ser encontrada em https://docutils.sourceforge.io/docs/ref/rst/directives.html#image

==================================== ===========================================
Formato                              reStructuredText
==================================== ===========================================
**Negrito**                          .. code-block:: bash

                                        **Negrito**

*Itálico*                            .. code-block:: bash

                                        *Itálico*

``inline code``                      .. code-block:: bash

                                        ``inline code``

:sub:`subscript`                     .. code-block:: bash

                                        :sub:`subscript`

:sup:`superscript`                   .. code-block:: bash

                                        sup:`superscript`

:emphasis:`emphasis`                 .. code-block:: bash

                                        :emphasis:`emphasis`

:strong:`strong`                     .. code-block:: bash

                                        :strong:`strong`

:literal:`literal`                   .. code-block:: bash

                                        :literal:`literal`

.. centered:: teste                  .. code-block:: bash

                                        .. centered:: teste
==================================== ===========================================

Cálculos Matemáticos
====================

Podemos escrever cálculos matemáticos de duas formas na Sphinx, uma usando o comando :literal:`:math:``` e outra usando :literal:`..math::`, segue exemplos:

:math:`X_{0:5} = (X_0, X_1, X_2, X_3, X_4)`

Código::

    :math:`X_{0:5} = (X_0, X_1, X_2, X_3, X_4)`

.. math::
    :label: referencia

    \nabla^2 f =
    \frac{1}{r^2} \frac{\partial}{\partial r}
    \left( r^2 \frac{\partial f}{\partial r} \right) +
    \frac{1}{r^2 \sin \theta} \frac{\partial f}{\partial \theta}
    \left( \sin \theta \, \frac{\partial f}{\partial \theta} \right) +
    \frac{1}{r^2 \sin^2\theta} \frac{\partial^2 f}{\partial \phi^2}

Para ver o código da equação acima, clique em **View page source** no canto superior direito da página.


Também é possivel referenciar equações usando  :eq:`referencia` usando ``:eq:``.


Download de Links e Arquivos
============================

Na Sphinx também é possível inserir links com arquivos para download, usando ``:download:``

:download:`Link <https://source.unsplash.com/200x200/daily?cute+puppy>`

===============================
Imagens e Vídeos
===============================

Para inserir imagens, use::

    .. image:: imagem.png
        :height: 100 px
        :width: 200 px
        :scale: 400 %
        :align: center

    |

Para inserir vídeos, use::

    .. video:: _static/video.mp4
        :autoplay:
        :loop:
        :nocontrols:
        :height: 700
        :width: 700
        :muted:

Importante ressaltar que para que o vídeo funcione na documentação, é preciso instalar e colocar a extensão de arquivos de vídeo no arquivo de **conf.py**, em :ref:`Guia de Instalação <modo de utilização>` é explicado com mais detalhes o processo de instalação da extensão de vídeo.

============
Tabelas
============

O Sphinx também permite a criação de tabelas. Existem vários processos e tipos de tabelas, para encontrar um conteúdo com mais detalhes sobre, veja em https://sphinx-themes.org/sample-sites/sphinx-rtd-theme/kitchen-sink/tables/

Essa documentação vai expor o processo de criação de tabelas mais simples, porém existem os mais diversos tipos.

A tabela a seguir, é uma tabela simples sem cabeçalho:

====================== ====================== ======================
Exemplo                 Exemplo                 Exemplo

Exemplo                 Exemplo                 Exemplo

Exemplo                 Exemplo                 Exemplo

Exemplo                 Exemplo                 Exemplo

Exemplo                 Exemplo                 Exemplo

====================== ====================== ======================


O separador de colunas é o **=**, então, por exemplo a tabela::

   ====================== ====================== ======================
    Exemplo                 Exemplo                 Exemplo

    Exemplo                 Exemplo                 Exemplo

    Exemplo                 Exemplo                 Exemplo

    Exemplo                 Exemplo                 Exemplo

   ====================== ====================== ======================

possui 3 colunas.

O número de linhas vai depender do conteúdo que será inserido na tabela, ou seja, se eu colocar 4 linhas de texto entre os sinais de igual, minha tabela terá 4 linhas, como no exemplo acima.
