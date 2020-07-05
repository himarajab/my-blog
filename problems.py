#!/usr/bin/env python3.8
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

# import getpass
# print(getpass.getuser())

# def count_vowls(inputStr):
#     return sum(1 for let in inputStr if let in "aeiouAEIOU")


# def count_vowels(string):
#     vowel_list = 'a','e','i','u','o'
#     vowel_count = 0

#     for char in string:
#         if char in vowel_list:
#             vowel_count += 1

#     if vowel_count:
#         return vowel_count
#     else:
#         return 'no vowels'


# res = count_vowels('for')
# print(res)



# def array_diff(a, b):
#      result = set(a) - set(b)
#      return list(result)

# print(array_diff([1,2,2,2,3],[2]))


# measure memory usage
# from pympler import asizeof
# simple = SimplePosition('London', -0.1, 51.5)
# slot = SlotPosition('Madrid', -3.7, 40.4)
# asizeof.asizesof(simple, slot)
# (440, 248)
# measures the speed of attribute access on a slots data class
# from timeit import timeit
# timeit('slot.name', setup="slot=SlotPosition('Oslo', 10.8, 59.9)", globals=globals())
# 0.05882283499886398


# from collections import Counter
# import re
# # >>> words = re.findall(r'\w+', open('hamlet.txt').read().lower())
# def word_frequency(str1):
#      list1 = str1.split()
#      counts = Counter(list1)
#      sorted_words = dict(counts.most_common() )
#      return sorted_words


# def read_file(file_name,mine):
#      with open(file_name) as file:
#           data = file.read()
#           edited = data.strip().lower().split()
#           data_set = set(edited)
#           # sorted_data = sorted(edited)
#      with open(mine) as file2:
#           data2 = file2.read()
#           edited2 = data2.split()
#           data_set2 = set(edited2)
#           # sorted_data2 = sorted(edited2)
#      result = data_set - data_set2
#      # print(result)
#      for elem in result:
#           with open(mine,'a') as file3:
#                file3.write(f"\n {elem}")
#      return result
# result = read_file('test.txt','mine.txt')
# TODO:read online files 

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


# def function1():
#     function2()
#     function3()


# def function2():
#     for _ in range(50):
#         computation()


# def function3():
#     computation()


# def main():
#     function1()


# def myfunc(x:int,y:int) -> int:
# def myfunc(x:int,y:int) -> int:
#     # num = 0
#     # while True:
#     #     yield num
#     #     num += 1
#     # z :int= 5

#     return x * y
# # def myfunc():
#     pass

# @profile
def main():
    start = 'asdf=5;'
    end = '123jasd'
    s = 'asdf=5;iwantthis123jasd'
    print (s[s.find(start)+len(start):s.rfind(end)])

    # return myfunc(5,6)
    # return myfunc(5,6)
        # print(f'{type(e).__name__}: {e} ')


if __name__ == '__main__':
    main()

# TODO: use cpython instead of this decrator once i can fix the wiered results that appears