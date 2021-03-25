'''
Sadiqur Sakib
period 8
American Flag
'''

from turtle import *
from math import *

speed(0)# the speed at which turtle draws
colormode(255)
#the rectangle drawing
def rect(l1, l2):
    for i in range(2):
        fd(l1)
        rt(90)
        fd(l2)
        rt(90)
#picks the pen up and moves to a specific x and y coordinates
def moveto(x, y):
    pu()
    goto(x, y)
    pd()

moveto(-300,0)
#All the variables
hoist = 300 # width of flag
fly = 1.9 * hoist # length of flag
strip_width = .0769 * hoist # the width of the strip
union_fly = 0.76 * hoist
union_hoist = 0.5380 * hoist
k = 0.0616 * hoist # diamater of the star
e = 0.063 * hoist
g = 0.054 * hoist
homex = xcor()
homey = ycor()

#draws the amount of rows of the star which is represented by x
def star_row(x):
    for i in range(x):
        star(k / 2)
        moveto(xcor() + e * 2, ycor() + 0)

#this is the blue rectange union
def union(side1, side2):
    color(60, 59, 110)
    begin_fill()
    for i in range(2):
        fd(side1)
        rt(90)
        fd(side2)
        rt(90)
    end_fill()
#the definition of star

def star(r):
    pu()
    size = k / 2 # the size of star
    s = r * sin(radians(36)) / sin(radians(126))
    goto(xcor(), ycor() + r)
    circle(-r)
    rt(72)
    pd()
    color(255, 255, 255) # the color white
    begin_fill()
    for i in range(5):
        fd(s)
        lt(72)
        fd(s)
        rt(144)
    end_fill()
    goto(xcor(), ycor() - r)
    setheading(0)

rect(fly, hoist)
for i in range(13):# the 13 strips of the flag
    if(i % 2 == 0):
        fillcolor(178, 34, 52) #the red strip of the flag
    else:
        fillcolor(255, 255, 255) # the white strip of the flag
    begin_fill()
    rect(fly, strip_width)
    moveto(xcor(), ycor() - strip_width)
    end_fill()
moveto(homex, homey)
color(60, 59, 110)#the blue union
begin_fill()
rect(union_fly, union_hoist)
end_fill()
#this draws the stars

for i in range(4):#the second row of stars
    moveto(homex, homey)
    moveto(xcor() + e * 2, ycor() - g * (2 + i * 2))
    star_row(5)

for i in range(5):# the first row of stars
    moveto(homex,homey)
    moveto(xcor() + e, ycor() - g * (1 + i * 2))
    star_row(6)
moveto(-300,0)# removes the pen off the flag

exitonclick()