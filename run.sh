#! /bin/bash
#
# run.sh
# Copyright (C) 2015 truong-d <truong-d@ahcclp03>
#
# Distributed under terms of the MIT license.
#


export PKG_CONFIG_PATH=/home/is/truong-d/work/vidata/libffi-3.2.1/installed/lib/pkgconfig
export LD_LIBRARY_PATH=/home/is/truong-d/work/vidata/libffi-3.2.1/installed/lib/

#scrapy crawl vietnamnet_crawl -o items.json -s JOBDIR=crawls/vietnamnet_crawl LOG_FILE=scrapy.log
scrapy crawl vietnamnet_crawl -o items.json -s JOBDIR=crawls/vietnamnet_crawl -s LOG_FILE=scrapy.log
