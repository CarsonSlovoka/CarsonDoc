.. _linking-ELK.Install:

.. .. sectnum::

.. include:: ../../../_templates/CSS_DECLARE/color.dc_css

.. |ss| raw:: html

    <strike>

.. |se| raw:: html

    </strike>

================
Install
================

.. sidebar:: Summary

    * :field-name:`Release:` 0.0.0
    * :field-name:`Last updated:` 2020/02/03
    * :field-name:`Authors:` |MainAuthor|
    * :field-name:`Target:` Install
    * :field-name:`Status:` 1

You need install:

    1. JAVA
    #. Elasticsearch
    #. Logstash
    #. Kibana

JAVA
========================

.. note:: Which version of JAVA should be installed? see `Support Matrix`_

#. Installation `Java <https://java.com/zh_TW/download/faq/java_win64bit.xml#verify%20browser>`_

    `jdk-8u241-windows-x64.exe <https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html>`_

    `jdk-11.0.6_windows-x64_bin.exe <https://www.oracle.com/technetwork/java/javase/downloads/jdk11-downloads-5066655.html>`_

    .. note:: JDK(Java SE 8u241) installation package will include JRE
    .. note:: Different environments provide different resources, such as the current JDK-11 does not provide JRE and SERVER-JRE

    * check with command

        1. ``java -version``::

            java version "11.0.6" 2020-01-14 LTS
            Java(TM) SE Runtime Environment 18.9 (build 11.0.6+8-LTS)
            Java HotSpot(TM) 64-Bit Server VM 18.9 (build 11.0.6+8-LTS, mixed mode)
            # Java HotSpot(TM) Client VM (build 25.241-b07, mixed mode, sharing)  # 32

        2. :strike:`javac -version`::

            javac 1.8.0_241


`Elasticsearch Install <https://www.elastic.co/guide/en/elasticsearch/reference/current/zip-windows.html>`_
===============================================================================================================

Installation steps
-------------------

#. `Download Elasticsearch <https://www.elastic.co/cn/downloads/elasticsearch>`_
#. Run ``bin/elasticsearch`` (or ``bin\elasticsearch.bat`` on Windows) to start the ELK

    ERROR:

        - [2020-02-03T10:38:51,721][INFO ][o.e.x.s.s.SecurityStatusChangeListener] [XXX-MACHINE] Active license is now [BASIC]; Security is disabled
            - `FIX <https://www.elastic.co/cn/blog/elastic-stack-6-3-0-and-6-3-1-may-disable-security-for-trial-licenses>`_:
                Ensure you have this setting in your :mark:`config/elasticsearch.yml` file: ``xpack.security.enabled: true``

#. Run :mark:`curl http://localhost:9200/` or :mark:`Invoke-RestMethod http://localhost:9200` with PowerShell
#. Dive into the `getting started guide <https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started.html>`_ and video.

Config
-------------

Config files location edit
Elasticsearch has three configuration files:

1. ``elasticsearch.yml`` for configuring Elasticsearch
#. ``jvm.options`` for configuring Elasticsearch JVM settings
#. ``log4j2.properties`` for configuring Elasticsearch logging

.. csv-table::
   :header: "Setting", "Description"
   :widths: 20, 100
   :delim: #

    xpack.graph.enabled       # enable graph learning or not
    xpack.ml.enabled          # enable machine learning or not
    xpack.monitoring.enabled  #
    xpack.reporting.enabled   #
    xpack.security.enabled    #
    xpack.watcher.enabled     #


RECOMMENDED SYSTEM ENV SETTING
-----------------------------------

.. note:: SET_ENV: ``C:\Windows\System32\SystemPropertiesProtection.exe``

The ``.zip`` package is entirely self-contained. All files and directories are,

by default, contained within :mark:`ES_HOME` -- the directory created when unpacking the archive.


