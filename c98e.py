def c98(op, n):
	#op, n = raw_input('Input operator and iterations').split()
	n = int(n)
	table = [[0]*(n+1) for i in range(n+1)]
	div = ''
	run = range(n+1)
	for i in range(n+1):
		div += '----'
		for j in range(n+1):
			table[i][j] = eval('%d%s%d'%(i, op, j))
	print op,'|', str(run).strip('[]').replace(',',' ')
	print div
	for i in run:
		print run[i], '|', str(table[i]).strip(',[]').replace(',', ' ')
c98('+',4);
	