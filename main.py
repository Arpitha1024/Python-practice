# randomely keeps generating a number, when it generates 5 of the same number it stops generating that number

#https://stackoverflow.com/questions/33730396/how-to-generate-random-integers-with-multiple-ranges

import functions as fc

f = open("totals.txt", "a")

MAXNUM = 9

finish = [6, 3, 9]
numbersToPick = []

for i in range(MAXNUM + 1):
	numbersToPick.append(i)


totalRolls = 0
while numbersToPick != []:
	rollData = fc.rollUntilFive(numbersToPick)
	totalRolls += rollData[0]
	numbersToPick.pop(rollData[1])

f.write(str(totalRolls) + "\n")
f.close()


print("\nIt took us a total of " + str(totalRolls) + " rolls")
avg = round(fc.Average("totals.txt"),2)
print("The average total rolls is now " + str(avg)) 

endPoints = fc.endPoints("totals.txt")

min = str(endPoints[0])
max = str(endPoints[1])

#The sort function is based on text, need to convert to int

print("The all time minimum roll was " + min + "\nThe all time maximum roll was " + max)

