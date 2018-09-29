import random
s=0
while(s<=100):
	n=input("press r to roll the dice")
	if(n=='r'):
		r=random.randint(1,6)
		s=s+r
		print("u got",r)
		print("new position is",s)

		if(s==8):
			s=37
			print("i got ladder")
		elif(s==11):
			s=2
			print("sorry, u got snake")
		if(s==13):
			s=34
			print("i got ladder")
		elif(s==25):
			s=4
			print("sorry, u got snake")
		if(s==40):
			s=68
			print("i got ladder")
		elif(s==38):
			s=9
			print("sorry, u got snake")
		if(s==52):
			s=81
			print("i got ladder")
		elif(s==65):
			s=46
			print("sorry, u got snake")
		if(s==76):
			s=97
			print("i got ladder")
		elif(s==93):
			s=64
			print("sorry, u got snake")
		if(s==100):
			print("u won")
			exit()
		elif(s>=100):
			print("stay in same place")
			s=s-r

