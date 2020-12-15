# # !/usr/bin/env python3.8
# # import os
# # # Access all environment variables
# # print('*----------------------------------*')
# # total = os.environ
# # # print(my_dict)
# #
# # '''
# # Iterate over a sorted list of keys and select value from dictionary for each key
# # and print the key value pairs in sorted order of keys
# # '''
# # for key in sorted(total.keys()) :
# #     print(key , " :: " , total[key])


# # def count_vowls(inputStr):
# #     return sum(1 for let in inputStr if let in "aeiouAEIOU")


# # def array_diff(a, b):
# #      result = set(a) - set(b)
# #      return list(result)

# # print(array_diff([1,2,2,2,3],[2]))


# from collections import Counter
# import re
# def word_frequency(str1):
#      list1 = str1
#      counts = Counter(list1)
#      sorted_words = dict(counts.most_common() )
#      return sorted_words

# def read_file(file_name,mine,res_file):
#      sorted_data = None
#      sorted_data2 = None
#      with open(file_name) as file:
#           data = file.read()
#           edited = data.strip().split()
#           word_result = word_frequency(edited)

#           data_set = set(word_result)
#      with open(mine) as file2:
#           data2 = file2.read().lower()
#           edited2 = data2.strip().split()
#           data_set2 = set(edited2)
#      result = data_set - data_set2
#     #  import ipdb ; ipdb.set_trace()

#      a = dict.fromkeys(edited)
#      b = dict.fromkeys(edited2)
#      ordered_result = dict.fromkeys(x for x in a if x not in b)
#      for elem,counter in word_result.items():
#          if elem in result:
#             with open(res_file,'a') as file3:
#                file3.write(f"\n {elem} :{counter} ")
#     #  for elem in ordered_result:
#     #     with open(res_file,'a') as file3:
#     #         file3.write(f"\n {elem} ")
     
#      return result

# import cProfile, pstats, io,sys
# import time


# def profile(fnc):
    
#     """A decorator that uses cProfile to profile a function"""
    
#     def inner(*args, **kwargs):
        
#         pr = cProfile.Profile()
#         pr.enable()
#         retval = fnc(*args, **kwargs)
#         pr.disable()
#         s = io.StringIO()
#         sortby = 'cumulative'
#         ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
#         ps.print_stats()
#         # get memory used by obj 
#         # sys.getsizeof(obj)
#         print(s.getvalue())
#         return retval

#     return inner

# # @profile

# # def computation():
# #     a = range(int(1e6))
# #     b = range(int(1e6))
# #     result = 0
# #     for x, y in zip(a, b):
# #         result += x + y
# #     return result






# # def myfunc(x:int,y:int) -> int:

# import json 
# import re

# # @profile
# def main():
#     test_str = """
#     so hello world! how are you ? every thing will be fine so to speak with you
#     """
#     file1_path = '/home/hima/Downloads/Video/blog/test.txt'
#     file2_path = '/home/hima/Downloads/Video/blog/test2.txt'
#     file3_path = '/home/hima/Downloads/Video/blog/result.txt'

#     file_result = read_file(file1_path,file2_path,file3_path)
#     # import ipdb ; ipdb.set_trace()
#     # return result

    

# # if __name__ == '__main__':
# #     main()

# # TODO: use cpython instead of this decrator once i can fix the wiered results that appears


# from typing import NamedTuple
# class C4(NamedTuple):
#     x :int
#     y:int =1
#     z:int = 2

# # >>> c4 = C4(1)
# # >>> c4
# # C4(x=1, y=1, z=2)
# # >>> type(c4)
# # <class '__main__.C4'>
# # >>> c4 = C4(1,3)
# # >>> c4
# # C4(x=1, y=3, z=2)



# # provide default value if u trying access values that doesn't exist
# import collections

# dct = collections.defaultdict(int)
# #  dct['a']
# # 0
# # >>> dct['b'] += 2
# # >>> dct
# # defaultdict(<class 'int'>, {'a': 0, 'b': 2})
# dct2 = collections.defaultdict(int,{'a':2,'b':3})
# # dct2['a']
# # 2


## ***********
# my_int = int(input('inter integer '))

# print(f'\n{my_int +4}\n')

# # Complete the solve function below.
# def solve(meal_cost, tip_percent, tax_percent):
#     tip = meal_cost / 100 * tip_percent
#     tax = meal_cost / 100 * tax_percent

#     total_cost = meal_cost + tip +tax
#     print(round(total_cost))

# if __name__ == '__main__':
#     meal_cost = float(input())

#     tip_percent = int(input())

#     tax_percent = int(input())

#     solve(meal_cost, tip_percent, tax_percent)



