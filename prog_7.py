#!/usr/bin/python3
import random
cc=0#integer to store computers score
ps=0#int to store players score
count=0
s=["stone","scissor","paper"]#create an array
r=random.randint(0,2)#create a radom integer 
c=s[r]#Choosing form the array 
z=input("press p to play")
while count<=10:
	count=count+1
	if z=="p":
		i=input("typ stone, scissor ,paper to play")
		print("player chose",i,",comp chose",c)
		if i=="stone":
			if c=="stone":
				print("its a draw")
				print("ur score is",ps,",comp score is",cc)
			elif c=="scissor":
				print("u won")
				ps=ps+1
				print("ur score is",ps,",comp score is",cc)
			else :
				print("comp won")
				cc=cc+1
				print("ur score is",ps,",comp score is",cc)
		elif i=="scissor":
			if c=="stone":
				print("comp won")
				cc=cc+1
				print("ur score is",ps,",comp score is",cc)
			elif c=="scissor":
				print("its a draw")
				print("ur score is",ps,",comp score is",cc)
			else :
				print("u won")
				ps=ps+1
				print("ur score is",ps,",comp score is",cc)
		elif i=="paper":
			if c=="stone":
				print("u won")
				ps=ps+1
				print("ur score is",ps,",comp score is",cc)
			elif c=="scissor":
				print("comp won")
				cc=cc+1
				print("ur score is",ps,",comp score is",cc)
			else :
				print("its a draw")
				print("ur score is",ps,",comp score is",cc)
		else:
			print("wrong spelling,typr again")
