Tests unitaires
===============

.. code-block:: console

  cd Python-OC-Lettings-FR/

  source venv/b-in/activate

  python manage.py test lettings.tests

  python manage.py test profiles.tests

  coverage run manage.py test lettings

  coverage run manage.py test profiles

  coverage report

  coverage html