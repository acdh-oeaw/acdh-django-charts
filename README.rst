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
        'charts',
        ...
    )

Add django_charts's URL patterns:

.. code-block:: python

    urlpatterns = [
        ...
        url(r'^charts/', include('charts.urls', namespace='charts')),
        ...
    ]

By default the app's templates extend a base template `webpage/base.html`. To ovveride this, just define a `CHARTS_BASE_TEMPLATE` variable on your project's `settings.py` like e.g:

.. code-block:: python

    CHARTS_BASE_TEMPLATE = 'base.html'

To link to the application's 'chart-selector-view' you can add something like the snippet below to your e.g. base-template:

.. code-block:: html

    <a href="{% url 'charts:chart_selector' %}">Charts</a>

Configuration
----

ToDo...


Build and publish
-----

.. code-block:: console

    python setup.py sdist bdist_wheel
    twine upload dist/*



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
