from random import randrange
class intialize:
	def __init__(self):
		self.kke = 0
		self.li = []
		l = ["."]
		self.li = [l*35 for i in range(15) ]
		for i in range(2,10):
	        	self.li[i][27] = "X"
		for i in range(4,19):
			self.li[11][i] = "X"
		for i in range(3,12):
			self.li[i][18] = "X"
		for i in range(8,13):
			self.li[5][i] = "X"
		for i in range(5,9):
			self.li[i][7] = "X"
	def rand_coins(self):
		self.coins = randrange(25,32)
		for i in range(self.coins):
			a1 = randrange(0,15)
			a2 = randrange(0,35)
			if(self.li[a1][a2]!="X" and self.li[a1][a2]!="P" and self.li[a1][a2]!="G" ):
				self.li[a1][a2] = "C"
				self.kke = self.kke + 1
		
		 
	def fun(self):
		for i in self.li:
			for j in i:
				print j,
			print ""

	def reputation(self,m,n,n2,n3):
		while(1):
			self.fun()
			self.m = m
			self.n = n
			self.n2 = n2
			self.n3 = n3
			print "Score:",self.m.score
			print self.kke
			if(self.m.score == self.kke):
				self.rand_coins()
			k = raw_input("Enter Move:")
                	if k == "a":
				x = self.m.left()
			if k == "w":
				x = self.m.up()
			if k == "s":
				x = self.m.down()
			if k == "d":
				x = self.m.right()
			if k == "q":
			 	break
			if(x == 4):
				self.fun()
				break
			pp = self.n.travel()
			qq = self.n2.travel()
			rr = self.n3.travel()
			if(pp == 4 or qq == 4 or rr == 4):
				self.fun()
				break
			

class person:
	def __init__(self,x,y,li):
		self.x = x
		self.y = y
		self.li = li
	def checkWall(self,k):
		if(k == "up"):
			if((self.x > 0) and self.li[self.x - 1][self.y] == "X"):
				return True
		if(k == "down"):
			if((self.x < 14) and self.li[self.x + 1][self.y] == "X"):
				return True
		if(k == "right"):
			if((self.y < 34) and self.li[self.x][self.y + 1] == "X"):
				return True
		if(k == "left"):
			if((self.y > 0) and self.li[self.x][self.y - 1] == "X"):
				return True 
	
	def up(self):

		if(self.x > 0 and (self.li[self.x - 1][self.y] == "C" or self.li[self.x - 1][self.y] == "." )):  
			self.collectCoin("up")
			self.li[self.x][self.y] = "."
			self.x = self.x - 1
			self.li[self.x][self.y] = "P"
			return 2
		elif(self.checkWall("up")):
			print "\n\n Sorry u can't move"
			return 3
		elif(self.checkGhost("up")):
			print "Game is Over \n\n"
			return 4
	def down(self):
		if(self.x < 14 and (self.li[self.x + 1][self.y] == "C" or self.li[self.x + 1][self.y] == "." )):
			self.collectCoin("down")
			self.li[self.x][self.y] = "."
			self.x = self.x + 1
			self.li[self.x][self.y] = "P"
			return 2
		elif(self.checkWall("down")):
			print "\n\n Sorry u can't move"
			return 3
			
		elif(self.checkGhost("down")):
			print "Game is Over \n\n"
			return 4
	def right(self):
		if(self.y < 34 and (self.li[self.x][self.y + 1] == "C" or self.li[self.x][self.y + 1] == "." )):
			self.collectCoin("right")
			self.li[self.x][self.y] = "."
			self.y = self.y + 1
			self.li[self.x][self.y] = "P"
			return 2

		elif(self.checkWall("right")):
		  	print "\n\n Sorry u can't move"
			return 3
		
		elif(self.checkGhost("right")):
		  	print "Game is Over \n\n"
			return 4

	def left(self):
		if(self.y > 0 and (self.li[self.x][self.y - 1] == "C" or self.li[self.x][self.y - 1] == "." )):
			self.collectCoin("left")
			self.li[self.x][self.y] = "."
			self.y = self.y - 1
			self.li[self.x][self.y] = "P"
			return 2
		elif(self.checkWall("left")):
			print "\n\n Sorry u can't move"
			return 3
		elif(self.checkGhost("left")):
		 	print "Game is Over \n\n"
		 	return 4
	def position(self):
		return (self.x,self.y)

