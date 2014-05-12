__author__ = 'Admin'
import os
import constant

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
     print f.readlines()
     f.close()