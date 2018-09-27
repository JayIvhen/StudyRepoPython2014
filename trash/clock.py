#!usr\bin\python

""" Floating Clock

Program for comand line interpreter. Random floating clock.

"""

__author__ = "JayIvhen"

import os
import datetime
import curses
import random

time = []

DT = datetime.datetime.now


def rand_p_m_1():
	return random.randrange(-1,2,2)
def new_coord(hight, width, stdscr):
	hight = hight + rand_p_m_1()
	if hight <= 0:
		hight = 2
	if hight >= stdscr.getmaxyx()[0] - 8:
		hight = stdscr.getmaxyx()[0] - 9
	width = width + rand_p_m_1()
	if width <= 0:
		width = 2
	if width >= stdscr.getmaxyx()[1] - 25:
		width = stdscr.getmaxyx()[1] - 27 
	return hight, width
def create_clock_strings(time, starttime, timer):
	time = []
	time.append("Year: " + str(DT().year))
	time.append("Month: " + str(DT().month))
	time.append("Day :" + str(DT().day))	
	time.append("Start time: " + str(starttime[1]) + ":" + 
				     str(starttime[2]) + ":" +
				     str(starttime[3])
		   )	
	time.append("Time: " + str(DT().hour) + ":" + str(DT().minute) + ":" +
		               str(DT().second)
		   )
	time.append("Time spent: " + str(timer[0]) + ":" + str(timer[1]) 
				   + ":" + str(timer[2])
		   )
	time.append("Press S to exit")
	return time
def timer(start):
	start_sec = (start[3] + start[2] * 60 +
		     start[1] * 60 * 60 + start[0] * 60 * 60 * 24)
	now = (DT().day, DT().hour, DT().minute, DT().second)
	now_sec = (now[3] + now[2] * 60 + 
                   now[1] * 60 * 60 + now[0] * 60 * 60 * 24)
	timer_sec = now_sec - start_sec
	timer_h = timer_sec / 60 / 60
	timer_m = timer_sec / 60 % 60
	timer_s = timer_sec % 60
	return (timer_h, timer_m, timer_s)
def curses_start():
	stdscr= curses.initscr()
	curses.noecho()
	curses.cbreak()
	stdscr.keypad(True)
	stdscr.nodelay(True)
	return stdscr
def curses_stop(stdscr):
	curses.nocbreak()
	stdscr.keypad(False)
	curses.echo()
	curses.endwin()
def main(stdscr):
	time = []
	hight, width = stdscr.getmaxyx()
	hight = hight / 2
	width = width / 2
	old_time = DT().second
	start_time = (DT().day, DT().hour, DT().minute, DT().second)
	while True:
		if  old_time != DT().second:
			old_time = DT().second
			stdscr.refresh()
			stdscr.erase()
			stdscr.border()
			time = create_clock_strings(time, start_time, 
						    timer(start_time)
						   )			
			for i in xrange(len(time)):		
				stdscr.addnstr(hight + i, width,
					       time[i], len(time[i])
					      )
			hight, width = new_coord(hight, width, stdscr)
			c = stdscr.getch()
			if c == ord("s"):
				break
scr = curses_start()
main(scr)
curses_stop(scr)
