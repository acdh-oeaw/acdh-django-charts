=====
Usage
=====

To use django_charts in a project, add it to your `INSTALLED_APPS`:

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
        url(r'^', include(charts_urls)),
        ...
    ]