class pacman(person):
	def __init__(self,px,py,p):
		person.__init__(self,px,py,p)
		self.li[self.x][self.y] = "P"
		self.score = 0
	
	def collectCoin(self,kk):
		if(kk == "up"):
			if((self.x > 0) and (self.li[self.x - 1][self.y] == "C")):
				self.score = self.score + 1
		if(kk == "down"):
		  	if((self.x < 14) and (self.li[self.x + 1][self.y] == "C")):
				self.score = self.score + 1
		if(kk == "right"):
		  	if((self.y < 34) and (self.li[self.x][self.y + 1] == "C")):
				self.score = self.score + 1
		if(kk == "left"):
		  	if((self.y > 0) and (self.li[self.x][self.y - 1] == "C")):
				self.score = self.score + 1

  	def  checkGhost(self,pp):
		if(pp == "up"):
			if((self.x > 0) and (self.li[self.x - 1][self.y] == "G")):
				return True
		if(pp == "down"):
		  	if((self.x < 14) and (self.li[self.x + 1][self.y] == "G")):
				return True
		if(pp == "right"):
		  	if((self.y < 34) and (self.li[self.x][self.y + 1] == "G")):
				return True
		if(pp == "left"):
		  	if((self.y > 0) and (self.li[self.x][self.y - 1] == "G")):
				return True
		
class ghost(person):
	def __init__(self,x,y,p1):
		person.__init__(self,x,y,p1)
		self.li[self.x][self.y] = "G"
		self.flag = 0
	def travel(self):
		kkk = 0
		ash = randrange(-1,2)
		rand =randrange(-1,2)
		if((0 <= self.y + rand <= 34) and (0 <= self.x + ash <= 14)  and (self.li[self.x + ash][self.y + rand] == "." or self.li[self.x + ash][self.y + rand] == "P")):
			if(self.li[self.x + ash][self.y + rand ] == "P"):
					print "Game is Over"
					kkk = 1
						
			if(self.flag == 1):
				self.li[self.x][self.y] = "C"
				self.x = self.x + ash
				self.y = self.y + rand
				self.li[self.x][self.y] = "G"
				self.flag=0
			else:
				self.li[self.x][self.y] = "."
				self.x = self.x + ash
				self.y = self.y + rand
				self.li[self.x][self.y] = "G"
			if(kkk == 1):
				return 4
			elif(kkk !=1):
			 	return 2
		elif((0 <=self.y + rand <= 34) and (0 <= self.x + ash <=14 ) and ( self.li[self.x + ash ][self.y + rand] == "X")):
			print "\n"
			return 3
		elif((0 <=self.y + rand <= 34) and (0 <= self.x + ash <= 14) and (self.li[self.x + ash][self.y + rand] == "C")):
			if(self.flag == 1):
				self.li[self.x][self.y] = "C"
				self.x = self.x + ash
				self.y = self.y + rand
				self.li[self.x][self.y] = "G"
			else:
				
				self.li[self.x][self.y] = "."
				self.x = self.x + ash
				self.y = self.y + rand
				self.li[self.x][self.y] = "G"
				self.flag = 1


	def ghostPosition(self):
		return (self.x,self.y)
	

if __name__ == "__main__" :
	a = intialize()
	p = a.li
	m = pacman(6,23,p)
	n = ghost(8,16,p)
	n2 = ghost(13,29,p)
	n3 = ghost(2,5,p)
	a.rand_coins()
        a.reputation(m,n,n2,n3)    
