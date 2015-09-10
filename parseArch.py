#!/usr/bin/env python

import sys

#by charlie_sun@01/16/2014

"""
Script specification provided by Steve Hunter@20140116

Archive naming convention:
<CenterName>_<Disease>.<Platform>.Level_<#>.<BatchNumber>.<RevisionNumber>.<ProjectID>
 
Python Script #1:
Short Desc:         Parses and returns the desired value from an archive name
Input:                    desired_component, archive_name
Output:                desired_component_value
Example:             parsearch.py 2 nationwidechildrens.org_LGG.bio.Level_2.0.1.0
Script Loc.:          /tcga_team/QA/automation/framework/utilities/pythonScripts
Details:
Running the example above would generate this string:
LGG
"""

#this script help remove duplicated sequence from input fsata file and 
#generate a fasta file with unique set of sequences
#a map file will also be generated to keep the mapping info 


        



if ( len(sys.argv[:]) < 2  or len(sys.argv[:]) > 3 )  and __name__ == '__main__':
     print 'USAGE parseArch archive_name desired_component(optional, int value 1-6) \n'
     print '1 for CenterName, 2 for Disease, 3 for Platform, 4 for Level, 5 for BatchNumber, 6 for RevisionNumber, 7 for ProjectID\n'
     print 'None for Everything\n' 
elif  __name__ == '__main__':

    archive_name = sys.argv[1]
    desired_comp = 0
    if len(sys.argv[:])==3:
        desired_comp = int(sys.argv[2])
    try:
        CenterName = archive_name.split('_')[0]
        Disease = '_'.join(archive_name.split('_')[1:-1]).split('.')[0]
        Platform = '_'.join(archive_name.split('_')[1:-1]).split('.')[1]
        Level = archive_name.split('_')[-1].split('.')[0]
        BatchNumber = archive_name.split('_')[-1].split('.')[1]
        RevisionNumber = archive_name.split('_')[-1].split('.')[2]
        ProjectID = archive_name.split('_')[-1].split('.')[3]
        all_comps = """
CenterName:%s
Disease:%s
Platform:%s
Level:%s
BatchNumber:%s
RevisionNumber:%s
ProjectID:%s
"""%(CenterName, Disease, Platform, Level, BatchNumber, RevisionNumber, ProjectID)
        print {0:all_comps,1:CenterName,2:Disease,3:Platform,4:Level,5:BatchNumber,6:RevisionNumber,7:ProjectID}.get(desired_comp)
    except:
        print 'please make sure you input a valid name.'  
