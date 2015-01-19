# -*- coding: utf-8 -*-
__author__ = 'qing'
"""
reference:http://www.cnblogs.com/coser/archive/2011/12/14/2287739.html

"""
import json
class JsonTest(object):
    def __init__(self):
        pass
    #dumps :decode the simple data:tuple to array
    #loads :string to unicode
    def dumps_test(self):
        obj = [[1,2,3],123,123.123,'abc',{'key1':(1,2,3),'key2':(4,5,6)}]
        encoded_obj=json.dumps(obj)
        print repr(obj),type(obj)
        print encoded_obj,type(encoded_obj)
        #load encode file_object;loads encode string
        decode_obj=json.loads(encoded_obj)
        print type(decode_obj)
        print decode_obj
        print decode_obj[4]['key1']
    def dumps_agrs(self):
        data1 = {'b':789,'c':456,'a':123}
        data2 = {'a':123,'b':789,'c':456}
        d1=json.dumps(data1,sort_keys=True)
        d2=json.dumps(data2)
        d3=json.dumps(data2,sort_keys=True)
        print d1
        print d2
        print d3
        print d1==d2
        print d1==d3

        d4=json.dumps(data1,sort_keys=True,indent=4)
        print d4
        #separators 压缩数据
        print "repr(data1)              ",len(repr(data1))
        print "dumps(data1,separartors)",len(json.dumps(data1,separators=(",",":")))
    #字典
    def dic_test(self):
        dic_obj={"key1":{"key11":"abc","key12":123},"key2":"def"}
        print dic_obj
        if dic_obj.has_key("key1"):
            dic_obj['key1']["key11"]="def"
        print dic_obj
        print dic_obj.keys()
if __name__=="__main__":
    startObj=JsonTest()
    startObj.dic_test()
#    startObj.dumps_agrs()
#    startObj.dumps_test()
