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

#Function DecimalToBinary(number) convert decimal number to binary number
#Method below is circular one
def DecimaiToBinary_cir(number):
    def convert_opt(num):
        temp = []
        residue = num
        quotient = num
        while( quotient ): #If quotient is not zero, while loop will keep working
            residue = quotient % 2
            quotient = quotient // 2
            temp.append(residue)
        temp.reverse()
        result = ''
        for item in temp:
            result += str(item)
        return result
            
            
    str_num = str(number)
    str_num_twopart_list = str_num.split('.')
    length = len(str_num_twopart_list)
    integer_part = int(str_num_twopart_list[0])    
    if integer_part <= 0:
        integer_part = abs(integer_part)
        integer_part_to_b = convert_opt(integer_part)
        if length == 2:            
            fraction_part = int(str_num_twopart_list[1])
            fraction_part_to_b = convert_opt(fraction_part)
            return '-' + integer_part_to_b + '.' + fraction_part_to_b
        else:
            return '-' + integer_part_to_b
    else:
        integer_part_to_b = convert_opt(integer_part)
    if length == 2:            
        fraction_part = int(str_num_twopart_list[1])
        fraction_part_to_b = convert_opt(fraction_part)
        return integer_part_to_b + '.' + fraction_part_to_b
    else:
        return integer_part_to_b
    
#Method two is recursive one
def DecimaiToBinary_rec(number):
    if number == 0:
        return '0'
    elif number < 0:
        number = abs(number)
        res = ''
        if number:
            res = '-'+DecimaiToBinary_rec(number // 2)
            return  res + str(number % 2)
        else:
            return res
    else:
        res = ''
        if number:
            res = DecimaiToBinary_rec(number // 2)
            return res + str(number % 2)
        else:
            return res

#Convert a integer into a list
res = []
def integer_to_list(int_num):   
    if int_num > 0:
        res.insert(0, int_num % 10)
        integer_to_list(int_num // 10)
    return res

               
    


   
    
    
    
    
    
    
    
    