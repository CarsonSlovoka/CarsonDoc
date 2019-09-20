.. _linking-GitHub.github_page:

.. include:: ../../../_templates/CSS_DECLARE/color.dc_css

=================================
GitHub Page
=================================

.. sidebar:: Summary

    * :field-name:`Release:` 0.1.0
    * :field-name:`Last updated:` 2019-09-20
    * :field-name:`Authors:` |MainAuthor|
    * :field-name:`Language:` en
    * :field-name:`Target:` Build with Sphinx
    * :field-name:`Status:` 1

.. sectnum::

Provide Web Services
====================================

1. Free domain
    * DNS
#. Web hosing
#. https


root & child nodes
====================================

    1. New repository
        * Repository name: ``{user_name}.github.io``
        * public

        .. note:: private: Upgrade to GitHub Pro or make this repository public to enable Wikis. ($7.00 / month)

    #. design by yourself or find your favorite theme in { `sphinx themes <https://sphinx-themes.org/>`_ , `jekyllthemes <http://jekyllthemes.org/>`_ } and apply them
        * Select source:
            * master branch
            * master branch /docs folder


Build with Sphinx
===================

Sphinx uses directories with leading underscores

You can fix this by adding a file called .nojekyll in the the directory with the generated sphinx html

.. important:: you need to create an empty file in the root directory that lets GitHub know you aren't using Jekyll to structure your site.
