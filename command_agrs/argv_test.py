__author__ = 'qing'
#separate with commar
#python argv_test.py hello world
import sys
print "script name:",sys.argv[0]
for i in range(1,len(sys.argv)):
    print "arguments",i,sys.argv[i]

