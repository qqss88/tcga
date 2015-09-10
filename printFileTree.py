#!/usr/bin/python

import os

# traverse root directory, and list directories as dirs and files as files
def list():
    for root, dirs, files in os.walk("."):
        path = root.split('/')
        print (len(path) - 1) *'---' , os.path.basename(root)       
        for file in files:
            print len(path)*'---', file

if __name__ == '__main__':
    list()
