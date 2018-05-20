import sys
from alarmexception import *
from random import *
import time
import os

from brick import *
from bomb import *
from player import *
from enemy import *

class GameBoard():
		
	#This class has a function to build the Gameboard

	def build(self,Board):
		for i in range(40):
			for j in range(84):
				if(j<=3 or j>=80):
					Board[i][j]='X'
				elif(i<2 or i>=38):
					Board[i][j]='X'
				elif((j>3 and j<76 and i>=2 and i<38) and (j%8==3 or j%8==1 or j%8==2 or j%8==0) and (i%4==0 or i%4==1)):
					Board[i][j]='X'
				# else:
