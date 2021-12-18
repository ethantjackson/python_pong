from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(800, 600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

p1 = Paddle(-360, 0)
p2 = Paddle(350, 0)
ball = Ball()
screen.onkey(p1.up, "w")
screen.onkey(p1.down, "s")
screen.onkey(p2.up, "Up")
screen.onkey(p2.down, "Down")

game_running = True

while game_running:
    screen.update()
    ball.move()
    if (abs(ball.pos_x - p2.xcor()) < 20 and abs(ball.pos_y - p2.ycor()) < 60) or \
            (abs(ball.pos_x - p1.xcor()) < 20 and abs(ball.pos_y - p1.ycor()) < 60):
        ball.vel_x *= -1
    if abs(ball.pos_y) > 290:
        ball.vel_y *= -1
    if abs(ball.pos_x) > 385:
        game_running = False
    time.sleep(0.01)

screen.exitonclick()
