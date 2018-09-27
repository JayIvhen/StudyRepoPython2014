#!usr/bin/python

#YES_or_NO

def ask_ok(message1, retries=4,message2='YES(y) or NO(n) please'):
	while True:
		ok = raw_input(message1)
		if ok in ('y','Y','ye','YE','YES','yes'):
			return True
		if ok in ('n','N','NO','no'):
			return False
		retries = retries - 1
		if retries < 0:
			raise IOError('error')
		print message2

ask_ok('Are you shure you whant to exit? Y or N \n')
	
