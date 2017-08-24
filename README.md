[![Documentation Status](https://readthedocs.org/projects/python-keycloak/badge/?version=latest)](http://python-keycloak.readthedocs.io/en/latest/?badge=latest)

Django REST Framework Keyclaok
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

The documentation for **django-rest-framework-keycloak** is available on [readthedocs](http://python-keycloak.readthedocs.io).

## Contributors

* [Agriness Team](http://www.agriness.com/pt/)

## Usage

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