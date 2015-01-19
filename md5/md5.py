# -*- coding: utf-8 -*-
__author__ = 'qing'
import hashlib
class Start(object):
    def __init__(self):
        pass
    def cal_md5(self,filepath):
        m=hashlib.md5()
        f=file(filepath,'rb')
        while True:
            d=f.read(8096)
            if not d:
                break
            m.update(d)
        return m.hexdigest()
if __name__=="__main__":
    f=r"D:\youku\alipay_5913.apk"
    obj=Start()
    print obj.cal_md5(f)