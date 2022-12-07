#import the turte module
from tkinter import font
import turtle

#initialization of the screen
wind = turtle.Screen()
wind.title("Ping Pong by Hamam")
wind.bgcolor("black")
wind.setup(width=800 , height=600)
wind.tracer(0)

#madrab 1, madrab2 and the ball
#madrab1
madrab1 = turtle.Turtle()
madrab1.speed(0)
madrab1.color("blue")
madrab1.shape("square")
madrab1.penup()
madrab1.goto(350,0)
madrab1.shapesize(stretch_len=1 , stretch_wid=5)

#madrab2
madrab2 = turtle.Turtle()
madrab2.speed(0)
madrab2.color("red")
madrab2.shape("square")
madrab2.penup()
madrab2.goto(-350,0)
madrab2.shapesize(stretch_len=1 , stretch_wid=5)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.color("white")
ball.shape("square")
ball.penup()
ball.goto(0,0)
ball.shapesize(stretch_len=1 , stretch_wid=1)
ball.dx = 0.15
ball.dy = 0.15

#score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,250)
score.write("Player : 0  Player : 0" , align="center" , font=("calibri",24,"normal"))

#movement of the madrab1 and madrab2 
def madrab1_up():
    y = madrab1.ycor()
    y += 20
    madrab1.sety(y)

def madrab1_down():
    y = madrab1.ycor()
    y -= 20
    madrab1.sety(y)

def madrab2_up():
    y = madrab2.ycor()
    y += 20
    madrab2.sety(y)

def madrab2_down():
    y = madrab2.ycor()
    y -= 20
    madrab2.sety(y)


#keyboard 
wind.listen()
wind.onkeypress(madrab1_up,"w")
wind.onkeypress(madrab1_down,"s")
wind.onkeypress(madrab2_up,"Up")
wind.onkeypress(madrab2_down,"Down")


#set up the loop
while True:
    wind.update()

    #ball movement
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    #check the borber
    if ball.ycor() > 290 :
        ball.sety(290) 
        ball.dy *= -1

    if ball.ycor() < -290 :
        ball.sety(-290) 
        ball.dy *= -1

    if ball.xcor() > 390 :
        ball.goto(0,0)
        ball.dx *= -1
        score.clear()
        score1 += 1
        score.write("Player : {}  Player : {}".format(score1,score2) , align="center" , font=("calibri",24,"normal"))

    if ball.xcor() < -390 :
        ball.goto(0,0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("Player : {}  Player : {}".format(score1,score2) , align="center" , font=("calibri",24,"normal"))

    #tasadom the ball with madrab1 and madrab2
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < madrab1.ycor() + 50 and ball.ycor() > madrab1.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1 
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < madrab2.ycor() + 50 and ball.ycor() > madrab2.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1 


