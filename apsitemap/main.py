#!/usr/bin/env python3
# encoding: utf-8
from docopt import docopt

from .spider import Spider
from .urlset import UrlSet
from .utility import sitemap_log

_app_doc = """
     _ _                               
 ___(_) |_ ___ _ __ ___   __ _ _ __    author:   gamelife1314
/ __| | __/ _ \ '_ ` _ \ / _` | '_ \   homepage: https://github.com/gamelife1314/sitemap
\__ \ | ||  __/ | | | | | (_| | |_) |  email:    fudenglong1417@gmail.com
|___/_|\__\___|_| |_| |_|\__,_| .__/   version:  0.1
                              |_|    

Usage: 
    apsitemap  <domain> [options]  

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
"""


def main():
    args = docopt(_app_doc, version="0.2.3")
    sitemap_log.setLevel(args["--log-level"].upper())
    urlset = UrlSet(entry=args["<domain>"], changefreq=args["--changefreq"], lastmod=args["--lastmod"])
    spider = Spider(entry=args["<domain>"], urlset=urlset)
    spider.start()
    urlset.save_xml(args["--xml-file"])
    urlset.save_txt(args["--txt-file"])
    sitemap_log.info("Get %s urls", len(urlset))
