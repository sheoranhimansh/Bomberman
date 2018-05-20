import sys
from alarmexception import *
from random import *
import time
import os

from board import *
from brick import *
from player import *
from enemy import *

class Bomb():

	def __init__(self,enemyarray,score):  #Initializes counter to 0
		# Board=Board
		self.enemyarray=enemyarray
		self.counter=0 # To check if enemy has collided with bomberman or bomberman died due to bombing.
		self.score=score # For calculating score
	
	def drawbomb(self,x,y,Board):
		if(Board[2*x][4*y]!='X' or Board[2*x][4*y]!='/' or Board[2*x][4*y]!='E'): #Creating Bomb At (X,Y)
					Board[2*x][4*y] = "[" 
					Board[2*x][4*y+1] = "0"
					Board[2*x][4*y+2] = "0"
					Board[2*x][4*y+3] = "]"
					Board[2*x+1][4*y] = "[" 
					Board[2*x+1][4*y+1] = "0"
					Board[2*x+1][4*y+2] = "0"
					Board[2*x+1][4*y+3] = "]"
					time.sleep(1)

	

	def erase(self,x,y,Board):  
		# print(x,y)
		
		if(Board[2*x][4*y]!='X'): # Erasing Contents At (X,Y)
			# print("abhi")
			Board[2*x][4*y]=' '
			Board[2*x][4*y+1]=' '
			Board[2*x][4*y+2]=' '
			Board[2*x][4*y+3]=' '
			Board[2*x+1][4*y]=' '
			Board[2*x+1][4*y+1]=' '
			Board[2*x+1][4*y+2]=' '
			Board[2*x+1][4*y+3]=' '


	def explode(self,x,y,Board):
		print(x,y)
		
		if(Board[2*x][4*y]!='X'): #Showing the Bomb Affected Area
		
			Board[2*x][4*y]='e'
			Board[2*x][4*y+1]='e'
			Board[2*x][4*y+2]='e'
			Board[2*x][4*y+3]='e'
			Board[2*x+1][4*y]='e'
			Board[2*x+1][4*y+1]='e'
			Board[2*x+1][4*y+2]='e'
			Board[2*x+1][4*y+3]='e'

	def check(self,x,y,Board,player):
		if([x,y] in self.enemyarray): #checking whether destroyed positions include enemy position or not
			self.enemyarray.remove([x,y])
			self.score+=100
			if(Board[2*x][4*y]=="/"):
				self.score+=20
		if(x==player[0] and y==player[1]): #whether Bomberman and enemy collided
			self.counter=1



	def checkbrick(self,x,y,Board):

		if(Board[2*x][4*y]!='X'): #checking for wall bricks
			return 1
		return 0


	def funcBomb(self,x,y,Board,player): # mainly to explode the area around Bomb
 		
		if(self.checkbrick(x+1,y,Board)):  #checking whether the passed coordinates have brick walls
			self.explode(x+1,y,Board)      # drawing bomb devastation at (X,Y)
			self.check(x+1,y,Board,player) # checking whether Bomberman and enemy were destoyed in bomb blast 

		if(self.checkbrick(x-1,y,Board)):
			self.explode(x-1,y,Board)
			self.check(x-1,y,Board,player)

		if(self.checkbrick(x,y+1,Board)):
			self.explode(x,y+1,Board)
			self.check(x,y+1,Board,player)

		if(self.checkbrick(x,y-1,Board)):
			self.explode(x,y-1,Board)
			self.check(x,y-1,Board,player)				

		if(self.checkbrick(x+2,y,Board) and self.checkbrick(x+1,y,Board)):
			self.explode(x+2,y,Board)
			self.check(x+2,y,Board,player)

		if(self.checkbrick(x-2,y,Board) and self.checkbrick(x-1,y,Board)):
			self.explode(x-2,y,Board)
			self.check(x-2,y,Board,player)

		if(self.checkbrick(x,y+2,Board) and self.checkbrick(x,y+1,Board)):
			self.explode(x,y+2,Board)
			self.check(x,y+2,Board,player)

		if(self.checkbrick(x,y-2,Board) and self.checkbrick(x,y-1,Board)):
			self.explode(x,y-2,Board)
			self.check(x,y-2,Board,player)
	
	def enemypos(self):
	 	return self.enemyarray

	def retcounter(self):
		return self.counter

	def retscore(self):
		return self.score

