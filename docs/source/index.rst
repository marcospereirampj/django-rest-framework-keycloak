.. Django REST Framework Keycloak documentation master file, created by
   sphinx-quickstart on Thu Aug 24 10:31:35 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. toctree::
   :maxdepth: 2
   :caption: Contents:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. image:: https://readthedocs.org/projects/django-rest-framework-keycloak/badge/?version=latest
   :target: http://django-rest-framework-keycloak.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status


Welcome to Django REST Framework Keyclaok's documentation!
==========================================================

**django-rest-framework-keycloak** package provides Keycloak support.

Installation
==================

Via Pypi Package::

   $ pip install django-rest-framework-keycloak

Manually::

   $ python setup.py install

Dependencies
==================

**django-rest-framework-keycloak** depends on:

* Python 3
* `django <https://www.djangoproject.com/>`_
* `djangorestframework <http://www.django-rest-framework.org/>`_
* `python-keycloak <http://python-keycloak.readthedocs.io/en/latest/>`_

Tests Dependencies
------------------

* unittest

Bug reports
==================

Please report bugs and feature requests at
`https://bitbucket.org/agriness/django-rest-framework-keycloak/issues <https://bitbucket.org/agriness/django-rest-framework-keycloak/issues>`_

Documentation
==================

The documentation for **django-rest-framework-keycloak** is available on `readthedocs <http://python-keycloak.readthedocs.io>`_.

Contributors
==================

* `Agriness Team <http://www.agriness.com/pt/>`_

Usage
=====

1. Add "django_keycloak" to your INSTALLED_APPS setting like this:

.. code-block:: python

    INSTALLED_APPS = [
        ...
        'django_keycloak',
    ]

2. Add "keycloak_django.middleware.KeycloakMiddleware" to your MIDDLEWARE setting like this:

.. code-block:: python

   MIDDLEWARE = [
       ...
       'keycloak_django.middleware.KeycloakMiddleware'
       ...
   ]

3. Add configure Keycloak:

.. code-block:: python

   KEYCLOAK_CONFIG = {
       'KEYCLOAK_SERVER_URL': 'http://localhost/auth/',
       'KEYCLOAK_REALM': 'your_realm',
       'KEYCLOAK_CLIENT_ID': 'your_client',
       'KEYCLOAK_CLIENT_SECRET_KEY': 'secret_key',
       'KEYCLOAK_CLIENT_PUBLIC_KEY': 'public_key',
       'KEYCLOAK_DEFAULT_ACCESS': 'DENY', # DENY or ALLOW (Default is DENY)
       'KEYCLOAK_AUTHORIZATION_CONFIG': os.path.join(BASE_DIR,  'your-client-authz-config.json'),
       'KEYCLOAK_METHOD_VALIDATE_TOKEN': 'INTROSPECT', # INTROSPECT OR DECODE (Default is INTROSPECT)
   }

4. Map the scopes of the APIView:

.. code-block:: python

   from django.http.response import JsonResponse
   from rest_framework.views import APIView

   class AdminView(APIView):
       keycloak_scopes = {'GET': 'read-only-admin-view',
                          'POST': 'edit-admin-view'}

       def get(self, request, **kwargs):
           return JsonResponse({"page": "Admin Resource"})

       def post(self, request, format=None):
           return JsonResponse({"page": "Edit Admin Resource"})

