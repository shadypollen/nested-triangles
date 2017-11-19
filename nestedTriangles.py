def main():
	while True:
		print("Please enter the width of the innermost triangle")
		print("The value must be an odd positive integer")
		try:
			triangleWidth = int(input("> "))
			if triangleWidth % 2 != 0 and triangleWidth > 0:
				break
			else:
				print("The number is either even or negative")
				print("\n")
		except ValueError:
			print("\n")

	print("Enter the triangle nesting level:")
	nestLevel = int(input("> "))
	triangleGenerator(triangleWidth, nestLevel)


#Generates basic un-nested triangles and puts them in a list
def triangleGenerator(triangleWidth, nestLevel):
	charOne = "*"#charString[0]
	charTwo = "."#charString[1]
	triangleList = []
	triangleRow = []

	for level in range(nestLevel):
		#alternates nest chars every level
		if level % 2 == 0:
			char = charOne
		else:
			char = charTwo
		i = triangleWidth
		while i >= 1:
			row = (char*i).center(triangleWidth, " ")
			triangleRow.append(row)
			i = i - 2
		if level % 2 == 0:	
			triangleList.append(triangleRow)
		else:
#reverses triangle direction every level
			triangleList.append(list(reversed(triangleRow))) 
		
		triangleRow = []
		triangleWidth = (triangleWidth*2)+1
	if nestLevel > 1:
		joinTriangle(triangleList, nestLevel)


#prints basic un-nested triangles for reference
def printTriangle(triangleList): 
	for triangle in triangleList:
		print("Level:", triangleList.index(triangle)+1)
		for row in triangle:
			print("".join(row))

#Generates nested triangles
def joinTriangle(triangleList, nestLevel):
	triOneIndex = 0
	triTwoIndex = 1
	resultIndex = 1
	for level in range(nestLevel-1):
		resultTriangle = []
		triangleOne = triangleList[triOneIndex]
		triangleTwo = triangleList[triTwoIndex]	
		counter = 0
		if level % 2 == 0:
			triangleOne = list(reversed(triangleOne))
		for row in triangleOne:
			interTri = []
			if level % 2 == 0:
				nestRow = list(reversed(triangleTwo))[counter]
			else:
				nestRow = list(triangleTwo)[counter]
			nestInterRow = nestRow.replace(" ", "")
			nestingRow = row.replace(" ", "")
			nestChar = nestInterRow[0][0]
			interTri.append(nestingRow.center(len(nestInterRow), nestChar))
			resultTriangle.append(interTri[0].center(len(nestRow), " "))	
			counter = counter + 1
		nestEnd = len(resultTriangle)
		if level % 2 == 0:
			tail = reversed(triangleTwo[:nestEnd])
		else:
			tail = triangleTwo[nestEnd:]
		for row in tail:
			resultTriangle.append(row)
		print("Level {0} nest:".format(level+2))
		if level % 2 == 0:
			triangleList[resultIndex] = list(reversed(resultTriangle))
		else:
			triangleList[resultIndex] = resultTriangle
		for row in triangleList[resultIndex]:
			print(row)
		
		triangleList[level] = list(reversed(resultTriangle))
		triOneIndex = triOneIndex + 1
		triTwoIndex = triTwoIndex + 1
		resultIndex = resultIndex + 1
		
	
	
main()
