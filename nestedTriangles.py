def main():
#	print("Please enter 2 characters with which to draw the triangle")
#	print("Examples: \".*\", \"$!\", \"ab\"")
#	charString = str(input("> "))
#	charString = list(charString)
#	if len(charString) != 2:
#		print("Incorrect input. Try again.\n")
#		main()
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


def printTriangle(triangleList):
	for triangle in triangleList:
		print("Level:", triangleList.index(triangle)+1)
		for row in triangle:
			print("".join(row))

def joinTriangle():
	pass
	#use nested .center with alternating characters 
	#to implement joining triangles
main()
