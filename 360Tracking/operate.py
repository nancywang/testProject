__author__ = 'Admin'
#-*- coding:utf-8 -*-
import os
import constant
# import datetime

base_path = constant.BASE_PATH
test_date = constant.DATE

base_name = constant.BASE_NAME
extension_name = constant.EXTENSION_NAME
test_hour = constant.HOUR
final_name = base_name+test_hour+extension_name

dir_path = os.path.join(base_path, test_date)
file_path = os.path.join(dir_path, final_name)


def check_dir():
        if os.path.exists(dir_path) is True:
            return True
        else:
            return False

def create_dir():
        if True:
            os.mkdir(os.path.join(base_path, test_date))
            return dir_path
        else:
            return False

def check_file():
        for  filename in os.listdir(dir_path):
            if cmp(final_name, filename) == 0 :
                return True
        else:
            return False

def create_file():
         if os.path.exists(file_path) is False:
            f = open(os.path.join(dir_path, final_name), 'w+')
            f.close()
            return final_name


def create_data():
     f = open(file_path, 'w+')
     li = constant.DATA_DICT
     for i in li:
         f.writelines(i)
     # print f.readlines()
     f.close()

class data_file:
    # 定义基本属性
    TIME = 0 ,
    IP = '',
    LP = '',
    UA = '',
    UID = '',
    SID = 0,
    SCREEN = '',
    LANGUAGE = '',
    URL = '',
    REF_URL = '',
    KEYWORD_ID = 0,
    CREATIVE_ID = 0,
    QIHU_UID = 0
    def __init__(self, time, ip, lp, ua, uid, sid, screen, language, url, ref_url, keyword_id, creative_id, qihu_uid):
        self.TIME = time
        self.IP = ip
        self.LP = lp
        self.UA = ua
        self.UID = uid
        self.SID = sid
        self.SCREEN = screen
        self.LANGUAGE = language
        self.URL = url
        self.REF_URL = ref_url
        self.KEYWORD_ID = keyword_id
        self.CREATIVE_ID = creative_id
        self.QIHU_UID = qihu_uid