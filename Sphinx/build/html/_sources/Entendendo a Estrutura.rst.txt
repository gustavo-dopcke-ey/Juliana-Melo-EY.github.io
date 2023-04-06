=======================
Entendendo a Estrutura
=======================

.. _entendendo a estrutura:

O processo de instalação foi detalhado em :ref:`Guia de Instalação <modo de utilização>`. Após finalizado todo o processo exposto, o Sphinx já pode ser utilizado.

Estrutura Sphinx
================

No diretório criado para rodar o Sphinx, após o quickstart, encontaremos uma estrutura com 2 pastas, **build** e **source**, em **build** ficam os htmls criados após a compilação do código que gera a documentação, agora em **source** temos os arquivos default,  nela temos o arquivo chamado **conf.py**, nele, temos as informações gerais  da documentação, como o nome, autor e etc. Ainda em conf.py também é possível alterar o template que será utilizado e adicionar extensões.

Alterar Template da Documentação
================================
Como abordado em :ref:`Afinal, o que é Sphinx? <afinal o que é o sphinx>`, o Sphinx possui inúmeros templates disponíveis, por default ele vem com o template Alabama, mas é possível escolher outros templates em https://sphinx-themes.org/#themes e mudar no conf.py em *html theme*.

Extensões
=========
Podemos também adicicionar extensões. Para inserir vídeos e gerar documentação automática de códicos na documentação, precisamos em *extensions* colocar as extensões::

    [#[...]"sphinxcontrib.video", 'sphinx.ext.autodoc']

Autodocumentação sys.path
==========================

O Sphinx pode acusar alguns erros em relação ao autodoc, que é a documetação automática de códigos do Sphinx. Para evitar que isso aconteça, coloque no início do **conf.py** o seguinte código:

.. code-block:: python
    :linenos:
    
    import sys
    import os

    sys.path.insert(0, os.path.abspath('..'))


Página Inicial da Documentação
==============================

Depois da alteração do **conf.py** a documentação já pode ser iniciada.

O Sphinx permite a documentação via arquivos rst e direto de códigos. Para criar páginas, inserir textos, imagens, vídeos, tabelas, links e etc, criamos arquivos .rst e inserimos esse conteúdo usando **reStructuredText**.

Em https://docutils.sourceforge.io/docs/ref/rst/directives.html#image conseguimos achar como funciona a estrutura do **reStructuredText**.

Index
======

O arquivo **index.rst** é o arquivo responsável pela página inicial da sua documentação, é nele que serão inseridos os conteúdos que aparecerão na primeira página da documentação. Importante ressaltar que o conteúdo nessa página e nas demais, precisa estar estruturado seguindo o **reStructuredText**.

Page Source
===========

Em https://sphinx-themes.org/sample-sites/sphinx-rtd-theme/ e nos demais templates disponíveis temos, além da sintaxe, o Código fonte utilizado para gerar as páginas, clicando em **view page source** é possível observar com mais facilidade todo o processo de construção e comandos necessários.

============================
Páginas, Links e Referências
============================

Para inserir **páginas** e referência-las em sua documentação, crie um arquivo .rst no mesmo diretório do index.rst. Depois de inserir todas as informações no arquivo criado, referencie ele para que a página seja criada.

Criando Páginas via toctree
===========================
Depois de criar as páginas precisamos referencia-las, para isso::


    .. toctree::
        :caption:Título(para que as páginas fiquem agrupadas em ‘pastas’):
        :titlesonly:

    nome do arquivo.rst criado

Agora, para referenciar páginas já criadas:

1. Crie a referência na página(arquivo.rst), colocando o seguinte comando logo depois do título da página::

    .. _pagina:

2. Use ref para referenciar a página::

    :ref:`Página <pagina>`

Links
======

Para inserir links na documentação basta pegar o https e colar como se fosse um texto no .rst.



