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
-------------

To visualize any property of your model you have to pass in the models name (lowercase), the field-path (using django's lookup syntax `__` to follow foreign key and many2many relations) and the chart type (bar|line|pie) via keyword arguments to the `charts.views.DynChartView()`. In case those params are valid (i.d. the model and the lookup path acutally exist) the according chart should be drawn. But be aware that this only works if your project's `DEBUG` settings are set to `True`.
As **recomended** alternative you should create `ChartConfig` objects for each property/model you'd like to explore via django admin-backend.

management commands
-------------------

The package ships with a management command to

* create/delete chartconfig objects (Bar, Pie, Linecharts)

.. code-block:: console

    python manage.py create_charttypes

.. code-block:: console

    python manage.py delete_charttypes

* create/delete ChartConfig objects per application

.. code-block:: console

    python manage.py create_charts <app_name>

.. code-block:: console

    python manage.py delete_charts <app_name>

Build and publish
-----------------

.. code-block:: console

    python setup.py sdist bdist_wheel
    twine upload dist/*



Features
--------

* Visualizes aggregated values of your models as charts (pie/bar/line) using https://www.highcharts.com/
* Charts can be configured via admin backend (see Configuration Section)

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
