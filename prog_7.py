#!/usr/bin/python3
#stone paper scisors
import random
cc=0
ps=0
count=0
s=["stone","scisor","paper"]
r=random.randint(0,2)
c=s[r]
z=input("press p to play")
while count<=10:
	count=count+1
	if z=="p":
		i=input("typ stone, scisor ,paper to play")
		print("player chose",i,",comp chose",c)
		if i=="stone":
			if c=="stone":
				print("its a draw")
				print("ur score is",ps,",comp score is",cc)
			elif c=="scisor":
				print("u won")
				ps=ps+1
				print("ur score is",ps,",comp score is",cc)
			else :
				print("comp won")
				cc=cc+1
				print("ur score is",ps,",comp score is",cc)
		elif i=="scisor":
			if c=="stone":
				print("comp won")
				cc=cc+1
				print("ur score is",ps,",comp score is",cc)
			elif c=="scisor":
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
			elif c=="scisor":
				print("comp won")
				cc=cc+1
				print("ur score is",ps,",comp score is",cc)
			else :
				print("its a draw")
				print("ur score is",ps,",comp score is",cc)
		else:
			print("wrong spelling,typr again")
