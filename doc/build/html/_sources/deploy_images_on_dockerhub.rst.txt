Déploiement images Docker, sur DockerHub
========================================

On utilisera le dépôt Docker générique: `DockerHub <https://hub.docker.com/>`_

Afin de simplifier les illustrations tout comme l'usage des commandes en local, vous aurez créer un fichier ".


On va exécuter un script format BASH. Sur Windows il faudra adapter, jouer les seules commandes nécessaires.

.. code-block:: console

  cd Python-OC-Lettings-FR/

  ./docker-compose-deployment.sh build

  ./docker-compose-deployment.sh down

  ./docker-compose-deployment.sh publish