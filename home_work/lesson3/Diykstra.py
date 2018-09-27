#!usr/bin/python

"""Diykstra algorithm"""

__author__ = "JayIvhen"

def search_function(room, x, y, path):
	print x, y, room[x][y]['path_length']
	path.append((x,y))
	if room[x][y]['x'] == 10 and room[x][y]['y'] ==10:
		print 'Finish!!'
		global path = path
		return 
	if room[x][y]['UP_check'] == False:
		room[x][y]['UP_check'] = True
		if room[x][y]['x'] != 0 and room[x-1][y]['simbol'] != '#':
			room[x-1][y]['DOWN_check'] = True
			room[x-1][y]['path_length'] = room[x][y]['path_length'] + 1
			search_function(room, x-1, y)	
	if room[x][y]['DOWN_check'] == False:
		room[x][y]['DOWN_check'] = True
		if room[x][y]['x'] != 10 and room[x+1][y]['simbol'] != '#':
			room[x+1][y]['UP_check'] = True
			room[x+1][y]['path_length'] = room[x][y]['path_length'] + 1
			search_function(room, x+1, y)
	if room[x][y]['LEFT_check'] == False:
		room[x][y]['LEFT_check'] = True
		if room[x][y]['y'] != 0 and room[x][y-1]['simbol'] != '#':
			room[x][y-1]['RIGHT_check'] = True
			room[x][y-1]['path_length'] = room[x][y]['path_length'] + 1
			search_function(room, x, y-1)
	if room[x][y]['RIGHT_check'] == False:
		room[x][y]['RIGHT_check'] = True
		if room[x][y]['y'] != 10 and room[x][y+1]['simbol'] != '#':
			room[x][y+1]['LEFT_check'] = True
			room[x][y+1]['path_length'] = room[x][y]['path_length'] + 1
			search_function(room, x, y+1)
	if room[x][y]['x'] == 0 and room[x][y]['y'] == 0 and room[x][y]['path_length'] == 1:
		print 'YOOU SHELL NOT PASS!!! There is no escape!'
	return
	
def input_read():

	lab_map = []
	labirinth = []
	room = []

	while True:
		b = raw_input()
		if b == '':
			break
		lab_map.append(b)
	for i in range(len(lab_map)):
		room.append([])
		for j in range(len(lab_map[i])):
			room[i].append(dict(simbol = lab_map[i][j],
						x = i,
						y = j,
						path_length = 1,
						UP_check = False,
						DOWN_check = False,
						LEFT_check = False,
						 RIGHT_check = False))
	x, y = input('Enter star point x, y: ')

	return room, x, y

path = []
room, x, y = input_read()
search_function(room, x, y)
print path
