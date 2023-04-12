===================
Guia de Instalação
===================

.. _modo de utilização:

Em :ref:`Afinal, o que é Sphinx? <afinal o que é o sphinx>` temos um overview sobre a biblioteca e suas funcionalidades. Para utilizar a Sphinx como recurso de documentação é necessário fazer sua instalação. Para isso, siga as etapas abaixo:



Instalação
=============

O Sphinx possui um processo de instalação simples e rápido, entretanto, para diminuir a chance de erros e problemas com versões de outras bibliotecas, é aconselhada a criação de um ambiente virtual, para isso, antes de instalar a Sphinx, siga seguintes etapas:

Criação do ambiente virtual
===========================

Em um terminal de sua preferência coloque::

   python -m venv 'nome_env'

Ativando o ambiente virtual
===========================
Para ativar o ambiente, use::

   'nome_env'/Scripts/activate

Instalação do Sphinx
====================

Depois de seguir esses passos, vamos instalar o Sphinx no seu ambiente, para isso::

   pip install -U Sphinx

Instale também a extensão que permite a inserção de vídeos na documentação::

   pip install sphinxcontrib-video


Quickstart
==========

É aconselhada a criação de um diretório para rodar o Sphinx, para isso use::

   mkdir Sphinx

Com o diretório criado, mude o caminho::

   cd Sphinx

Depois desses passos seu ambiente virtual está pronto para rodar a Sphinx, para rodar o quickstart use::

   python -m sphinx.cmd.quickstart

Após executar esse comando, o Sphinx fará algumas perguntas como o nome do projeto, idioma e etc. Após preencher todas as perguntas, a instalação está concluída e o Sphinx está pronto para ser utilizado.
Em :ref:`Entendendo a Estrutura <entendendo a estrutura>` temos uma explicação detalhada de como a Sphinx é estruturada e todas as adaptações que precisam ser feitas antes de gerar a documentação.






