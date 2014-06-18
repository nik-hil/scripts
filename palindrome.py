# simple fun with O(n^2) to find all palindrome in given string

def pal(string):
	l = len(string)+1
	for i in range(l):
		for j in range(1,l):
			#print string[i:j]
			if string[i:j] == string[i:j][::-1]:
				if len(string[i:j]) != 1 and string[i:j]:
					print string[i:j]
					
'''
>>> pal("ABCBAHELLOHOWRACECARAREYOUIAMAIDOINGGOOD")
ABCBA
BCB
LL
OHO
RACECAR
ACECA
CEC
ARA
RAR
IAMAI
AMA
GG
OO
'''
