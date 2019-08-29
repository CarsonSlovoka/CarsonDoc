.. _linking-Sass_SCSS.Install:


Install
=================================

.. sidebar:: Summary

    * :field-name:`Release:` 0.0.0
    * :field-name:`Last updated:` 2019/08/28
    * :field-name:`Authors:` |MainAuthor|
    * :field-name:`Target:` install
    * :field-name:`Status:` 1

----

guideline
-------------

There are two ways to compile scss/sass file.

1. node js: npm
#. ruby: gem

node js
^^^^^^^^^^

1. download `node.js <https://nodejs.org/en/>`_ [#note-green]_

#. after you finished, run command: ``npm --version`` to check install success

    .. note:: 勾選自動安裝Chocolatey
    .. note:: nodejs will install at: ``%ProgramFiles%/nodejs`` which contains {npm, npx, node}

#. npm install -g scss-compile

/Usage:
    you can run it from any directory. Just run: ``npm run scss-compile``

ruby
^^^^^^^^^^

1. download `ruby Ruby+Devkit 2.5.5-1 (x64) <https://rubyinstaller.org/downloads/>`_
#. ``ruby -v`` or ``ruby --version``
#. after you download ruby, you will get the **gem** . using ``gem environment`` to watch all path.
#. update gem: ``gem update --system``
#. ``gem install sass``

    .. hint:: all you install packages which location will at ``{ruby_dir}\gems\{gem_version2.5.0}\gems``


#. ``sass -v`` > *Ruby Sass 3.7.4*
#. `option:` ``gem install compass``

    如果你的scss檔案裏面有用到，就要安裝，例如

    @import "compass/css3";

    .. error::

        If you can't install successfully.

        you must get there which is https://github.com/Igosuki/compass-mixins and clone it.

        all the .sass inside ``compass-mixins\lib\*`` that is what you need！

Usage:
    ``sass input.scss output.css``


.. note::

    `PyCharm Setting <https://www.jetbrains.com/help/pycharm/transpiling-sass-less-and-scss-to-css.html>`_

    Installing Sass/SCSS ``npm install -g sass`` LEARN MORE > https://sass-lang.com/install


----


Reference
----------

.. [#note-green] ★ go to `node green <https://node.green/>`_ to check whether packages are available

* practice HTML+CSS(scss, sass)+JS: https://codepen.io
