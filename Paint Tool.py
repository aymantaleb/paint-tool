import turtle
import sys
import time
from tkinter import *

sys.setrecursionlimit(1000)
wn = turtle.Screen()
red = turtle.Turtle()
blue = turtle.Turtle()
green = turtle.Turtle()
yellow = turtle.Turtle()
purple = turtle.Turtle()
orange = turtle.Turtle()
pink = turtle.Turtle()
ext = turtle.Turtle()
clear = turtle.Turtle()
tool = turtle.Turtle()
black = turtle.Turtle()
incSize = turtle.Turtle()
decSize = turtle.Turtle()
resetSize = turtle.Turtle()
n = -290
tool.penup()
tool.speed(0)
tool.shape('arrow')
window = turtle.Screen()

canvas = turtle.getcanvas()         

def IncSize(z, y):
	x = int(tool.pensize())
	x = x + 1
	tool.pensize(x)
	tool.resizemode('auto')
	print(x)

def DecSize(z, y):
	x = int(tool.pensize())
	x = x - 1
	if x == 0:
		x = 1
	tool.pensize(x)
	tool.resizemode('auto')
	print (x)

def ResetSize():
	tool.pensize(1)

incSize.shape('triangle')
incSize.shapesize(2)
incSize.left(90)
decSize.shape('triangle')
decSize.shapesize(2)
decSize.right(90)

turtleMoving = False

def draw(event):
	global turtleMoving
	if turtleMoving:
		return
	turtleMoving = True
	if event.y > 63:
		print(event.x, event.y)
		width = turtle.window_width()
		height = turtle.window_height()
		tool.goto(event.x-width/2, height/2 - event.y)
		tool.pendown()
		time.sleep(0.001)
	turtleMoving = False

tool.ondrag(None)
canvas.bind('<B1-Motion>', draw)
  
def Red(x, y):
	tool.color('red')
def Blue(x, y):
	tool.color('blue')
def Green(x, y):
	tool.color('green')
def Yellow(x, y):
	tool.color('yellow')
def Purple(x, y):
	tool.color('purple')
def Orange(x, y):
	tool.color('orange')
def Pink(x, y):
	tool.color('pink')
def Black(x, y):
	tool.color('black')
for i in (red, blue, green, yellow, purple, orange, pink, ext, clear, black, tool, incSize, decSize, resetSize):
	i.speed(300)
tool.left(90)
red.color('red')
blue.color('blue')
green.color('green')
yellow.color('yellow')
purple.color('purple')
orange.color('orange')
pink.color('pink')
tool.color('black')

for i in (ext, clear, resetSize):
	i.hideturtle()
for i in (red, blue, green, yellow, purple, orange, pink, black):
	i.shapesize(1)
	i.shape("square")
for i in (red, blue, green, yellow, purple, orange, pink, black, incSize, decSize):
	i.penup()
	i.setposition(n,360)
	n = n + 35
ext.penup()
ext.setposition(-450, 380)
ext.write('Press ESC to exit')
clear.penup()
clear.setposition(-450, 370)
clear.write('Press C to clear')
resetSize.penup()
resetSize.setposition(-450, 360)
resetSize.write('Press R to Reset pen size')






red.onclick(Red)
blue.onclick(Blue)
green.onclick(Green)
yellow.onclick(Yellow)
purple.onclick(Purple)
orange.onclick(Orange)
pink.onclick(Pink)
black.onclick(Black)
incSize.onclick(IncSize)
decSize.onclick(DecSize)

def close():
	wn = turtle.Screen()
	wn.bye()
def Clear():
	tool.clear()
wn.onkey(ResetSize, "r")
wn.title("Paint Tool")
wn.onkey(Clear, "c")
wn.onkey(close, "Escape")
wn.listen()

turtle.mainloop()
