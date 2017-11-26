# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 12:14:31 2017

@author: 风落雨
"""
import random as r

legal_x = [0, 10]
legal_y = [0, 10]

class Turtle(object):
    def __init__(self, power=100):
        self.power = power
        self.velocity = [1,2,-1,-2]
        self.x = r.randint(legal_x[0], legal_x[1])
        self.y = r.randint(legal_y[0], legal_y[1])
        
    def move(self):
        #calculate new coordinates randomly
        new_x = self.x + r.choice(self.velocity)
        new_y = self.y + r.choice(self.velocity)
        
        #determine if the new coordinates is in the ranges
        if new_x < legal_x[0]:
            self.x = legal_x[0] - (new_x - legal_x[0])
        elif new_x > legal_x[1]:
            self.x = legal_x[1] - (new_x - legal_x[1])
        else:
            self.x = new_x
            
        if new_y < legal_y[0]:
            self.y = legal_y[0] - (new_y - legal_y[0])
        elif new_y > legal_y[1]:
            self.y = legal_y[1] - (new_y - legal_y[1])
        else:
            self.y = new_y
        
        #physicial strength deplete
        self.power -= 1
        
        return (self.x, self.y)
                
    def eat(self):
        self.power += 20
        if self.power > 100:
            self.power = 100

class Fish(object):
    def __init__(self):
        self.velocity = [1,2,-1,-2]
        self.x = r.randint(legal_x[0], legal_x[1])
        self.y = r.randint(legal_y[0], legal_y[1])
        
     def move(self):
        #calculate new coordinates randomly
        new_x = self.x + r.choice(self.velocity)
        new_y = self.y + r.choice(self.velocity)
        
        #determine if the new coordinates is in the ranges
        if new_x < legal_x[0]:
            self.x = legal_x[0] - (new_x - legal_x[0])
        elif new_x > legal_x[1]:
            self.x = legal_x[1] - (new_x - legal_x[1])
        else:
            self.x = new_x
            
        if new_y < legal_y[0]:
            self.y = legal_y[0] - (new_y - legal_y[0])
        elif new_y > legal_y[1]:
            self.y = legal_y[1] - (new_y - legal_y[1])
        else:
            self.y = new_y
        
        #physicial strength deplete
        self.power -= 1
        
        return (self.x, self.y)
    
turtle = Turtle()
fish = []
for i in range(10):
    new_fish = Fish()
    fish.append(new_fish)

while True:
    if not len(fish):
        print('All fished have been eaten, game over!')
        break
    if not turtle.power:
        print('turtle has exhausted the physicial strength!')
        
    pos = turtle.move()
    
    for each_fish in fish[:]:
        if each_fish.move() = pos:
            turtle.eat()
            fish.remove(each_fish)
            print('A fish has been eaten by turtle!')
        
        
        
        
        
        
        
        
        
        
    
