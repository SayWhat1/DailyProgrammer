def c101e(start, end):
	years = []
	for i in range(start, end +1):
		if len(str(i)) == len(set(str(i))):
			years.append(i)
	print years, len(years)

c101e(1980, 1987)