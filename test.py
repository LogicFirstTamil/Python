import turtle
import winsound

score_a = 0
score_b = 0

win = turtle.Screen()
win.title("Pong Game")
win.setup(800, 600)
win.bgcolor("blue")
win.tracer(0)

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.goto(-380,0)

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.penup()
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.goto(380,0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15
ball.dy = 0.15

#score
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.goto(0, 260)
pen.color("white")
pen.hideturtle()
pen.write("Player A: 0  Player B: 0",align="center",font=("Ariel",24,"normal"))

def paddle_a_up():
    paddle_a.sety(paddle_a.ycor()+20)
def paddle_a_down():
    paddle_a.sety(paddle_a.ycor()-20)
def paddle_b_up():
    paddle_b.sety(paddle_b.ycor()+20)
def paddle_b_down():
    paddle_b.sety(paddle_b.ycor()-20)


win.listen()
win.onkeypress(paddle_a_up,"w")
win.onkeypress(paddle_a_down,"s")
win.onkeypress(paddle_b_up,"Up")
win.onkeypress(paddle_b_down,"Down")

while True:
    win.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if(ball.ycor()>290):
        ball.sety(290)
        ball.dy *= -1
    if (ball.ycor() < -290):
        ball.sety(-290)
        ball.dy *= -1
    if (ball.xcor() > 390):
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Ariel", 24, "normal"))
    if (ball.xcor() < -390):
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Ariel", 24, "normal"))

    #collision with right paddle
    if ball.xcor()>380 and ball.ycor()<paddle_b.ycor()+50 and ball.ycor()>paddle_b.ycor()-50:
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.setx(360)
        ball.dx *= -1

    #collision with left paddle
    if ball.xcor() < -380 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.setx(-360)
        ball.dx *= -1
