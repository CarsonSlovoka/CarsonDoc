.. include:: ../../../../_templates/CSS_DECLARE/color.dc_css

.. _linking.Python.PyPI.Toturial:

=================================
Tutorial
=================================

.. sidebar:: Summary

    * :field-name:`Release:` 0.3.1
    * :field-name:`Last updated:` 2019/09/12
    * :field-name:`Authors:` |MainAuthor|
    * :field-name:`Target:` pip install -r requirements.txt
    * :field-name:`Status:` 1

----

.. sectnum::

***********************
How to Pronounce?
***********************

PyPy is pronounced ``pie pie``,

PyPI is pronounced ``pie pee eye`` or ``the cheeseshop``.

*********************
Publish To PyPI
*********************

Create Account
====================

If you don't have an account yet, go to the `official website <https://pypi.org/>`_ to register an account:

Settings (account, password)
========================================

**load account and password from config**

    create ``.pypirc`` file at ``%USERPROFILE%/.pypirc``

    **file contents**::

        [distutils]
        index-servers =
          pypi
          pypitest

        [pypi]
        repository = https://pypi.python.org/pypi
        username = your_name
        password = ???

        [pypitest]
        repository = https://testpypi.python.org/pypi
        username= your_name
        password= ???

    .. note::

        that will publish to two websites (pypi and pypitest) at the same time.

        just remove if you won't need someone

Prepare Data
====================

