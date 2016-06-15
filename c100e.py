import datetime
def c100e():
	cycle = datetime.timedelta(minutes = 90)
	wake = raw_input('When would you like to wake up?')
	h, m = wake.split(':')
	wake = datetime.time(int(h), int(m))
	sleep = []
	for i in range(5,0,-1):
		sleep.append(wake - cycle * (i+1))
	print sleep
c100e()
	