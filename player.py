import sys
from alarmexception import *
from random import *
import time
import os


class Player():
	# playerPos=[1,1]

	def __init__(self):
		# Board=Board
		self.playerPos=[1,1]

	def drawPlayer(self,x,y,Board):  # Drawing the player at (X,Y)
		if(Board[2*x][4*y]!="X" and Board[2*x][4*y]!="/"):
				Board[2*x][4*y] = "B" 
				Board[2*x][4*y+1] = "B"
				Board[2*x][4*y+2] = "B"
				Board[2*x][4*y+3] = "B"
				Board[2*x+1][4*y] = "B" 
				Board[2*x+1][4*y+1] = "B"
				Board[2*x+1][4*y+2] = "B"
				Board[2*x+1][4*y+3] = "B"
		return [x,y]

	
	def erasePlayer(self,x,y,Board): # Erasing the player at (X,Y)
			if(Board[2*x][4*y]!="X" and Board[2*x][4*y]!="/"):	
				Board[2*x][4*y] = " " 
				Board[2*x][4*y+1] = " "
				Board[2*x][4*y+2] = " "
				Board[2*x][4*y+3] = " "
				Board[2*x+1][4*y] = " " 
				Board[2*x+1][4*y+1] = " "
				Board[2*x+1][4*y+2] = " "
				Board[2*x+1][4*y+3] = " "


	def checkPosition(self,x,y,Board): # Checking whether the wall bricks are there at (X,Y)
		if(Board[2*x][4*y]=="X" or Board[2*x][4*y]=="/"):
			return -1
		return 1

	def updatePlayer(self,Board): #updating the position of players
		x = self.playerPos[0]
		y = self.playerPos[1]
		self.drawPlayer(x,y,Board) #calling drawPlayer to draw the Bomberman
		return 	

	def playerInit(self):  # Initializing the player
		playerPos = (1,1)
		x = self.playerPos[0]
		y = self.playerPos[1]
		self.drawPlayer(x,y,Board)
		return

	def moveDown(self,Board): # When user called Bomberman to move down
 		x = self.playerPos[0]
		y = self.playerPos[1]		
		if(self.checkPosition(x+1,y,Board)>0):  # checking if there is no wall bricks
			self.erasePlayer(self.playerPos[0],self.playerPos[1],Board)
			self.playerPos[0] += 1  # changing player position
			# self.erasePlayer(self.playerPos[0],self.playerPos[1])
			self.drawPlayer(self.playerPos[0],self.playerPos[1],Board)
		return

	def moveUp(self,Board):
 		x = self.playerPos[0]
		y = self.playerPos[1]		
		if(self.checkPosition(x-1,y,Board)>0):
			self.erasePlayer(self.playerPos[0],self.playerPos[1],Board)
			self.playerPos[0] -= 1
			# self.erasePlayer(self.playerPos[0],self.playerPos[1])
			self.drawPlayer(self.playerPos[0],self.playerPos[1],Board)
		return

	def moveLeft(self,Board):
 		x = self.playerPos[0]
		y = self.playerPos[1]		
		if(self.checkPosition(x,y-1,Board)>0):
			self.erasePlayer(self.playerPos[0],self.playerPos[1],Board)
			self.playerPos[1] -= 1
			self.drawPlayer(self.playerPos[0],self.playerPos[1],Board)
		return

	def moveRight(self,Board):
 		x = self.playerPos[0]
		y = self.playerPos[1]		
		if(self.checkPosition(x,y+1,Board)>0):
			self.erasePlayer(self.playerPos[0],self.playerPos[1],Board)
			self.playerPos[1] += 1
			self.drawPlayer(self.playerPos[0],self.playerPos[1],Board)
		return

	def playerpos(self): # Returning player's position
		return self.playerPos

