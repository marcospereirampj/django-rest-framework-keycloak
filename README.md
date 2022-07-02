[![Documentation Status](https://readthedocs.org/projects/django-rest-framework-keycloak/badge/?version=latest)](http://django-rest-framework-keycloak.readthedocs.io/en/latest/?badge=latest)

Django REST Framework Keycloak
====================

**django-rest-framework-keycloak** package provides Keycloak support.

## Installation

### Via Pypi Package:

``` $ pip install django-rest-framework-keycloak ```

### Manually

``` $ python setup.py install ```

## Dependencies

**django-rest-framework-keycloak** depends on:

* Python 3
* [django](https://www.djangoproject.com/)
* [djangorestframework](http://www.django-rest-framework.org/)
* [python-keycloak](http://python-keycloak.readthedocs.io/en/latest/)

### Tests Dependencies

* unittest

## Bug reports

Please report bugs and feature requests at
https://bitbucket.org/agriness/django-rest-framework-keycloak/issues

## Documentation

The documentation for **django-rest-framework-keycloak** is available on [readthedocs](http://django-rest-framework-keycloak.readthedocs.io).

## Contributors

* [Agriness Team](http://www.agriness.com/)

## Usage

* Add "django_keycloak" to your INSTALLED_APPS setting like this::

```python
    INSTALLED_APPS = [
        ...
        'django_keycloak',
    ]
```

* Add "django_keycloak.middleware.KeycloakMiddleware to your MIDDLEWARE setting like this::

```python
   MIDDLEWARE = [
       ...
       'django_keycloak.middleware.KeycloakMiddleware'
       ...
   ]
```

* Add configure Keycloak::

```python
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
```

* Map the scopes of the APIView::

```python

from django.http.response import JsonResponse
from rest_framework.views import APIView

class AdminView(APIView):
    keycloak_scopes = {'GET': 'read-only-admin-view',
                       'POST': 'edit-admin-view'}

    def get(self, request, **kwargs):
        return JsonResponse({"page": "Admin Resource"})

    def post(self, request, format=None):
        return JsonResponse({"page": "Edit Admin Resource"})

```
