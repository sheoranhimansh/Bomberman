import sys
from alarmexception import *
from random import *
import time
import os
from board import *
from bomb import *
from player import *
from enemy import *

class Brick():

	def brick(self,Board):

			for i in range(15):
				x=randint(1,20)
				y=randint(1,41)
				if((x%2==0 and y%4==0) and (Board[x][y]!='X')): #To build wall bricks in the cardboard
					Board[x][y]='/'
					Board[x][y+1]='/'
					Board[x][y+2]='/'
					Board[x][y+3]='/'
					Board[x+1][y]='/'
					Board[x+1][y+1]='/'
					Board[x+1][y+2]='/'
					Board[x+1][y+3]='/'

