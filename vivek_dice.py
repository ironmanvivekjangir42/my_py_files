#!/usr/bin/python3
import random
r=random.randint(1,6)#creates a random integer between 1 and 6
if r==6:
	print("hurrayy!!!!!...   u got 6")#print hurray if dice shows 6
elif r==5:
    print("good....u got 5")#print this if dice shows 5
else:
	print("u got",+r)#prints this if dice shows less then 5
