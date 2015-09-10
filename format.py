#!/usr/bin/env python

import os,sys

#by charlie_sun@03/26/2014

"""
a script for running cgquery in batch mode
"""

"""
here is a demo if quick query result:

============================================================================
    Script Version                   : 2.1.8
    CGHub Server                     : https://cghub.ucsc.edu
    WebServices Interface Version    : 3.6
    REST Resource                    : /cghub/metadata/analysisDetail
    QueryString                      : filename=C347.TCGA-18-3406-01A-01D-0983-08.19.bam
    Output File                      : None
----------------------------------------------------------------------------
    Matching Objects                 : 1
============================================================================

    Analysis 1
        analysis_id                  : 0feaae9e-2ba2-4f07-94ca-bb54c136991e
        state                        : live
        last_modified                : 2014-03-26T02:50:02Z
        upload_date                  : 2011-01-14T20:00:00Z
        published_date               : 2011-02-03T20:00:00Z
        center_name                  : BI
        study                        : phs000178
        aliquot_id                   : d3320989-71fd-425b-933e-6e8528a016ed
        files
            file 1
                filename             : C347.TCGA-18-3406-01A-01D-0983-08.19.bam
                filesize             : 22925722439
                checksum             : 170b7a4788aae54d603e9e7ddab3fdb9
            file 2
                filename             : C347.TCGA-18-3406-01A-01D-0983-08.19.bam.bai
                filesize             : 8343272
                checksum             : 8c8ef64acd685144f0d9cd4eb3eff869
        sample_accession             : SRS105675
        legacy_sample_id             : TCGA-18-3406-01A-01D-0983-08
        disease_abbr                 : LUSC
        tss_id                       : 18
        participant_id               : 95b83006-02c9-4c4d-bf84-a45115f7d86d
        sample_id                    : 7a55a700-a706-443d-8bad-e70483c464f2
        analyte_code                 : D
        sample_type                  : 01
        library_strategy             : WXS
        refassem_short_name          : HG19_Broad_variant
        analysis_submission_uri      : https://cghub.ucsc.edu/cghub/metadata/analysisSubmission/0feaae9e-2ba2-4f07-94ca-bb54c136991e
        analysis_full_uri            : https://cghub.ucsc.edu/cghub/metadata/analysisFull/0feaae9e-2ba2-4f07-94ca-bb54c136991e
        analysis_data_uri            : https://cghub.ucsc.edu/cghub/data/analysis/download/0feaae9e-2ba2-4f07-94ca-bb54c136991e

    Summary of Matching Objects
        downloadable_file_count      : 2
        downloadable_file_size (GB)  : 21.36
        state_count
            live                     : 1


----------------------------------------------------------------------------
    All matching objects are in a downloadable state.
----------------------------------------------------------------------------

"""

#query_dic = {'1':'filename','2':'aliquot_id','3':'legacy_sample_id','4':'analysis_id','5':'participant_id'}
"""
if ( len(sys.argv[:]) < 3  or len(sys.argv[:]) > 3 )  and __name__ == '__main__':
     print 'USAGE cgquery.py file_name query_by(int value 1-5) \n'
     print '1 for filename, 2 for aliquot_id, 3 for legacy_sample_id, 4 for analysis_id, 5 for participant_id\n'
     print 'None for Everything\n'
""" 
if  __name__ == '__main__':

    file_name = sys.argv[1]
    #query_by = query_dic[sys.argv[2]]
    file_in = open(file_name, 'r')
    all_lines = file_in.readlines()
    file_in.close()
    
    file_out = open(file_name+'.ref', 'w')
    file_out.write('bam\tstate\tcenter\tuuid\n')
    one_line='' 
    for line in all_lines:
        if line.count('Query')!=0:
            file_out.write(one_line+'\n')
            one_line=line.strip().split('=')[1]+'\t'
        else:
            one_line = one_line+line.strip().split(':')[1]+'\t'
    file_out.write(one_line+'\n')
    file_out.close()
