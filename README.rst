sitemap: python3 sitemap generators.
====================================

Install
-------

via pip ::

    pip3 install https://github.com/gamelife1314/sitemap/archive/master.zip
via source code ::

    python3 setup.py install


Documentation:

view help::

    > sitemap-tool --help
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

    Log options:
        --log-level <level>         set log level, eg: DEBUG, INFO, ERROR, WARNING, CRITICAL.[default: DEBUG]

example::

    sitemap-tool http://blog.fudenglong.site/ --log-level info --changefreq weekly --lastmod 2017-07-01
    sitemap-tool http://blog.fudenglong.site/
