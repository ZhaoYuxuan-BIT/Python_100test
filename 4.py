#!/usr/bin/env python
#coding:utf8
year=int(raw_input("year:\n"))
month=int(raw_input("month:\n"))
day=int(raw_input("day:\n"))
months = [31,28,31,30,31,30,31,31,30,31,30,31]
sum = 0
if (year%4==0) or (year%400==0) and (year%100!=0):
	months[1]=29
for i in range(month-1):
	sum+=months[i]
sum+=day
print sum