Set your directory structure are as follows:

    \file
        * .setup.py [#note-setup.py]_
        * MANIFEST.in
        * README.{rst, md}

        .. note:: README file is not necessary to be located here but recommended

        * requirements.txt (Option)

        .. note::

            **list all packages:**
                * pip list
                * pip freeze > requirements.txt

            **install packages by requirements.txt:**
                pip install -r requirements.txt

        * LICENSE (Option)
    \directory
        * {packages} [#note-packages]_

        .. note:: name of "packages" is an example, not necessary named to same.

    .. important:: Remember! These are all related to the contents of the ``setup.py`` [#note-setup.py]_ file.

.. [#note-setup.py] name of "setup.py" is not necessary named to so, but this has been used or accepted in the society.
.. [#note-packages] After you `pip install {project}` finished that will also install those files that is what you append anything of files or directory in packages directory.

Write contents
====================

MANIFEST.in
-----------------------

\Manifest-related options:
    * if the manifest file (MANIFEST by default) exists and the first line does not have a comment indicating it is generated from MANIFEST.in, then it is used as is, unaltered
    * ``if the manifest file doesn’t exist or has been previously automatically generated, read MANIFEST.in data to create the manifest``
    * if neither MANIFEST nor MANIFEST.in exist, create a manifest with just the default file set
    * use the list of files now in MANIFEST (either just generated or read in) to create the source distribution archive(s)

\contents:
    ::

        include LICENSE
        include *.txt # include all files in the distribution root matching *.txt

        exclude temp.py test.py  #

        recursive-include examples *.txt *.py  # all files anywhere under the examples directory matching *.txt or *.py
        recursive-exclude examples *.test

        prune dir  # exclude all files under dir
        prune examples/sample?/build  # exclude all directories matching examples/sample?/build.

        graft dir  # include all files under dir
        graft Carson\Class

.. important:: every items of MANIFEST.in are promise able to download, but it doesn't mean that can put those to ``Python\Lib\site-packages`` path.

`Learn more MANIFEST > <https://docs.python.org/2/distutils/sourcedist.html>`_

setup.py
-----------------------

.. code-block:: python

    from distutils.core import setup

    # from setuptools import find_packages
    # packages=find_packages(exclude=['contrib', 'docs', 'tests', 'temp'])

    with open('README.rst', encoding='utf-8') as f:
        long_description = f.read()

    author = 'Carson'
    project_name = 'your_project_name'

    setup(
        name=f'{author}-{project_name}]',  # it means: pip install {name}  # I recommended use author+project_name
        version='{0.0.0}',  # x.x.x.{dev, a, b, rc}  # a: alpha, b: beta, rc: release  # pip install "name==x.x.x.dev1"

        # when user install finished,
        # will create those file at
        #   %Python%/Lib/site-packages/{packages_1}/{subItem}
        #   %Python%/Lib/site-packages/{packages_2}/{everything you wan't}
        packages=["{packages_1}/{subItem}", "{packages_2}/{everything you wan't}"],
        # include_package_data=True,
        # exclude_package_data={}
        # package_data={"{packages_path}": ["icons/*"]},  # https://packaging.python.org/guides/distributing-packages-using-setuptools/#manifest-in

        # data files will put those directories at Python root path (same with Scripts, Lib, etc.)
        data_files=[('Carson/Image/jpg', ['Carson/Image/jpg/5.jpg', 'Carson/Image/jpg/6.jpg']),  # the sub-item directory name must be the same as the root directory name.
                    ('Carson/Image/png', glob('Carson/Image/png/*.png')),],  # modified by your self


        license="{MIT}",

        author=author,
        author_email='{your@gmail.com}',

        scripts=['{your.exe}'],  # this will be put at %Python%/Scripts/{some.exe}.
        # python path is usually auto append to the system path,
        # then {your.exe} will be run after user open terminal and typing text: {your.exe}. ( it's not necessary to input abspath)

        install_requires=[],  # other PyPI packages

        url='https://github.com/{user name}/{project name}',  # (Option). # It's not necessary to use GitHub. It's ok with using another URL what you like.
        project_urls={
            # 'Bug Reports': 'https://github.com/{user name}/{project name}/issues',
            # 'Funding': '',
            # 'Say Thanks!': '',
            # 'Source': '',
        },

        description='{simply description of your project}',
        long_description=long_description,  # read data from file.
        long_description_content_type='text/x-rst',  # text/markdown  # Learn more > https://packaging.python.org/guides/making-a-pypi-friendly-readme/
        keywords=[],  # just input what you like.

        download_url='https://github.com/{user name}/{project name}/tarball/{v0.0.0}',  # (Option).
        # If you are using GitHub, tags allow you to download.
        # you can use 'git tag -a {tag_name}' to create tag
        python_requires='>=3.6.2, <4',  # defined by your self

        zip_safe=False,  # Set to False to start faster
        classifiers=[
            # the follow below that must input specific format instead of what you like!
            # Learn more > https://pypi.org/classifiers/
            'Topic :: System :: Logging',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Natural Language :: Chinese (Traditional)',
            'Natural Language :: English',
            'Operating System :: Microsoft',
            'Operating System :: MacOS',
            'Operating System :: Unix',
            'Development Status :: 5 - Production/Stable',
            'License :: OSI Approved :: Apache Software License',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
        ]
    )

.. important:: you must set `.py` path assign to ``packages`` variable instead of writing at MANIFEST.in otherwise, it will not put those files to ``Python\Lib\site-packages``

..  tip:: `Learn more > <https://packaging.python.org/guides/distributing-packages-using-setuptools/?highlight=manifest#setup-args>`_

**************
build
**************

There are three major `setup.py` commands we will use:


\bdist_egg:
    This creates an egg file. This is what is necessary so someone can use ``esay_install your_project``.

    .. note::

        `easy_install` is old fashioned! I'll suggest you using pip install too instead of it.

        that is because ``pip`` provide more information to tell you what's happening.

\bdist_wininst
    This will create an ``.exe`` that will install your project on a windows machine.

    That will put "Remove{project}.exe" and "{project}-winiest.log" at the Python directory.

    "{project}-winiest.log" recorded all install information so that when uninstall that can delete all files (include registry values) by reference.

    .. note:: if you want to uninstall, you may use the ``Add or Remove`` programs to do that.

\sdist:
    This create a raw source distribution which someone can download and run ``python setup.py`` directly.


    .. note:: full command: ``python setup.py sdist``

.. tip:: `build Learn more > <https://pythonhosted.org/an_example_pypi_project/setuptools.html>`_

**************
py2exe
**************

* pyInstaller - Cross-platform
* cx_Freeze - Cross-platform
* constructor - For command-line installers
* py2exe - Windows only
* py2app - Mac only
* bbFreeze - Windows, Linux, Python 2 only
* osnap - Windows and Mac
* pynsist - Windows only

`See more > <https://packaging.python.org/overview/>`_

**************
Reference
**************

* `What's different between distutils and setuptools <https://stackoverflow.com/questions/25337706/setuptools-vs-distutils-why-is-distutils-still-a-thing>`_
* `Packaging Python Projects <https://packaging.python.org/tutorials/packaging-projects/>`_
* `Error Code <https://segmentfault.com/a/1190000008663126>`_
* `bdist_egg, bdist_wininst, sdist <https://pythonhosted.org/an_example_pypi_project/setuptools.html>`_

