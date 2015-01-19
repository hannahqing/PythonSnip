__author__ = 'qing'
"""
getopt:shortopts ,-h or -i
       longopts,--help
excute command lines:
python getopt_test.py -h
python getopt_test.py -i 10.10.13.12 -p 9090
python getopt_test.py --ip=10.10.13.12 --port=9090
"""
import sys,getopt
try:
    options,args=getopt.getopt(sys.argv[1:],"hi:p:",["help","ip=","port="])
except getopt.GetoptError:
    sys.exit()
for name,valus in options:
    if name in ("-h","--help"):
        print "-i or --ip: input ip"
        print "-p or --port:input port"
    elif name in ("-i","--ip"):
        print "ip=",valus
    elif name in ("-p","--port"):
        print "port=",valus
for i in range(len(args)):
    print args[i]
