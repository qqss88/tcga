#!/usr/bin/env python

import os,sys
import re
#by charlie_sun@04/26/2014

"""
a script for scan files and search file content
"""

"""
if ( len(sys.argv[:]) < 3  or len(sys.argv[:]) > 3 )  and __name__ == '__main__':
     print 'USAGE cgquery.py file_name query_by(int value 1-5) \n'
     print '1 for filename, 2 for aliquot_id, 3 for legacy_sample_id, 4 for analysis_id, 5 for participant_id\n'
     print 'None for Everything\n'
""" 

def scan_file(dirName, fname):
    fin = open(os.path.abspath(dirName)+'/'+fname, 'r')
    all_lines=fin.readlines()
    fin.close()

    for aline in all_lines[1:]:#ignore the first line
        if aline.count('year')!=0:
            continue
        if aline.count('uuid')!=0:
            continue
        searchObj = re.search( r'20(0[0-9]|1[0-4])', aline)
        if searchObj:
            print os.path.abspath(dirName)+'/'+fname+': '+aline
      


def main():
 
    rootDir = '/Users/sunq3/tmp'
    #file_print='py$'
    for dirName, subdirList, fileList in os.walk(rootDir):
        print('Found directory: %s' % dirName)
        for fname in fileList:
            searchObj = re.search( r'xml$', fname, re.M|re.I)
            if searchObj:
   #print "searchObj.group() : ", searchObj.group()
                #print('\t%s' % fname)
                scan_file(dirName,fname)

if  __name__ == '__main__':
    main()
