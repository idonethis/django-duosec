# -*- coding: utf-8 -*-
"""Setup file for easy installation"""
from os.path import join, dirname
from setuptools import setup


LONG_DESCRIPTION = """
Provides Duo Security's 2-factor authenication capabilities for Django 
apps.
"""


def long_description():
    """Return long description from README.rst if it's present
    because it doesn't get installed."""
    try:
        return open(join(dirname(__file__), 'README.rst')).read()
    except IOError:
        return LONG_DESCRIPTION


setup(name='django-duosec',
      version='1.0',
      author='Duo Security + Mike Sun',
      description='Duo Security two-factor auth for Django apps',
      packages=['duo_app',],
      package_data={'duo_app':['locale/*/LC_MESSAGES/*']},
      long_description=long_description(),
      install_requires=['django>=1.2.5',
      classifiers=['Framework :: Django',
                   'Programming Language :: Python :: 2.7'])
