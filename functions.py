import random

def check(someArray):
	for i in range( len(someArray) - 1):
		if someArray[i] != someArray[i + 1]:
			return False
	
	return True

#----------------------------------------------------------

def rollUntilFive(numbersToPick):
	roll = 5
	lastFive = []

	for i in range(5):
		lastFive.append(numbersToPick[random.randint(0, len(numbersToPick) - 1)])

	
	while not check(lastFive):
		lastFive.pop(0)
		lastFive.append(numbersToPick[random.randint(0, len(numbersToPick) - 1)])
		roll += 1

	rollData = (roll, numbersToPick.index(lastFive[0]))
	
	#numbersToPick.pop( numbersToPick.index(lastFive[0]))
	
	print("It took us " + str(roll) +" rolls to roll the number " + str(lastFive[0]) + " five times in a row!")

	return rollData

#----------------------------------------------------------

def Average(file):
	
	with open(file) as my_file:
		allValues = my_file.readlines()

		sum = 0
		for i in allValues:
			sum += int(i)
	
		return sum / len(allValues)

#----------------------------------------------------------

def endPoints(file):
	
	with open(file) as my_file:
		allValues = my_file.readlines()

	for i in range(len(allValues)):
		allValues[i] = int(allValues[i])

	allValues.sort()
	Min = allValues[0]
	Max = allValues[len(allValues) - 1]

	return (Min, Max)
	


"""
def makeRanges():
	finish.sort()
	ranges = []
	lowerBound = 0

	for i in range(MAXNUM + 1):
		if i + 1 in finish:
			ranges.append( (lowerBound, i) )
			lowerBound = i + 2
		if i == MAXNUM and MAXNUM not in finish:
			ranges.append( (lowerBound, MAXNUM))
			

	print(lowerBound)
	return ranges
 """