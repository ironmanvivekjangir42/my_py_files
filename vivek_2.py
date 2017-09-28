#!/usr/bin/python3
#snake n ladder cheaded
import random
count=0
r=0
while count<=100:#creating a while loop
	roll=input("press q to roll")#taking input
	if roll=="q":
		r=random.randint(1,6)
		count=count+r
		if count>=100:
			print("u won")
		else:
			#conditions for ladders
			if count==8:
				count=37
				print("u climbed d ladder to ",count)
			elif count==13:
				count=34
				print("u climbed d ladder to ",count)
			elif count==40:
				count=68
				print("u climbed d ladder to",count)
			elif count==52:
				count=81
				print("u climbed d ladder to",count)
			elif count==76:
				count=97
				print("u climbed d ladder to",count)
			elif count==38:#changing d value of dice to never get a snake
				count=count-r
				if r<6:
					r=r+1
					count=count+r
					print(count)
				elif r==6:
					r=r-1
					count=count+r
					print(count)
			elif count==25:
				count=count-r
				if r<6:
					r=r+1
					count=count+r
					print(count)
				elif r==6:
					r=r-1
					count=count+r
					print(count)
			elif count==11:
				count=count-r
				if r<6:
					r=r+1
					count=count+r
					print(count)
				elif r==6:
					r=r-1
					count=count+r
					print(count)
			elif count==65:
				if r<6:
					r=r+1
					count=count+r
					print(count)
				elif r==6:
					r=r-1
					count=count+r
					print(count)
			elif count==93:
				if r<6:
					r=r+1
					count=count+r
					print(count)
				elif r==6:
					r=r-1
					count=count+r
					print(count)
			elif count==89:
				if r<6:
					r=r+1
					count=count+r
					print(count)
				elif r==6:
					r=r-1
					count=count+r
					print(count)
			else:#if no case matches than print count
				print(count)
