from random import randint

def c102e(roll):
	C, result = 0, 0
	A, B = roll.split('d')
	if A == '':
		A = 1
	if '+' in B:
			B, C = B.split('+')
			C = int(C)
	elif '-' in B:
			B, C = B.split('-')
			C = -int(C)
	return sum(randint(1, int(B)) for _ in range(int(A))) + C
	
for i in range(10):
	print c102e(str(i+1) +'d6-2')