'''Simple command line based tic tac toe for two human player
'''
	
def pprint(arr):
	print ""
	for r in range(row):
		print arr[r]
	
def validateinput(arr, row,col, pin, char):
	try:
		pin = pin.split(",")
		input = (int(pin[0]),int(pin[1]))
		if input[0] <3 and input[0] > -1 and\
			input[1] < 3 and input[1] > -1:
			if not arr[input[0]][input[1]]:
				arr[input[0]][input[1]] = char
				return True
		else:
			return False
		
	except Exception:
		return False

def verifyarr(arr, char, row, col):
	for r in range(row):
		count = 0
		for c in range(col):
			if arr[r][c] == char:
				count += 1
		if count == 3:
			return True
	for c in range(col):
		count = 0
		for r in range(row):
			if arr[r][c] == char:
				count += 1
		if count == 3:
			return True
	count = 0
	for r in range(row):
		if arr[r][r] == char:
			count += 1
	if count == 3:
		return True

	count = 0
	for r in range(row):
		if arr[r][row-r-1] == char:
			count += 1
	if count == 3:
		return True
		
	return False
	
	
row = col = 3
arr = []
for r in range(row):
	arr.append([None] * col)
	
print "Initial tic tac toe is: \n"
pprint(arr)

found = False
player = {0 : 'X', 1 :'O'}
pc = 0
while not found:
	char = player[pc]
	pin = raw_input("Enter row, col for " +  char + " :")
	vi = validateinput(arr, row,col, pin, char)
	if not vi:
		print "Wrong input"
		continue
	va = verifyarr(arr, char, row, col)
	if not va:
		pc = (pc + 1)%2
	else:
		print char + " user won"
		found = True
	pprint(arr)
