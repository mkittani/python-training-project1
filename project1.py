'''{ Qs3
def unique(s):
    s=s.replace(" ","")
    s=s.lower()
    myDict={}
    for i in s:
        if i not in myDict:
            myDict[i]=1
        else:
            myDict[i]+=1
    for i in myDict:
        if myDict[i]==1:
            return i
print(unique("Name naMag"))
}'''
'''{ Qs2
from datetime import date as dt
class student:
    def __init__(self,name,age,id):
        self.name=name
        self.age=age
        self.id=id
        print("New student registration:\nName: {}\nAge: {}\nID: {}".format(self.name,self.age,self.id))
    @staticmethod
    def underGrad(age):
        if age<18:
            return True
        else:
            return False
    @classmethod
    def studentSince(cls,name,year,id):
        print("""Student name: {} and been a student in our university for: {} years and carries the id: {}""".format(name,dt.today().year - year,id))

s1=student("ali",20,12099100)
s2=student("mohamad",22,12115142)

print(student.underGrad(17))
print(student.underGrad(20))

student.studentSince("Sara",2020,12099100)
}'''
'''{
import time
import functools
def timer(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        old_value=time.perf_counter()
        result=func(*args,**kwargs)
        new_value=time.perf_counter()
        runTime=new_value-old_value
        print("Runtime using the timer decorator= {}".format(runTime))
        return result
    return wrapper

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(200)])
waste_some_time(100)


import timeit
code='''
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(200)])
'''
print("Runtime using the timeit module=",timeit.timeit(stmt=code,number=100))
}'''