.. _linking-Sphinx.Basic:

.. include:: ../../_templates/CSS_DECLARE/color.dc_css

Basic Specification
=================================

.. sidebar:: Summary

    * :field-name:`Release:` 0.0.0
    * :field-name:`Last updated:` 2019/08/20
    * :field-name:`Authors:` |MainAuthor|
    * :field-name:`Target:` reformat
    * :field-name:`Status:` 5

Paragraphs
--------------

Paragraphs contain text and may contain inline markup.

    * *emphasis*： ``*emphasis*``
    * **strong emphasis**： ``**strong emphasis**``
    * `interpreted text`： ```interpreted text```
    * ``inline literals``： ````inline literals````
    * standalone hyperlinks： http://www.python.org
    * external hyperlinks： Python_

        .. _Python: http://www.python.org

        demoe:

            click me link to Python_

            click me link to `google <https://www.google.com.tw/>`_

    * internal cross-references： go_to_example_

        .. _go_to_example:

        The "_example" target above points to this paragraph.

        syntax::

            example_

            .. _example:

            The "_example" target above points to this paragraph.



    * footnote references: [1]_ (``[1]_``)

    * citation references: [CIT2002]_  (``[CIT2002]_``)

    * substitution references: |replace demo|

        .. |replace demo| replace:: Hello World!

        syntax::

            |replace demo|

            .. |replace demo| replace:: Hello World!

    * replace and link: |mathjax|_

        .. |mathjax| replace:: mathjax demo
        .. _mathjax: https://www.mathjax.org/#samples

        syntax::

            |mathjax|_

            .. |mathjax| replace:: mathjax demo
            .. _mathjax: https://www.mathjax.org/#samples

    * function: ``py:function:: def start(file):``

        .. py:function:: def start(file):

define your style
````````````````````````````

    * declare css at ``source\_templates\CSS_DECLARE\{my.css}`` ::

        .. role:: yellow

    * conf.py::

        rst_epilog += f'.. include:: {os.path.dirname(__file__)}/_templates/CSS_DECLARE/my.css' + '\n'

    * use it: :blue:`blue color` (``:blue:`blue color```)





List
-------

Bullet lists:
```````````````

- This is a bullet list.

- Bullets can be "*", "+", or "-".


Enumerated lists:
``````````````````

1. This is an enumerated list.

#. Enumerators may be arabic numbers, letters, or roman
   numerals.

Definition lists:
``````````````````

what
    Definition lists associate a term with a definition.

how
    The term is a one-line phrase, and the definition is one
    or more paragraphs or body elements, indented relative to
    the term.

Field lists:
``````````````````

:what: Field lists map field names to field bodies, like
       database records.  They are often part of an extension
       syntax.

:how: The field marker is a colon, the field name, and a
      colon.

      The field body may contain one or more body elements,
      indented relative to the field marker.

Option lists
``````````````````````````````````````````````````````````

    for listing command-line options:

        -a            command-line option "a"
        -b file       options can have arguments
                      and long descriptions
        --long        options can be long also
        --input=file  long options can also have
                      arguments
        /V            DOS/VMS-style options too


Literal blocks:
-------------------

    ::

        if literal_block:
            text = 'is left as-is'
            spaces_and_linebreaks = 'are preserved'
            markup_processing = None


Block quotes:
----------------

    This theory, that is mine, is mine.

    -- Anne Elk (Miss)


Table
-----------------

quickly create table: `online table editor <https://truben.no/table/>`_

Simple
`````````

    ====================  ==========  ==========
    Header row, column 1  Header 2    Header 3
    ====================  ==========  ==========
    body row 1, column 1  column 2    column 3
    body row 2            Cells may span columns
    ====================  ======================

    syntax::

            ====================  ==========  ==========
            Header row, column 1  Header 2    Header 3
            ====================  ==========  ==========
            body row 1, column 1  column 2    column 3
            body row 2            Cells may span columns
            ====================  ======================


tradition
````````````

    +-----------------------------+-----------+---------+
    | Description                 | 1 month   | 6 month |
    +=============================+===========+=========+
    | money back                  |     X     |   V     |
    +-----------------------------+-----------+---------+
    | M                           |     5     |   10    |
    |                             |           |         |
    | O                           |           |         |
    |                             |           |         |
    | N                           |           |         |
    |                             |           |         |
    | E                           |           |         |
    |                             |           |         |
    | Y                           |           |         |
    +-----------------------------+-----------+---------+

    syntax::

            +-----------------------------+-----------+---------+
            | Description                 | 1 month   | 6 month |
            +=============================+===========+=========+
            | money back                  |     X     |   V     |
            +-----------------------------+-----------+---------+
            | M                           |     5     |   10    |
            |                             |           |         |
            | O                           |           |         |
            |                             |           |         |
            | N                           |           |         |
            |                             |           |         |
            | E                           |           |         |
            |                             |           |         |
            | Y                           |           |         |
            +-----------------------------+-----------+---------+


Citation
------------

.. [1] A footnote contains body elements, consistently
   indented by at least 3 spaces.

.. [CIT2002] Just like a footnote, except the label is
   textual.