.. csv-table::
   :header: "Type", "Description", "Default Location", "Setting"
   :widths: 10, 40, 40, 30
   :delim: |

    home|    Elasticsearch home directory or ``%ES_HOME%``|  Directory created by unpacking the archive|
    bin| Binary scripts including ``elasticsearch`` to start a node and ``elasticsearch-plugin`` to install plugins| ``%ES_HOME%\bin``
    conf| Configuration files including ``elasticsearch.yml``| ``%ES_HOME%\config``| `ES_PATH_CONF <https://www.elastic.co/guide/en/elasticsearch/reference/current/settings.html#config-files-location>`_
    data| The location of the data files of each index / shard allocated on the node. Can hold multiple locations.| ``%ES_HOME%\data`` | path.logs
    plugins| Plugin files location. Each plugin will be contained in subdirectory.| ``%ES_HOME%\plugins``
    repo| Shared file system repository locations. Cann hold multiple locations. Afile system repository can be placed in to any subdirectory of any directory specified here.| Not configured| path.repo


`Logstash Install <https://www.elastic.co/cn/downloads/logstash>`_
=========================================================================

Installation steps
---------------------

1. `Download Logstash <https://www.elastic.co/cn/downloads/logstash>`_
#. Prepare a :mark:`logstash.conf` **config file**

        1. demo-01::

            input { stdin { } }
            output {
              elasticsearch { hosts => ["localhost:9200"] }
              stdout { codec => rubydebug }
            }

        #. demo-02: After receiving the content produced by the 5200 port, output it to Elasticsearch storage::

            input {
                tcp {
                    port => 5000
                }
            }

            output {
                elasticsearch {
                    hosts => "localhost:9200"
                }
            }

#. Run ``bin/logstash -f logstash.conf``

    * ERROR:
        - could not find java; set JAVA_HOME or ensure java is in PATH::

            JAVA_HOME = C:\Program Files\Java\jdk1.7.0_25
            PATH = C:\Program Files\Java\jdk1.7.0_25\bin

        |ss|
        - could not find jruby in D:\logstash-7.5.2\vendor\jruby

            1. `download JRuby 9.2.9.0 Windows Executable (md5, sha1, sha256) <https://www.jruby.org/download>`_
            #. edit ``logstash-7.5.2\bin\setup.bat``::

                set JRUBY_BIN="%LS_HOME%\vendor\jruby\bin\jruby"  -> set JRUBY_BIN="%LS_HOME%\vendor\bundle\jruby\2.5.0\bin"

        |se|

        - :strike:`LoadError: no such file to load -- bundler` (see `Support Matrix`_)

            |ss|
            1. cd C:\jruby-9.2.9.0\bin
            #. ``jruby -S gem install bundler``

            .. note:: check: ``jruby -S gem list``

            |se|

    .. note:: quickly test: ``logstash -e 'input{stdin{}}output{stdout{codec=>rubydebug}}'``

Kibana Install
===================

Installation steps

1. `Download Kibana <https://www.elastic.co/cn/downloads/kibana>`_
#. Open ``config/kibana.yml`` in an editor
    - server.port: 5601
    - server.host: "localhost"

# Run ``bin/kibana`` (or ``bin\kibana.bat`` on Windows)
# Point your browser at http://localhost:5601 (by step 2)

REFERENCE
===================

* https://kknews.cc/zh-tw/code/qljaxbb.html
* http://netkiller.sourceforge.net/monitoring/elk/logstash.html
* https://blog.johnwu.cc/article/elk-logstash-grok-filter.html
* https://oranwind.org/dv-elk-an-zhuang-ji-she-ding-jiao-xue/
* https://www.jianshu.com/p/ef6a57309c72
* https://doc.yonyoucloud.com/doc/logstash-best-practice-cn/get_start/full_config.html
* https://www.elastic.co/guide/en/logstash/current/running-logstash-windows.html
* https://www.elastic.co/cn/support/matrix#matrix_jvm
* https://blog.johnwu.cc/article/how-to-install-elasticsearch-logstash-and-kibana-elk-stack-on-centos-red-hat.html
* https://www.slideshare.net/kedych/elk-stack-kibana

.. _Support Matrix: https://www.elastic.co/cn/support/matrix#matrix_jvm