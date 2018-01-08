#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import re

list = []
files = glob.glob('/Users/starnight/Downloads/weblogic/*.html')
for f in files:
    print 'processing ', f
    with open(f, 'r') as fr:
        content = fr.read()
        raw_list = re.findall('search-result-item-title(.*)?target', content)
        for i in raw_list:
            link = i[8:-3]
            print link
            list.append(link)

print '[*]All %d lines in total' % len(list)
file_name = raw_input('[*]please input file name to save [just name no suffix] : ')
if file_name == '':
    file_name = 'result.txt'

with open(file_name + '.txt', 'w') as fw:
    for line in list:
        fw.write(line + '/\n')
    print 'Data saved to file %s.txt' % file_name
