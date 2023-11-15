Exécuter le site, en local, sans Docker
=======================================

.. code-block:: console

  cd Python-OC-Lettings-FR/

  source venv/bin/activate

  pip install --requirement ./Python-OC-Lettings-FR/requirements.txt

  python manage.py runserver

- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).