.. :changelog:

History
-------

0.5.4 (2019-10-11)
++++++++++++++++++

* values always returned as strings -> BooleanFields are displayed now

0.5.3 (2019-02-12)
++++++++++++++++++

* reworte code to fetch payload data to avoid mysterious duplicated values

0.5.2 (2018-12-18)
++++++++++++++++++

* improved admin interface for ChartConfig

0.5.1 (2018-12-05)
++++++++++++++++++

* added management commands to create ChartType and ChartConfig objects.

0.5.0 (2018-10-25)
++++++++++++++++++

* added `app_name` param to ChartConfig to avoid ambiguity in case models in different apps do have the same name.

0.4.1 (2018-07-12)
++++++++++++++++++

* minor change in dropdown template tag

0.4.0 (2018-07-10)
++++++++++++++++++

* refactoring of templates by introducing template tags

0.3.0 (2018-06-13)
++++++++++++++++++

* removed work in progress banner

0.3.0 (2018-06-05)
++++++++++++++++++

* In case of DEBUG=False only fieldpaths/models can be explored which are registerd in dedicated ChartConfig objects.

0.2.0 (2018-06-01)
++++++++++++++++++

* Base templates can now be configured in settings-param

0.1.0 (2018-06-01)
++++++++++++++++++

* First release on PyPI.
