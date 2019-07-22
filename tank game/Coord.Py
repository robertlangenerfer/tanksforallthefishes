#Move this

import random

#numObst = random.randint(10,25)
numObst = 5
cordListX = []
cordListY = []

for i in range(numObst+2): 
	if i < numObst:
		xPos = random.randint(0,20)
		yPos = random.randint(0,20)
	elif i == numObst:
		xPos = random.randint(0,4)
		yPos = random.randint(0,20)
	else:
		xPos = random.randint(15,20)
		yPos = random.randint(0,20)

	validCord = True

	repeatVal = True

	while repeatVal == True:
		for j in range(len(cordListX)):
			if cordListX[j] == xPos:
				if cordListY[j] == yPos:
					validCord = False
				
		if validCord == True:
			repeatVal = False
		else:
			if i < numObst:
				xPos = random.randint(0,20)
				yPos = random.randint(0,20)
			elif i == numObst:
				xPos = random.randint(0,4)
				yPos = random.randint(0,20)
			else:
				xPos = random.randint(15,20)
				yPos = random.randint(0,20)
			validCord = True

	cordListX.append(xPos)
	cordListY.append(yPos)


for x in range(numObst+2):
	if x < numObst:
		print(cordListX[x], ", ", cordListY[x], ", Obstacle ",x+1)
	elif x == numObst:
		print(cordListX[x], ", ", cordListY[x],", Tank 1")
	else:
		print(cordListX[x], ", ", cordListY[x],", Tank 2")
	