import math
import os
import random
import re
import sys



# if __name__ == '__main__':
#     N = int(input())
#     if N %2 != 0:
#       print('Weird')
#     elif N %2 ==0 and N >2 and N <=5:
#       print('Not Weird')
#     elif N %2 ==0 and N >6 and N <=20:
#       print('Weird')
#     elif N %2 ==0 and N >20:
#       print('Not Weird')



# class Person:
#     def __init__(self,initialAge):
#         # Add some more code to run some checks on initialAge
#         if initialAge <0:
#           initialAge =0
#           print('Age is not valid, setting age to 0.')
#         self.age = initialAge
#     def amIOld(self):
#         # Do some computations in here and print out the correct statement to the console
#         if self.age < 13:
#           print('You are young.')
#         elif self.age >= 13 and self.age < 18:
#           print('You are a teenager.')
#         else:  
#           print('You are old.')
#     def yearPasses(self):
#         # Increment the age of the person in here
#         self.age +=1
        
# t = int(input())
# for i in range(0, t):
#     age = int(input())         
#     p = Person(age)  
#     p.amIOld()
#     for j in range(0, 3):
#         p.yearPasses()       
#     p.amIOld()
#     print("")


# if __name__ == '__main__':
#     n = int(input())
#     for i in  range(1,11):
#       print(f'{n}x{i}={n*i}')

# if __name__ == '__main__':
    # for i in range(int(input())): 
    #   s=input() 
    #   print(*["".join(s[::2]),"".join(s[1::2])])
    
    
    
    # * reverse array *
    # n = int(input())
    # arr = list(map(int, input().rstrip().split()))
    # my_reversed = arr[-1::-1]
    # print(*my_reversed)


  # * map search *
  # n = int(input())
  # name_numbers = [input().split() for _ in range(n)]
  # print(name_numbers)
  # phone_book = {k: v for k,v in name_numbers}
  
  # while True:
  #     try:
  #         name = input()
  #         if name in phone_book:
  #             print(f'{name}={phone_book[name]}')
  #         else:
  #             print('Not found')
  #     except:
  #         break

# * recursion *
# def factorial(n):
#   result = 1
#   if n <= 1:
#     return result
#   else:
#     result = n * factorial(n-1)
#     return result


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input())

#     result = factorial(n)

#     fptr.write(str(result) + '\n')

#     fptr.close()



# * binary numbers *

# if __name__ == '__main__':
#     n = int(input().strip())
#     result = bin(n)[2:]
#     # is string method takes '1101' and splits it into a list. We end up with ['11','1']
#     # len(max(['11','1'])) ==> the max() method is simply going to look for the biggest value. In this case the biggest one is '11'. '11' is passed to the len() method which just returns the length of the object in it. In this case the object is the string '11' which has two characters, so len('11') returns 2. Which in turn is also the longest consecutive amount of ones. 
#     print(len(max(result.split('0'))))



# * sum max sunglass arr in multi dimenational array *

# if __name__ == '__main__':
#     arr = []
#     for _ in range(6):
#         arr.append(list(map(int, input().rstrip().split())))
#     res = []
#     for x in range(0, 4):
#         for y in range(0, 4):
#             s = sum(arr[x][y:y+3]) + arr[x+1][y+1] + sum(arr[x+2][y:y+3])
#             res.append(s)

#     print(max(res))



# * inhertaince *


# class Person:
#   def __init__(self, firstName, lastName, idNumber):
#     self.firstName = firstName
#     self.lastName = lastName
#     self.idNumber =idNumber
#   def printPerson(self):
#     print("Name:", self.lastName + ",", self.firstName)
#     print("ID:", self.idNumber)

# class Student(Person):
#     def __init__(self,firstName,lastName,idNumber,scores):
#         Person.__init__(self, firstName, lastName, idNumber)
#         self.scores = scores

#     def calculate(self):
#         a=sum(self.scores)/len(self.scores)
#         grades = 'OEAPDT'
#         conditions = [
#         90 <= a <= 100, 80 <= a < 90, 70 <= a < 80, 
#         55 <= a < 70, 40 <= a < 55, a < 40
#           ]
    
#         for (condition, grade) in zip(conditions, grades):
#             if condition is True: return grade

# line = input().split()
# firstName = line[0]
# lastName = line[1]
# idNum = line[2]
# numScores = int(input()) # not needed for Python

# scores = list( map(int, input().split()) )


# s = Student(firstName, lastName, idNum, scores)
# s.printPerson()




# * abtstract class *
# from abc import ABCMeta, abstractmethod
# class Book(object, metaclass=ABCMeta):
#     def __init__(self,title,author):
#         self.title=title
#         self.author=author   
#     @abstractmethod
#     def display(self): 
#       pass

