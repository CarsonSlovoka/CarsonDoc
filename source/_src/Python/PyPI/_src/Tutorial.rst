.. include:: ../../../../_templates/CSS_DECLARE/color.dc_css

.. _linking.Python.PyPI.Toturial:

=================================
Tutorial
=================================

.. sidebar:: Summary

    * :field-name:`Release:` 0.1.0
    * :field-name:`Last updated:` 2019/09/06
    * :field-name:`Authors:` |MainAuthor|
    * :field-name:`Target:` reformat and add MANIFEST.in
    * :field-name:`Status:` 1

----

***********************
1. How to Pronounce?
***********************

PyPy is pronounced ``pie pie``,

PyPI is pronounced ``pie pee eye`` or ``the cheeseshop``.

*********************
2. Publish To PyPI
*********************

2.1 Create Account
====================

If you don't have an account yet, go to the `official website <https://pypi.org/>`_ to register an account:

2.2 Settings (account, password)
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

2.3 Prepare Data
====================

Set your directory structure are as follows:

    \file
        * .setup.py [#note-setup.py]_
        * MANIFEST.in
        * README.{rst, md}

        .. note:: README file is not necessary to be located here but recommended

        * LICENSE (Option)
    \directory
        * {packages} [#note-packages]_

        .. note:: name of "packages" is an example, not necessary named to same.

    .. important:: Remember! These are all related to the contents of the ``setup.py`` [#note-setup.py]_ file.

.. [#note-setup.py] name of "setup.py" is not necessary named to so, but this has been used or accepted in the society.
.. [#note-packages] After you `pip install {project}` finished that will also install those files that is what you append anything of files or directory in packages directory.

2.3.1 Write contents
====================

2.3.1.1 MANIFEST.in
-----------------------

::

    include LICENSE
    include {other files}

2.3.1.2 setup.py
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

..  tip:: `Learn more > <https://packaging.python.org/guides/distributing-packages-using-setuptools/?highlight=manifest#setup-args>`_

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

