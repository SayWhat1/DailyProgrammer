def c99e():
	words, count = open('enable1.txt', 'r').read.splitlines(), 0
	for word in words:
		if list(word) == sorted(word):
			count += 1
	print count
			
c99e()