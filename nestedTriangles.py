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


def triangleGenerator(triangleWidth, nestLevel):
	charOne = "*"#charString[0]
	charTwo = "."#charString[1]
	triangleList = []
	triangleRow = []

	for level in range(nestLevel):
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
			triangleList.append(list(reversed(triangleRow)))
		
		triangleRow = []
		triangleWidth = (triangleWidth*2)+1
	printTriangle(triangleList)
	if nestLevel > 1:
		joinTriangle(triangleList, nestLevel)


def printTriangle(triangleList):
	for triangle in triangleList:
		print("Level:", triangleList.index(triangle)+1)
		for row in triangle:
			print("".join(row))

def joinTriangle(triangleList, nestLevel):
	triOneIndex = 0
	triTwoIndex = 1
	resultTriangle = []
	triangleOne = triangleList[triOneIndex]
	triangleTwo = triangleList[triTwoIndex]	
	counter = 0
	for row in reversed(triangleOne):
		interTri = []
		nestRow = list(reversed(triangleTwo))[counter]
		nestInterRow = nestRow.replace(" ", "")
		nestingRow = row.replace(" ", "")
		nestChar = nestInterRow[0][0]
		interTri.append(nestingRow.center(len(nestInterRow), nestChar))
		resultTriangle.append(interTri[0].center(len(nestRow), " "))
		interTri = []			
		counter = counter + 1
	nestEnd = len(resultTriangle)
	for row in reversed(triangleTwo[:nestEnd]):
		resultTriangle.append(row)
	print("Result triangle:")
	for row in reversed(resultTriangle):
		print(row)
#	triOneIndex = triOneIndex + 1
#	triTwoIndex = triTwoIndex + 1
	
	
main()
