Exécuter le site, en local, avec Docker
=======================================

Vous devez avoir installé "docker" (ou podman) et "docker-compose".

On va exécuter un script format BASH. Sur Windows il faudra adapter, jouer les seules commandes nécessaires.

.. code-block:: console

  cd Python-OC-Lettings-FR/

Pour une première exécution:

.. code-block:: console

  ./docker-compose-deployment.sh build

Dans le cas où vous avez déjà les images en local et l'application initialisée:

.. code-block:: console

  ./docker-compose-deployment.sh run

Pour arrêter les conteneurs:

.. code-block:: console

  ./docker-compose-deployment.sh down
