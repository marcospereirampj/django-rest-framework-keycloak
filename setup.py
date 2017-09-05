# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='django-rest-framework-keycloak',
    version='0.2.0',
    url='https://bitbucket.org/agriness/django-rest-framework-keycloak',
    license='GNU General Public License - V3',
    author='Marcos Pereira',
    author_email='marcospereira.mpj@gmail.com',
    keywords='django rest framework keycloak openid',
    description=u'django-rest-framework-keycloak package provides Keycloak support.',
    packages=['django_keycloak'],
    install_requires=['django>=1.10', 'djangorestframework>=3.6.3', 'python-keycloak>=0.9.0'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Topic :: Utilities'
    ]
)
