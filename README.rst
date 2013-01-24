Webapp Server
#############

Ce script permet de servir vos fichiers `.webapp` et `.manifest` avec les bons
Content-Type; pour qu'ils soient installables en tant que webapps sur
FirefoxOS.

Pour l'utiliser sur votre machine, allez dans le dossier ou vos fichiers
.webapp (ou .manifest) sont et faites::

    $ wget https://raw.github.com/ametaireau/webappserver/master/serve.py

Et il ne vous reste qu'à le lancer::

    $ python serve.py
