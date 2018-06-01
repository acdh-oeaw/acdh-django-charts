=============================
django_charts
=============================

.. image:: https://badge.fury.io/py/acdh-django-charts.svg
    :target: https://badge.fury.io/py/acdh-django-charts

.. image:: https://travis-ci.org/acdh-oeaw/acdh-django-charts.svg?branch=master
    :target: https://travis-ci.org/acdh-oeaw/acdh-django-charts

.. image:: https://codecov.io/gh/acdh-oeaw/acdh-django-charts/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/acdh-oeaw/acdh-django-charts

An app to explore your data through charts based on Highcharts.js

Documentation
-------------

The full documentation is at https://acdh-django-charts.readthedocs.io.

Quickstart
----------

Install django_charts::

    pip install acdh-django-charts

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'charts.apps.ChartsConfig',
        ...
    )

Add django_charts's URL patterns:

.. code-block:: python

    from charts import urls as charts_urls


    urlpatterns = [
        ...
        url(r'^charts/', include(charts_urls, namespace='charts')),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
