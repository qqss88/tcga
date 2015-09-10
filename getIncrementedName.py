#! /usr/bin/python
import sys
#import fasta

#by Qiang Sun@01/16/2014
"""
Python Script #2:
Short Desc:         Provides name of incremented revision of an archive
Input:                    increment_amount, archive_name
Output:                incremented_archive_name
Example:             getIncrementedName.py 1 nationwidechildrens.org_LGG.bio.Level_2.0.1.0
Script Loc.:          /tcga_team/QA/automation/framework/utilities/pythonScripts
Details:
Running the example above would generate this string:
nationwidechildrens.org_LGG.bio.Level_2.0.2.0
"""

#this script help remove duplicated sequence from input fsata file and 
#generate a fasta file with unique set of sequences
#a map file will also be generated to keep the mapping info 


        



if ( len(sys.argv[:]) < 3  or len(sys.argv[:]) > 4 )  and __name__ == '__main__':
     print 'USAGE getIncrementedName increment_amount archive_name\n'
    
elif  __name__ == '__main__':

    amount = int(sys.argv[1])
    print 'this is your new name:\n'
    print '.'.join(sys.argv[2].split('.')[:-2])+'.'+str(int(sys.argv[2].split('.')[-2])+amount)+'.'+sys.argv[2].split('.')[-1]
