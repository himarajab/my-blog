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

# import getpass
# print(getpass.getuser())

# def count_vowls(inputStr):
#     return sum(1 for let in inputStr if let in "aeiouAEIOU")







# def array_diff(a, b):
#      result = set(a) - set(b)
#      return list(result)

# print(array_diff([1,2,2,2,3],[2]))




# from collections import Counter
# import re
# # >>> words = re.findall(r'\w+', open('hamlet.txt').read().lower())
# def word_frequency(str1):
#      list1 = str1.split()
#      counts = Counter(list1)
#      sorted_words = dict(counts.most_common() )
#      return sorted_words



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
import nltk.data
# nltk.download('punkt')
# @profile
def main():
    test_str = """
    hello world!how are u?every thing will be fine\nso to speak
    """
 
    # data = re.split('([?\n])', test_str.strip())
    
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    fp = open("/home/hima/Downloads/Video/blog/test.txt")
    data = fp.read()
    final_data = tokenizer.tokenize(data)
    print(final_data[2],type(final_data))    
    # return res_dct 
          
    # print(f'{type(e).__name__}: {e} ')


if __name__ == '__main__':
    main()

# TODO: use cpython instead of this decrator once i can fix the wiered results that appears