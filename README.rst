sitemap: python3 sitemap generators.
====================================
.. image:: https://travis-ci.org/gamelife1314/sitemap.svg?branch=master
    :target: https://travis-ci.org/gamelife1314/sitemap
.. image:: https://img.shields.io/badge/python-3.5,3.6-blue.svg
    :target: https://github.com/gamelife1314/sitemap

Install
-------

via pip ::

    pip install apsitemap


Documentation:

view help::

    > apsitemap --help
         _ _
     ___(_) |_ ___ _ __ ___   __ _ _ __    author:   gamelife1314
    / __| | __/ _ \ '_ ` _ \ / _` | '_ \   homepage: https://github.com/gamelife1314/sitemap
    \__ \ | ||  __/ | | | | | (_| | |_) |  email:    fudenglong1417@gmail.com
    |___/_|\__\___|_| |_| |_|\__,_| .__/   version:  0.1
                                  |_|

    Usage:
        sitemap-tool  <domain> [options]

    Options:
        -h, --help     view help.
        -v, --version  view version.

    UslSet Options:
        --changefreq <changefreq>   set the update frequency of site. eg: always, hourly, daily, weekly, monthly.
        --lastmod <lastmod>         set the last modified time. eg: 2016-06-30.
        --xml-file <xmlfile>        set the name of xmlfile.[default: sitemap.xml]
        --txt-file <xmlfile>        set the name of xmlfile.[default: sitemap.txt]

    Log options:
        --log-level <level>         set log level, eg: DEBUG, INFO, ERROR, WARNING, CRITICAL.[default: DEBUG]


example::

    apsitemap http://blog.fudenglong.site/ --log-level info --changefreq weekly --lastmod 2017-07-01
    apsitemap http://blog.fudenglong.site/

