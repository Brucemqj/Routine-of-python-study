# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 00:04:11 2017

@author: 风落雨
"""

import time as t

class MyTimer(object):
    def __init__(self, fun_obj=None, run_time=1000):
        self.fun_obj = fun_obj
        self.run_time = run_time
        self.default_timer = t.perf_counter
        self.res = []
        self.unit = ['Year', 'Month', 'Day', 'Hour',
                     'Minute', 'Second']
        self.prompt = 'Initialized now'
        print(self.prompt)
        
    def __str__(self):
        return self.prompt
    
    __repr__ = __str__
        
    def __add__(self, other):
        prompt = 'Total running time'
        tot_time = []
        for i in range(6):
            tot_time.append(self.res[i] + \
                            other.res[i])
            if tot_time[i]:
                prompt += str(tot_time[i]) + self.unit[i]
        return prompt
        
    def start(self):
        print('Begin MyTimer now')
        self.begin = t.localtime()
        self.prompt = 'started'
    
    def stop(self):
        if self.prompt != 'started':
            print('Please start first')
        else:
            self.end = t.localtime()
            self._cal_period()
            print('End MyTimer now')
            print(self.prompt)
            
    
    def timing(self):
        self.begin = self.default_timer()
        for i in range(self.run_time):
            self.fun_obj()
            
        self.end = self.default_timer()
        last_time = self.end - self.begin
        self.prompt = 'fun running time is :'
        self.prompt += str(last_time)
    
    def set_timer(self, timer):
        if timer == 'processs_timer':
            self.default_timer = t.process_time
        elif timer == 'perf_counter':
            self.default_timer = t.perf_counter
        else:
            print('Choose one timer from process_time or \
                  perf_counter')
            
        
    
    def _cal_period(self):
        self.prompt = 'Total running time'
        for i in range(6):
            self.res.append(self.end[i]-self.begin[i])
            if self.res[i] :
                self.prompt +=str(self.res[i]) + self.unit[i]
                
if __name__ == '__main__':
    t1 = MyTimer()
    t1.start()
    t.sleep(3)
    t1.stop()
    