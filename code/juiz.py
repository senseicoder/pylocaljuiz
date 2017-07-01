#! /usr/bin/env python

import os

def include(filename):
    if os.path.exists(filename): 
        execfile(filename)

class cLayersIdentifyFiles:
    def Analyse(self, sFilename):
        pass

rootdir = os.path.dirname(os.path.abspath(__file__)) + '/layers/identify_files/'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        execfile(os.path.join(subdir, file))
        cmp = os.path.splitext(file)
        className='c' + cmp[0]
        constructor = globals()[className]
        instance = constructor()
        instance.Analyse('/home/cedric/dark-matter-season-3-episode-1-english-37028.zip')

#one = cOne()
#one.hello()
#two = cTwo()
#two.hello()