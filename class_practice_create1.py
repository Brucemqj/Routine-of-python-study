# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 00:04:09 2017

@author: 风落雨
"""

#In this script, I will create some classes for practicing
import math

class Point(object):
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        
    def getPos(self, choice):
        choice_item = ['x','y','z']
        if choice in choice_item:
            if choice == 'x':
                return self.x
            elif choice == 'y':
                return self.y
            else:
                return self.z
        else:
            return ValueError
 
class Line(object):
    def __init__(self, p1, p2):
        if isinstance(p1, Point) and isinstance(p2, Point):
            self.x = p1.getPos('x') - p2.getPos('x')
            self.y = p1.getPos('y') - p2.getPos('y')
            self.z = p1.getPos('z') - p2.getPos('z')
            
            self.len = math.sqrt(self.x ** 2 + self.y ** 2 + \
                                 self.z ** 2)
        else:
            return ValueError
            
    def getLen(self):
        return self.len
        
p1 = Point(1,2,3)
p2 = Point(2,2,4)
line = Line(p1, p2)
print(line.getLen())


#Compare two words by its length
class Word(str):
    def __new__(cls, word):
        if ' ' in word:
            print('Word contains space, truncated to first space')
            word = word[:word.index[' ']]
        return str.__new__(cls, word)
    
    def __gt__(self, other):
        return len(self) > len(other)
    def __lt__(self, other):
        return len(self) < len(other)
    def __ge__(self, other):
        return len(self) >= len(other)
    def __le__(self, other):
        return len(self) <= len(other)

























