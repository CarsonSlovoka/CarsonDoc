.. _linking-Sphinx.Admonitions:

.. include:: ../../_templates/CSS_DECLARE/color.dc_css

Admonitions
=====================

.. sidebar:: Summary

    * :field-name:`Release:` 0.0.0
    * :field-name:`Last updated:` 2019/08/21
    * :field-name:`Authors:` |MainAuthor|
    * :field-name:`Target:` define style
    * :field-name:`Status:` 3

admonition
-------------

.. admonition:: Neque porro quisquam

   Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus mattis commodo eros, quis posuere enim lobortis quis. Nullam ut tempus nibh.


caution
--------

.. caution:: Neque porro quisquam

   Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus mattis commodo eros, quis posuere enim lobortis quis. Nullam ut tempus nibh.

danger
---------------


.. danger:: Neque porro quisquam

   Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus mattis commodo eros, quis posuere enim lobortis quis. Nullam ut tempus nibh.

error
---------------

.. error:: Neque porro quisquam

   Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus mattis commodo eros, quis posuere enim lobortis quis. Nullam ut tempus nibh.


hint
---------------

.. hint:: Neque porro quisquam

   Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus mattis commodo eros, quis posuere enim lobortis quis. Nullam ut tempus nibh.

important
---------------

.. important:: Neque porro quisquam

   Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus mattis commodo eros, quis posuere enim lobortis quis. Nullam ut tempus nibh.

note
---------------

.. note:: Neque porro quisquam

   Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus mattis commodo eros, quis posuere enim lobortis quis. Nullam ut tempus nibh.

tip
---------------

.. tip:: Neque porro quisquam

   Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus mattis commodo eros, quis posuere enim lobortis quis. Nullam ut tempus nibh.

warning
---------------

.. warning:: Neque porro quisquam

   Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus mattis commodo eros, quis posuere enim lobortis quis. Nullam ut tempus nibh.

define your style
--------------------

.. admonition:: section

    title

        * add your css at: ``_static/css/Page.css``

        * conf.py::

            def setup(app):
                app.add_stylesheet("css/Page.css")
        * use::

            .. admonition:: section

                title

                    text
