#!user/bin/python
#_*_ coding: UTF-8 _*_
#author:wangjuan
'''
print "hello world";
str='avddsdgsgsdg'
print str[3:9]
str=['a',123];
str1=[1]
print str[0:1];
print str * 2;
print str + str1
if(1==1):
    print  "it is true"
else:
    print "it is false"
a=10
if (a<0):
 print "a为负数"
elif (0<a<5):
 print "a为小于5的正数"
elif(5<= a <=10):
 print "a为5到10之间的数"
else:
 print "a为大于10的数"
count=0
while(count<9):
  print "the count is:",count
  count+=1
else :print "Good bye"
for letter in 'python':
 print 'letter is:',letter;
fruits=['apple','balaner','aplle']
for fruit in fruits:
 print "fruit is:",fruit
fruits=['a1','a2','a3']
for index in range(len(fruits)):
  print "fruit is:",fruits[index]
fruits=['a1','a2','a3']
a=len(fruits)
b=range(len(fruits))
print a,b
for num in range(10,20):
  for i in range(2,num):
     if num%i==0:
      j=num/i
      print "%d=%d*%d" %(num,i,j)
      break
  else:
   print num,"是一个质数"
for i in 'python':
   if i=='h':
    continue
   print "it is :",i
a=23.00
b=int(a)
print a,b
a=-10
print"绝对值是：",math.fabs(a)
print"绝对值是：",abs(a)
b=pow(2,3)
print b
var="we are farmily"
print "var[0]:",var[0]
print "更新字符串：",var[:4] + "wwww"
dict={'1':'列表'  ,'2':'元组'  ,'3':'字典'}
print dict['1']
import time
print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
import calendar
cal= calendar.month(2018,5)
print"五月份的日历如下："
print cal
def var(a,*b):
    print a;
    for var in b:
        print var;

var(4,2,3)
sum = lambda arg1,arg : arg1+arg;
print sum(10,20)
import mudol
mudol.support ("调用模块功能");
str=raw_input("请输入：")
print "你输入的内容是：",str;
import os
print os.getcwd()
'''
class employee:
    empcount=0
    def __init__(self,name,salary):
        self.name =name;
        self.salary =salary;
        employee.empcount +=1;

    def displayemployee(self):
        print "name:", self.name, ",salary:",self.salary;
emp1=employee("wangjaun",10000);
emp1.displayemployee();
