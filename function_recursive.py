# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 10:16:42 2017

@author: qijiang.ma
"""
#Function power(x,y) returns the result of x power of y.
def power(x, y):
    if y < 0:
        if x == 0:
            print('x shouldn\'t be zero in denominator')
            return ValueError
        else:
            if y == 1:
                return 1 / x
            else:
                return (1 / x) * power(x, y+1)
    elif y == 0:
        return 1
    else:
        if y == 1:
            return x
        else:
            return x * power(x, y-1)

#Function rat_count(month) return the number of rat which is a issue that if a
#couple of rats can give birth to two new rats a month while new born rats cannot give
#birth in the first month. The qustion is how many rats will be after a given
#number of month.
            
#Method 1 is a circular one.
def rat_count_circular(month):
    if month <=0:
        print('month is a positive number while you give a negtive')
        return ValueError
    else:
        temp = [1, 1]
        for i in range(month):
            t = temp[i] + temp[i+1]
            temp.append(t)
        return temp[month-1]

#Method 2 is a recursive one.
def rat_count_recur(month):
    if month <=0:
        print('month is a positive number while you give a negtive')
        return ValueError
    elif month == 1 or month == 2:
        return 1
    else:
        return rat_count_recur(month-1) + rat_count_recur(month-2)

#Function hanoi(n=1,a,b,c) is a solution of hanoi issue.
def hanoi(n=1,a='a',b='b',c='c'):
    if n == 1:
        print(a,'---->',c)
    else:
        #move the above n-1 plate from a to b while move the last one from a 
        #to c
        hanoi(n-1,a,c,b)
        print(a,'---->',c)
        hanoi(n-1,b,a,c)
        