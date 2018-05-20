import sys
from alarmexception import *
from random import *
import time
import os
from board import *
from brick import *
from bomb import *
from player import *
from enemy import *
from getchunix import *



getch = GetchUnix()

def alarmHandler(signum, frame):
    raise AlarmException

def input_to(timeout=1):
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.alarm(timeout)
    try:
        text = getch()
        signal.alarm(0)
        return text
    except AlarmException:
        print("\n Prompt timeout. Continuing...")
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''




Board=[[' ' for x in range(84)]for y in range(40)]

class Game():


	def print_mat(self,Board):
		for i in Board:
			print("".join(i))


	# def static_input():
	# 	try:
	# 		text=getch()
	# 	except:
	# 		text=''xxxxxxxxxxxxxxxxx
	# 	return text

	def functioning(self):
		score=0
		for i in range(3):
			ob=GameBoard()  #creating Gameboard object
			ob.build(Board) # calling Build function of GameBoard
			
			ob1=Brick() #creating Brick object
			ob1.brick(Board) #calling To build wall bricks in gameboard
			# pl=Player(ter)
			pl=Player()  #creating Player object
			pl.updatePlayer(Board)  #updating player position
			# pl.print_mat()
			en=Enemy([])
			en.enemyInit(Board)  #initializing enemy objects
			# w2=en.enemypos()
			en.update(Board)  #updating enemies
			w2=en.enemypos()  #storing enemies position
			
			os.system("clear")
			self.print_mat(Board)
			co=0
			
			while(1):
				
				print("Score: "+str(score))
				print("Lives: "+str(3-i))
				w1=pl.playerpos()  #storing player position
				w2=en.enemypos()   # storing enemy position
				for r in w2:
					if(r==w1):   #checking if enemy and Bomberman collide
						co=1
				if(co==1):
					pl.erasePlayer(w1[0],w1[1],Board) 
					os.system("clear")
					self.print_mat(Board)
					break
				

				# pl.updatePlayer(Board)
				# ob.build(Board)
				ob.build(Board) #building walls 
				
				en.update(Board)
				
				os.system("clear")
				self.print_mat(Board)
				x=input_to()   # To keep printing board even if no actions take place so that enemy could move randomly
				# en.update(Board)
				os.system("clear")
				self.print_mat(Board)
				# en.update()
				if(x=='w'):  # To move the bomberman up
					pl.moveUp(Board)
					# en.update(Board)
					# w2=en.enemypos()
					os.system("clear")
					self.print_mat(Board)
				elif(x=='a'):
					pl.moveLeft(Board) # To move the bomberman left
					# en.update(Board)
					# w2=en.enemypos()
					os.system("clear")
					self.print_mat(Board)
				elif(x=='s'):
					pl.moveDown(Board) # To move the bomberman down
					# en.update(Board)
					# w2=en.enemypos()
					os.system("clear") 
					self.print_mat(Board)
				elif(x=='d'):
					pl.moveRight(Board)  # To move the bomberman right
					# en.update(Board)
					# w2=en.enemypos()
					os.system("clear")
					self.print_mat(Board)
				elif(x=='b'):
					ter=en.enemypos()
					br=Bomb(ter,score)
					w1=pl.playerpos()
					print(w1)
					# time.sleep(1)			
					kar1=w1[0]
					kar2=w1[1]
					br.drawbomb(kar1,kar2,Board)
					os.system("clear")
					self.print_mat(Board)
					time.sleep(1)
					for i in range(4):
						en.update(Board)
				
						os.system("clear")
						self.print_mat(Board)
						x=input_to()  # To give Bomb the Timer of 4 moments
				
						if(x=='w'):
							pl.moveUp(Board)
					
						elif(x=='a'):
							pl.moveLeft(Board)


						elif(x=='s'):
							pl.moveDown(Board)
					
						elif(x=='d'):
							pl.moveRight(Board)
					
					w2=en.enemypos()
					x1=w1[0]
					y1=w1[1]

					os.system("clear")
					self.print_mat(Board)

					br.funcBomb(kar1,kar2,Board,pl.playerpos()) #Implementing Bomb devastation effect
					# self.print_mat(Board)
					os.system("clear")
					self.print_mat(Board)

					time.sleep(1)
					
					w2=br.enemypos()
					ob.build(Board)
					
					os.system("clear")
					self.print_mat(Board)
					
					br.erase(kar1,kar2,Board)     #erasing all positions where bomb devastation occured
					br.erase(kar1+1,kar2,Board)
					br.erase(kar1-1,kar2,Board)
					br.erase(kar1,kar2+1,Board)
					br.erase(kar1,kar2-1,Board)
					br.erase(kar1+2,kar2,Board)
					br.erase(kar1-2,kar2,Board)
					br.erase(kar1,kar2+2,Board)
					br.erase(kar1,kar2-2,Board)
					
					os.system("clear")
					self.print_mat(Board)
					
					score=br.retscore()

					c4=br.retcounter()
					if(c4==1):           #checking if enemy and Bomberman clashed
						print("DEAD")
						time.sleep(1)
						break
					
				elif(x=='q'):
					#br=Bomb(Board,)
					break
				en=Enemy(w2)	 # Here w2 is the new enemy positions array
				en.update(Board)
				# print("Score: "+str(score))
				# print("Lives: "+str(3-i))

g=Game()
g.functioning()
		