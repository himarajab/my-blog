# import cProfile
#
#
# def my_sum():
#     # print(1+2)
#     for i in range(10000):
#         print(i)
#
# cProfile.run('my_sum()')
#

# import getpass
# print(getpass.getpass())

import os
# print(os.environ['USER'])


def read_log(file_name):
    commited = is_committed(file_name)

    if commited:
            file = open(file_name, 'r')
            lines = file.read().splitlines()
            write_log(file_name,lines)
            file.close()

    else:
        return 'this file currently processing some data'


def write_log(file_name,lines):
    for line in lines:
        if not line:
            continue
    columns = [col.strip() for col in line.split(':') if col]
    # do something
    is_committed(file_name,commited=True)


def is_committed(file_name,commited=False):
    try:
        f = open(file_name)
        return commited
    except FileNotFoundError:
        return 'File does not exist'

