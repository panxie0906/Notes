#-*- coding:utf-8 -*-

class TimeTypeError(TypeError):
    pass

class TimeValueError(ValueError):
    pass

class Time:
    _num = 0
    
    def __init__(self,hours,minutes,seconds):
        if not (hours in range(24) and minutes in range(60) and seconds in range(60)):
            raise TimeValueError(hours,minutes,seconds)
        if not (isinstance(hours,int) and isinstance(minutes,int) and isinstance(seconds,int)):
            raise TimeTypeError(hours,minutes,seconds)
        
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds
        
        Time._num = Time._num + 1
    
    def hours(self):
        return self._hours
    def minutes(self):
        return self._minutes
    def seconds(self):
        return self._seconds
    
    def __add__(self,another):
        seconds_carry = 0
        seconds = self._seconds + another.seconds()
        if seconds > 60:
            seconds_carry = 1
            seconds = seconds % 60
        
        minutes_carry = 0
        minutes = self._minutes + seconds_carry + another.minutes()
        if minutes > 60:
            minutes = 1
            minutes = minutes % 60   
            
        hours = minutes_carry +self._hours + another.hours()
        
        return Time(hours,minutes,seconds)
    
    
    def __lt__(self,another):
        if ((self._hours*3600+self._minutes*60+self._seconds) < 
            (another.hours()*3600+another.minutes()*60+another.seconds())):
            return True
        return False
        
    def __eq__(self,another):
        if (self._hours == another.hours() and 
            self.minutes == another.minutes() and
            self.seconds == another.seconds()):
            return True
        return False
    
    def __sub__(self,another):
             
        minutes_borrow = 0
        seconds = self._seconds - another.seconds()
        if seconds<0:
            seconds = -seconds
            minutes_borrow = 1
            
        hours_borrow = 0
        minutes = self._minutes - minutes_borrow - another.minutes()
        if minutes<0:
            minutes = -minutes
            hours_borrow = 1
            
        hours = self._hours - another.hours() - hours_borrow
        
    def __detail__(self):
        return '/'.join((str(self._hours),str(self._minutes),str(self._seconds)))
        
if __name__ == '__main__':
    t = Time(12,23,45)
    print(t.__detail__())
    t2 = Time(22,34,12)
    print(t.__lt__(t2))