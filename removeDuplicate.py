def removeDupl(inputList):
	sortedList = []

	for item in inputList:
		if item not in sortedList:
			sortedList.append(item)

	return sortedList

names = ["mark", "john", "mark", "fred", "paul", "john"]

sortedList = removeDupl(names)
print(sortedList)