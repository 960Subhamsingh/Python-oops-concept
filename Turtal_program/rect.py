import turtle 
import  colorsys
turtle.bgcolor("black")
turtle.speed(0)
for i in range(2001):
    color = colorsys.hsv_to_rgb(i/100 , 1.0 ,1.0)
    turtle.color(color)
    turtle.forward(i)
    turtle.right(120)