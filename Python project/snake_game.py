from time import *
from turtle import *
from random import *

delay = 0.2
w = Screen()
w.title("Snake Game")
w.bgcolor("green")
w.setup(width=600,height=600)
w.tracer(0)
#snake head
snake_head = Turtle()
snake_head.speed(0)
snake_head.shape("square")
snake_head.color("black")
snake_head.penup()
snake_head.goto(0,0)
snake_head.direction = "stop"

#food
snake_food = Turtle()
snake_food.speed(0)
snake_food.shape("circle")
snake_food.color("red")
snake_food.penup()
snake_food.goto(0,100)

body = []

def go_up():
    if snake_head.direction != "down":
        snake_head.direction = "up"

def go_down():
    if snake_head.direction != "up":
        snake_head.direction = "down"  

def go_left():
    if snake_head.direction != "right":
        snake_head.direction = "left"

def go_right():
    if snake_head.direction != "left":
        snake_head.direction = "right"      

#keyboard actions
w.listen()
w.onkeypress(go_up,"Up")
w.onkeypress(go_down,"Down")
w.onkeypress(go_left,"Left")
w.onkeypress(go_right,"Right")
w.onkeypress("close","q")
def motion():
    if snake_head.direction == "up":
        y = snake_head.ycor()
        snake_head.sety(y + 20)
    if snake_head.direction == "down":
        y = snake_head.ycor()
        snake_head.sety(y - 20)
    if snake_head.direction == "left":
        x = snake_head.xcor()
        snake_head.setx(x - 20)
    if snake_head.direction == "right":
        x = snake_head.xcor()
        snake_head.setx(x + 20)

#Main Function
while True:
    w.update()
    #check collisions
    if snake_head.xcor() > 290:
        snake_head.goto(-290,0)
    elif snake_head.xcor() < -290:
        snake_head.goto(290,0)
    elif snake_head.ycor() > 290:
        snake_head.goto(0,-290)
    elif snake_head.ycor() < -290:
        snake_head.goto(0,290)

    if snake_head.distance(snake_food) < 20:
        x = randint(-290,290)
        y = randint(-290,290)
        snake_food.goto(x,y)
        new_body = Turtle()
        new_body.speed(0)
        new_body.shape("square")
        new_body.color("black")
        new_body.penup()
        body.append(new_body)
    
    #body length of snake
    for i in range(len(body)-1,0,-1):
        x = body[i-1].xcor()
        y = body[i-1].ycor()
        body[i].goto(x,y)

    if len(body) > 0:
        x = snake_head.xcor()
        y = snake_head.ycor()
        body[0].goto(x,y)

    motion()
    #check body collisions
    for segment in body:
        if segment.distance(snake_head) < 20:
            sleep(1)
            snake_head.goto(0,0)
            snake_head.direction="stop"
            for segment in body:
                segment.goto(1000,1000)
                
            body.clear()  


    sleep(delay)

w.mainloop()