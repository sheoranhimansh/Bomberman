import sys
from alarmexception import *
from random import *
import time
import os
from board import *
from brick import *
from bomb import *
from player import *

class Enemy(Player): #Player is inherited from the existing player file

	def __init__(self,enemyarray):
		# Board=Board
		self.enemyarray=enemyarray


	def drawEnemy(self,Board):  #Drawing Enemy at (X,Y)
		for i in range(len(self.enemyarray)):
			x = self.enemyarray[i][0]
			y = self.enemyarray[i][1]
			#print("x and y",x,y)
			if(Board[2*x][4*y]!="X" and Board[2*x][4*y]!="/"):
					Board[2*x][4*y] = "E" 
					Board[2*x][4*y+1] = "E"
					Board[2*x][4*y+2] = "E"
					Board[2*x][4*y+3] = "E"
					Board[2*x+1][4*y] = "E" 
					Board[2*x+1][4*y+1] = "E"
					Board[2*x+1][4*y+2] = "E"
					Board[2*x+1][4*y+3] = "E"

	
	def checkPosition(self,x,y,Board):  #To check whether sorrounding area has walls or not
		if(Board[2*x][4*y]!="X" and Board[2*x][4*y]!="/"):
			return 1
		return 0

	def enemyInit(self,Board): #Initial Positions of Enemies decided
		for i in range(4):
			x = randint(2,17)
			y = randint(2,17)	
			self.enemyarray.append([x,y])
			# print(enemyPos[i][0],enemyPos[i][1])
		self.drawEnemy(Board)	

	def update(self,Board): # Mainly to update the positions of enemies
		# global enemyarray
		print(self.enemyarray)
		for i in range(len(self.enemyarray)):
			x=self.enemyarray[i][0]
			y=self.enemyarray[i][1]
			speed=randint(4,8)
			if(speed==4):
				#print("ok")
				if(self.checkPosition(x+1,y,Board)):  #checking whether there is wall brick at given position
					self.erasePlayer(x,y,Board)
					self.enemyarray[i][0]+=1
			if(speed==5):
				if(self.checkPosition(x-1,y,Board)):
					self.erasePlayer(x,y,Board)
					self.enemyarray[i][0]-=1
			if(speed==6):
				if(self.checkPosition(x,y+1,Board)):
					self.erasePlayer(x,y,Board)
					self.enemyarray[i][1]+=1
			if(speed==7):
				if(self.checkPosition(x,y-1,Board)):
					self.erasePlayer(x,y,Board)
					self.enemyarray[i][1]-=1

		self.drawEnemy(Board)

	def enemypos(self): # Returning EnemyPosition
		return self.enemyarray

