#!/usr/bin/env python
# coding=utf-8




def compareXmls(src, dest) :
    try:
        import xml.etree.cElementTree as ET
    except ImportError:
        import xml.etree.ElementTree as ET

    srcRoot = ET.ElementTree(file=src).getroot()
    destRoot = ET.ElementTree(file=dest).getroot()
    
    srcNames = []
    for srcChild in srcRoot:
        srcAttribe = srcChild.attrib
        if (None != srcAttribe):
            srcNames.append(srcAttribe.get('name')) 
        
    destNames = []
    for destChild in  destRoot:
        destAttribe = destChild.attrib
        if (None != destAttribe):
            destNames.append(destAttribe.get('name'))
        

    
    decreasings = []
    increasings = []

    for srcItem in srcNames:
        if(srcItem in destNames):
            continue
        decreasings.append(srcItem)

    for destItem in destNames:
        if (destItem in srcNames) :
            continue
        increasings.append(destItem)
    
    return srcNames,destNames,increasings,decreasings

def testCompareXmls():
    src = '/home/androidyue/temp/strings_original.xml' 
    dest = '/home/androidyue/temp/strings_crowdin.xml'
    print compareXmls(src, dest)


if __name__ == '__main__':
    from sys import argv
    if (len(argv) != 3):
        print 'Usage compareXmls.py file1 file2'
    else:
        srcSet,destSet,increasings,decreasings = compareXmls(argv[1], argv[2])
        print 'increasings = ',increasings
        print 'decreasings = ',decreasings
        
