.. _linking.Windows.Regedit.Tutorial:

.. include:: ../../../_templates/CSS_DECLARE/color.dc_css

=================================
Tutorial
=================================

.. sidebar:: Summary

    * :field-name:`Target:` REGEDIT
    * :field-name:`Release:` 0.0.0
    * :field-name:`Authors:` |MainAuthor|
    * :field-name:`Last updated:` 2019-09-24
    * :field-name:`Created:` 2019-09-24
    * :field-name:`Status:` Active


Repair
=================

The System File Checker tool built into Windows can scan your Windows system files for corruption or any other changes.

If a file has been modified, it will automatically replace that file with the correct version.

Here's how to use it.

* Method 1: Run `SFC` and `DISM` Tool
* Method 2: Replace regedit.exe
* Method 3: Use Third Party Registry Editor

SFC AND DISM
---------------

open cmd.exe and input: ``sfc /scannow``

.. note::

    scan requires administrative privileges in order to run,

    and if you're having any issues with SFC,

    be sure that you're using Command Prompt as an administrator.

This does not require Internet access.

If this not help, you may need to repair the Windows Component Store itself.

To do this, you need to Run DISM::

    Dism /Online /Cleanup-Image /CheckHealth
    Dism /Online /Cleanup-Image /ScanHealth
    Dism /Online /Cleanup-Image /RestoreHealth

Replace regedit
-------------------

1. open cmd.exe and input below:
    ``takeown /f "C:\Windows\regedit.exe"``

    ``icacls "C:\Windows\regedit.exe" /grant "%username%":F``

#. Find regedit.exe then rename it to regedit.exe.old and then close the file explorer.
#. Now if you have `C:/Windows.old/Windows` folder then copy the regedit.exe from it to `C:/Windows` folder.

   If not, then copy the regedit.exe from the `extracted.zip <https://drive.google.com/open?id=1-Ff1_HLnkKDwI2HHlwKENYi5P54OD-wW>`_ file to C:/Windows folder.

Reference
------------

* https://www.thewindowsclub.com/dism-vs-sfc-first-windows-10
* https://troubleshooter.xyz/wiki/fix-regedit-exe-crashes-when-searching-through-registry/
* https://blog.darkthread.net/blog/sfc-and-dism/
* https://troubleshooter.xyz/wiki/fix-regedit-exe-crashes-when-searching-through-registry/
* https://support.4it.com.au/article/sfc-scannow-and-extracting-results-from-cbs-log-windows-8/


Schedule Delete or Move Files on Next Windows Bootup
===========================================================

The registered rename and delete commands from the:

``HKLM/System/CurrentControlSet/Control/Session Manager/PendingFileRenameOperations`` value.

you can use `PendMoves.zip <https://download.sysinternals.com/files/PendMoves.zip>`_ tool to help you show or move files.

/pendmoves.exe
    shows file of scheduled for deletion at the next reboot

/movefile.exe
    allows you to schedule move and delete commands for the next reboot.

Reference
------------

* https://docs.microsoft.com/en-us/sysinternals/downloads/movefile


Several registry entries that program development must know
===================================================================

* windows services: ``HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services``
* Uninstall:
    **32-bit**
        ``HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall``

        ``HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall``

    **64-bit**
        ``HKEY_CURRENT_USER\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall``

        ``HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall``

* SYSTEM PATH:
    ``HKEY_CURRENT_USER\Environment``

    ``HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment``


* RUN AT STARTUP:
    ``HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run``

    ``HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run``

    ``HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Run``

* ShellNotifyIcon
    windows 7 8 10:
        ``HKEY_CURRENT_USER\Software\Classes\Local Settings\Software\Microsoft\Windows\CurrentVersion\TrayNotify``

    windows XP:
        ``HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\TrayNotify``

    .. note::

        It writes all the information together at ``IconStreams`` and ``PastIconsStream``.
        This reason is why you can't delete files by specific.

Define menu that belongs to you
====================================

create a file `{name}.reg` and write the contents as below::

    Windows Registry Editor Version 5.00
    ;Directory Right Click
    ;[HKEY_CLASSES_ROOT\Directory\shell\xxx]

    ;File Right Click
    ;[HKEY_CLASSES_ROOT\*\shell\xxx]

    ;This example will create an item which name is "MenuCMD" that you will see after you right-click at directory
    ;That will run cmd.exe and pass the path which is the directory that you click one.
    [HKEY_CLASSES_ROOT\Directory\shell\MenuCMD]
    "MUIVerb"="cmd"
    "Icon"="shell32.dll,-3"
    "Position"="top"
    [HKEY_CLASSES_ROOT\Directory\shell\MenuCMD\command]
    ; every variable that contains with "%" is not working at here.
    ; you can pass other parameters, for example:
    ; @="C:\\your_dir\\your.exe para1 para2 ..."
    @="C:\\Windows\\System32\\cmd.exe %1"
