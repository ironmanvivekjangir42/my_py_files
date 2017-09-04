#!/usr/bin/python3
n=int(input("enter n val:"))
for i in range(1,n+1):#creates an integer in range of 1,11
	for j in range(1,11):
		print(i ,'X', j,i*j)