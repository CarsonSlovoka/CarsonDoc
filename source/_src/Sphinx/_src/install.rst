.. _linking-Sphinx.Install:

.. include:: ../../../_templates/CSS_DECLARE/color.dc_css

Install
=================================

.. sidebar:: Summary

    * :field-name:`Release:` 0.0.0
    * :field-name:`Last updated:` 2019/08/21
    * :field-name:`Authors:` |MainAuthor|
    * :field-name:`Target:` install
    * :field-name:`Status:` 1


guideline
-------------

    * pip install sphinx (pip install sphinx -pre)
    * :blue:`(Optional)`
        *  plantuml
            + pip install sphinxcontrib-plantuml
            + donwload `java <https://www.java.com/zh_TW/>`_

                .. warning:: the computer must restart after install

            + `donwload plantuml.jar <http://plantuml.com/zh/download>`_


            + put plantuml.jar to ``%USERPROFILE%``
                + conf.py::

                    extensions.append('sphinxcontrib.plantuml')
                    plantuml = 'java -jar {0}'.format(os.path.join(os.environ["USERPROFILE"], 'plantuml.jar'))

            + dot.exe: `donwload graphviz <https://graphviz.gitlab.io/_pages/Download/Download_windows.html>`_
                + set env path: ``C:../graphviz-2.38/release/bin``
            + pycharm IDE plugins download：plantuml
            + pycharm→settins→plantUML→set dot path： ``C:/Program Files/graphviz-2.38/release/bin/dot.exe``
        * mathjax:
            + conf.py::

                extensions.append(''sphinx.ext.mathjax'')

Start
^^^^^^^^^^

    * cd {work_dir}
    * sphinx-quickstart {work_dir}

