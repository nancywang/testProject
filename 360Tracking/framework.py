#-*- coding:utf-8 -*-
import os
import datetime
import constant
import operate as op

# base_path = constant.BASE_PATH
# test_date = constant.DATE

def main():
#Create test dir
    if op.check_dir()  is True:
        print 'Test Dir  %s was exist' % op.dir_path
    else:
        print 'Creating Test Dir'
        print "="*80
        print 'Create Test Dir %s Succeed' % op.create_dir()
# Create Test Log File
    if op.check_file()  is True:
        print "Test Log File  %s  was exist" % op.file_path
    else:
        print "Creating Test Log File"
        print "="*80
        print "Create Test Log File  %s Succeed" % op.create_file()
# Create Test Data
    print "Starting to create test data"
    op.create_data()
    print "="*80
    print "Finished!"

#if __name__ == '__main__':
main()