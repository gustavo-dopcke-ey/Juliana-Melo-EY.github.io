===================================
Como Criar e Disponibilizar o html
===================================

Como mencionado anteriormente, o Sphinx permite a criação dos mais diversos tipos de arquivos. Como essa documentação busca explicitar o processo da criação de documentações no estilo página web, o processo que será exposto será o de criação de um arquivo html a partir dos arquivos .rst e códigos de sua documentação.

Para criar o html da documentação, abra o terminal, coloque no caminho do diretório que contém os arquivos da documetação e use o seguinte comando::

    ./make html

O Sphinx vai ler tanto os arquivos .rst quanto os códigos que serão documentados via autodoc e criará um html com esses arquivos consolidados. Os html criados pelo Sphinx ficarão na pasta **build**, para saber mais detalhes sobre a estrutura de pastas do Sphinx, acesse :ref:`Entendendo Estrutura do Repositório <entendendo a estrutura>`.

Para visualizar a documentação, copie o path do arquivo index.html e cole em um navegador de sua preferência, a documentação aparecerá como uma página web, porém, como a visualização do html está vinculada com o path do arquivo em seu computador, ele fica vinculado ao seu usuário, logo o html não pode ser compartilhado.


Para compartilharmos a documentação criada via html, ela precisará ser hospedada. Existem diversas formas de hospedar o html da documentação criado pelo Sphinx, a mais simples é via Git Pages.

Para hospedar sua documentação via Git Pages siga o processo abaixo:

1. Criação do repositório
==========================


    Um repositório precisa ser criado no GitHub e o nome do repositório precisa seguir o seguinte formato::

        username.github.io

    Caso o nome do repositório não siga esse formato, o processo não irá funcionar.

    Depois que o repositório for criado, abra um terminal na pasta da documentação e clone o repositório criado::

        git clone https://github.com/username/username.github.io


    Copie a pasta **build/html** da sua documentação Sphinx para o repositório local clonado.::

        cp -r build/html /caminho/para/o/repositório/local

    Add, commit, e push::

        cd username.github.io
        
        git add html

        git commit -m "Initial commit"

        git push -u origin main


    Depois desse processo, sua documentação já está disponível como uma página web. Para acessa-lo,abra um navegador procure a seguinte página::

        https://username.github.io