# !/usr/bin/env python3.8
# import os
# # Access all environment variables
# print('*----------------------------------*')
# total = os.environ
# # print(my_dict)
#
# '''
# Iterate over a sorted list of keys and select value from dictionary for each key
# and print the key value pairs in sorted order of keys
# '''
# for key in sorted(total.keys()) :
#     print(key , " :: " , total[key])


# def count_vowls(inputStr):
#     return sum(1 for let in inputStr if let in "aeiouAEIOU")


# def array_diff(a, b):
#      result = set(a) - set(b)
#      return list(result)

# print(array_diff([1,2,2,2,3],[2]))


from collections import Counter
import re
def word_frequency(str1):
     list1 = str1
     counts = Counter(list1)
     sorted_words = dict(counts.most_common() )
     return sorted_words

def read_file(file_name,mine,res_file):
     sorted_data = None
     sorted_data2 = None
     with open(file_name) as file:
          data = file.read()
          edited = data.strip().split()
          word_result = word_frequency(edited)

          data_set = set(word_result)
     with open(mine) as file2:
          data2 = file2.read().lower()
          edited2 = data2.strip().split()
          data_set2 = set(edited2)
     result = data_set - data_set2
    #  import ipdb ; ipdb.set_trace()

     a = dict.fromkeys(edited)
     b = dict.fromkeys(edited2)
     ordered_result = dict.fromkeys(x for x in a if x not in b)
     for elem,counter in word_result.items():
         if elem in result:
            with open(res_file,'a') as file3:
               file3.write(f"\n {elem} :{counter} ")
    #  for elem in ordered_result:
    #     with open(res_file,'a') as file3:
    #         file3.write(f"\n {elem} ")
     
     return result

import cProfile, pstats, io,sys
import time


def profile(fnc):
    
    """A decorator that uses cProfile to profile a function"""
    
    def inner(*args, **kwargs):
        
        pr = cProfile.Profile()
        pr.enable()
        retval = fnc(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        # get memory used by obj 
        # sys.getsizeof(obj)
        print(s.getvalue())
        return retval

    return inner

# @profile

# def computation():
#     a = range(int(1e6))
#     b = range(int(1e6))
#     result = 0
#     for x, y in zip(a, b):
#         result += x + y
#     return result






# def myfunc(x:int,y:int) -> int:

import json 
import re

# @profile
def main():
    test_str = """
    so hello world! how are you ? every thing will be fine so to speak with you
    """
    file1_path = '/home/hima/Downloads/Video/blog/test.txt'
    file2_path = '/home/hima/Downloads/Video/blog/test2.txt'
    file3_path = '/home/hima/Downloads/Video/blog/result.txt'

    file_result = read_file(file1_path,file2_path,file3_path)
    # import ipdb ; ipdb.set_trace()
    # return result

    

# if __name__ == '__main__':
#     main()

# TODO: use cpython instead of this decrator once i can fix the wiered results that appears


from typing import NamedTuple
class C4(NamedTuple):
    x :int
    y:int =1
    z:int = 2

# >>> c4 = C4(1)
# >>> c4
# C4(x=1, y=1, z=2)
# >>> type(c4)
# <class '__main__.C4'>
# >>> c4 = C4(1,3)
# >>> c4
# C4(x=1, y=3, z=2)



# provide default value if u trying access values that doesn't exist
import collections

dct = collections.defaultdict(int)
#  dct['a']
# 0
# >>> dct['b'] += 2
# >>> dct
# defaultdict(<class 'int'>, {'a': 0, 'b': 2})
dct2 = collections.defaultdict(int,{'a':2,'b':3})
# dct2['a']
# 2

