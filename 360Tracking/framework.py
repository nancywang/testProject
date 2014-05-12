#-*- coding:utf-8 -*-
import os
import datetime
import constant
import operate as op

# base_path = constant.BASE_PATH
# test_date = constant.DATE

def main():
#创建测试目录
    if op.check_dir()  is True:
        print u"待测试目录 %s 已存在" % op.dir_path
    else:
        print u"正在创建待测试目录"
        print "="*80
        print u"测试目录 %s 创建成功" % op.create_dir()
# 创建测试文件
    if op.check_file()  is True:
        print u"待测试文件 %s 已存在" % op.file_path
    else:
        print u"正在创建待测试文件"
        print "="*80
        print u"测试文件 %s 创建成功" % op.create_file()
#创建测试数据
    print u"开始创建测试数据"
    op.create_data()
    print "="*80
    print "Finished!"


#if __name__ == '__main__':
main()