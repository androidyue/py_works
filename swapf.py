#!/usr/bin/env python
# coding=utf-8
# author:andrewallanwallace@gmail.com
'''
This simple script is written for easily swap two files or two folders.
'''


def swap(origin, dest, temp):
    '''
    Swap files 
    mv origin temp
    mv dest origin
    mv temp dest
    '''
    from os import system
    origin2Temp = 'mv -f -v %s %s'%(origin, temp)
    system(origin2Temp)
    
    dest2Origin = 'mv -f -v %s %s'%(dest, origin)
    system(dest2Origin)

    temp2Dest = 'mv -f -v %s %s'%(temp, dest)
    system(temp2Dest)


def shouldSwap(origin, dest):
    from os import path
    
    originExists = path.exists(origin)
    destExists = path.exists(dest)

    if(not originExists or not destExists):
        print 'Both the files should be existing %s existing State = %s ; %s existing State = %s'%(origin, str(originExists), dest, str(destExists))
        return False 
    
    originIsDir = path.isdir(origin)
    destIsDir = path.isdir(dest)

    if (originIsDir != destIsDir):
        print 'the two files should be the same type %s is dir = %s ;%s is dir = %s'%(origin, str(originIsDir), dest, str(destIsDir))
        return False
    return True
        

def main():
    '''
    Usage:swapf.py origin dest [temp]
    '''
    import sys
    paramsSize = len(sys.argv)
    
    origin = None
    dest = None
    temp = 'temp_backup.file'

    if (paramsSize < 3):
        print main.__doc__
        return

    origin = str(sys.argv[1])
    dest = str(sys.argv[2])


    if (paramsSize == 4):
        temp = str(sys.argv[3])


    if (shouldSwap(origin, dest)):
        swap(origin, dest, temp)



main()
