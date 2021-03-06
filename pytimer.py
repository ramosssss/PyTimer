#!/usr/bin/env python3

"""
  Tkinter Python egg timer

	Enter the number of minutes (or the alarm time as HH:MM)
	into the text entry and click the Start button
"""

import sys, time
from tkinter import *
import play_wav

wav = "Question.wav"
sound = play_wav.Sound()
run = False
curtime = 10
altime = time.time() + 1e8

def play_alarm():
	sound.playFile(wav)
	curtime = time.time() - altime
	tt.config(state = "normal")
	tt.delete(0, END)
	tt.insert(0, "−%u:%02u" % (curtime // 60, curtime % 60))
	tt.config(state="disabled")
	master.after(1200, play_alarm)

def start(s = ''):
	global run, curtime, altime

	if run and curtime < 1:
		sys.exit(0)

	if not run:
		run = True
		but.config(background = "green")
		a = tt.get()
		if ':' in a:	# input is HH:MM time
			b = list(time.localtime())
			b[3], b[4] = [int(x) for x in a.split(':')]
			b[5] = 0
			altime = time.mktime(tuple(b))
			if altime < time.time():	# alarm time is tomorrow
				altime += 24*60*60
		else:		# input is minutes
			try:
				mins = int(a)
			except:
				mins = 1	# default: one-minute countdown
			altime = 60 * mins + time.time()
		tt.config(justify = "right", state = "disabled")

def showtime():
	global curtime

	curtime = max(0, int(altime - time.time()))

	if run:
		tt.config(state = "normal")
		tt.delete(0, END)
		tt.insert(0, "%u:%02u" % (curtime // 60, curtime % 60))
		if curtime < 30:
			but.config(background = "yellow")
		if curtime < 2:
			but.config(background = "red", text = "   Quit   ")
		tt.config(state="disabled")
	if curtime > 0:
		master.after(1000, showtime)
	else:
		master.after(50, play_alarm)

master = Tk()

f1 = Frame(master)
f1.pack(side = TOP, fill = Y)
f2 = Frame(master)
f2.pack(side = TOP, fill = Y)

tt = Entry(f2, width = 8)
tt.pack(side = LEFT)
tt.delete(0, END)
tt.bind('<Return>', start)
tt.focus()

but = Button(f1, text = "  Start  ", command = start)
but.pack(side = LEFT)

master.title("PyTimer")

master.after(1000, showtime)

mainloop()

