.. _linking-GitHub.git_tutorial:

.. include:: ../../../_templates/CSS_DECLARE/color.dc_css

Tutorial
=================================

.. sidebar:: Summary

    * :field-name:`Release:` 0.0.0
    * :field-name:`Last updated:` 2019/08/22
    * :field-name:`Authors:` |MainAuthor|
    * :field-name:`Target:` Setting
    * :field-name:`Status:` 1


.gitconfig
-----------------------------

    1. cd %USERPROFILE%
    2. create file: ``.gitconfig.`` ::

        [user]
	        name = ???
	        email = xxx@gmail.com
        [gui]
        [alias]
            st = status
        [core]
            quotepath = false
            editor = '%PROGRAMFILES(X86)%\\Notepad++\\notepad++.exe' -multiInst -notabbar -nosession -noPlugin
        [gui]
            encoding = utf-8
        [i18n "commit"]
	        encoding = utf-8
        [i18n]
	        logoutputencoding = utf-8


.gitignore
-----------------

    ::

        # comment

        # ignore .some_dir
        some_dir/

        # ignore all {DS_Store, sys} file
        *.DS_Store
        *.sys

        # not ignore: "!"
        !src/css/*.sys

    force add: ``git add *.sys -f``