# #Write MyBook class
# class MyBook(Book):
#     price = 0
#     def __init__(self, title, author, price):
#         super(Book, self).__init__()
#         self.price = price 

#     def display(self):
#         print("Title: "+ title)
#         print("Author: "+ author)
#         print("Price: "+ str(price))

# title=input()
# author=input()
# price=int(input())

# new_novel=MyBook(title,author,price)

# new_novel.display()



# * scope *
# class Difference:
#     def __init__(self, a):
#         self.__elements = a

#     def computeDifference(self):
#       self.maximumDifference = abs(max(self.__elements) - min(self.__elements)) 
      
# # End of Difference class

# _ = input()
# a = [int(e) for e in input().split(' ')]

# d = Difference(a)
# d.computeDifference()

# print(d.maximumDifference)



# * exceptians *
# class Calculator:
#   def power(self,n,p):
#     if n <0 or p <0:
#       return 'n and p should be non-negative'
#     return pow(n,p)
# myCalculator=Calculator()
# T=int(input())
# for i in range(T):
#     n,p = map(int, input().split())
#     try:
#         ans=myCalculator.power(n,p)
#         print(ans)
#     except Exception as e:
#         print(e)   


# * interfaces *
# class AdvancedArithmetic(object):
#     def divisorSum(self,n):
#         raise NotImplementedError

# class Calculator(AdvancedArithmetic):
#     def divisorSum(self, n):
#       my_sum=0
#       for i in range(1,n+1):
#         val =n % i
#         if val == 0:
#           my_sum +=i
#       return my_sum   


# n = int(input())
# my_calculator = Calculator()
# s = my_calculator.divisorSum(n)
# print("I implemented: " + type(my_calculator).__bases__[0].__name__)
# print(s)

# import sys

#   def my_sort(my_arr):
#     numberOfSwaps=0
#     for i in range(len(my_arr)):
#       for j in range(len(my_arr)-1):
#         if my_arr[j] > my_arr[j+1]:
#           my_arr[j],my_arr[j+1] =my_arr[j+1],my_arr[j]
#           numberOfSwaps+=1
#     print(f'Array is sorted in {numberOfSwaps} swaps.') 
#     print(f'First Element:',end='')
#     print(my_arr[0]) 
#     print(f'Last Element:',end='')
#     print(my_arr[-1]) 

# n = int(input().strip())
# a = list(map(int, input().strip().split(' ')))
# my_sort(a)

# * prime *
# my_tries =int(input())

# def my_prime(num):
#   if num % 2 or num %3:
#     my_str = 'Not Prime'

#   else:
#     my_str = 'Prime'
#   return my_str

# for i in range(my_tries):
#   param = int(input())
#   # for j in range(2,param):
#   res = my_prime(param)
#   print(res)


# for _ in range(int(input())):
#   num = int(input())
#   if(num == 1):
#       print("Not prime")
#   else:
#       if(num % 2 == 0 and num > 2):
#           print("Not prime")
#       else:
#           for i in range(3, int(num**(1/2))+1, 2):
#               if num % i == 0:
#                   print("Not prime")
#                   break
#           else:
#               print("Prime")


# * nested logic *
# returned_date = input().split(' ')
# due_date = input().split(' ')

# def calculate_fine(due_date,returned_date):
#   fine=0
#   day =  int(returned_date[0])-int(due_date[0]) 
#   month =  int(returned_date[1])-int(due_date[1])  

#   year =  int(returned_date[2])-int(due_date[2])  
#   if year >0:
#     fine= 10000 
    
#     # return fine 
  
#   elif month >0:
    
#     fine= 500 * day
#     # return fine 

#   elif day >0:
#     fine= 15 * day
#     # return fine 
#   return fine
# if __name__ == '__main__':
#     res = calculate_fine(due_date,returned_date)
#     print(res)


# rd, rm, ry = [int(x) for x in input().split(' ')]
# ed, em, ey = [int(x) for x in input().split(' ')]

# if (ry, rm, rd) <= (ey, em, ed):
#     print(0)
# elif (ry, rm) == (ey, em):
#     print(15 * (rd - ed))
# elif ry == ey:
#     print(500 * (rm - em))
# else:
#     print(10000)


# * rgex *
# if __name__ == '__main__':
#     N = int(input())

#     for N_itr in range(N):
#         firstNameEmailID = input().split()

#         firstName = firstNameEmailID[0]

#         emailID = firstNameEmailID[1]
#         x = re.search("@gmail.com$", emailID)
#         if x is not None:
#           print(firstName )