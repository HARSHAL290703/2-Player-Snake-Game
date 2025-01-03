import turtle
import time
import random


# Game settings
default_delay = 0.1
delay = default_delay
level = 1

# Scores for both players
score1 = 0
score2 = 0
high_score1 = 0
high_score2 = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game by Group 14")
wn.bgcolor("green")
wn.setup(width=800, height=800)
wn.tracer(0)  # Turns off the screen updates




# Snake head 1
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("orange")
head.penup()
head.goto(-100, 0)
head.direction = "stop"

# Snake head 2
head2 = turtle.Turtle()
head2.speed(0)
head2.shape("square")
head2.color("blue")
head2.penup()
head2.goto(100, 0)
head2.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Segments for both players
segments = []
segments2 = []

# Pen for displaying scores
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 340)
pen.write(f"Player 1 Score: {score1}  Player 2 Score: {score2}", align="center", font=("courier", 20, "normal"))
pen.goto(0, 310)      
pen.write(f"High Score 1: {high_score1}  High Score 2: {high_score2}  Level: {level}", align="center", font=("courier", 20, "normal"))



# Functions for player 1
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

# Functions for player 2
def go_up2():
    if head2.direction != "down":
        head2.direction = "up"

def go_down2():
    if head2.direction != "up":
        head2.direction = "down"

def go_left2():
    if head2.direction != "right":
        head2.direction = "left"

def go_right2():
    if head2.direction != "left":
        head2.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

def move2():
    if head2.direction == "up":
        y = head2.ycor()
        head2.sety(y + 20)
    if head2.direction == "down":
        y = head2.ycor()
        head2.sety(y - 20)
    if head2.direction == "left":
        x = head2.xcor()
        head2.setx(x - 20)
    if head2.direction == "right":
        x = head2.xcor()
        head2.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

wn.onkeypress(go_up2, "i")
wn.onkeypress(go_down2, "k")
wn.onkeypress(go_left2, "j")
wn.onkeypress(go_right2, "l")

# Main game loop
while True:
    wn.update()

    # Check for collision with the border for player 1
    if head.xcor() > 360 or head.xcor() < -360 or head.ycor() > 360 or head.ycor() < -360:
        head.goto(-100, 0)
        head.direction = "stop"
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score1 = 0
        level = 1
        delay = default_delay 
        pen.clear()
        pen.goto(0, 340)  
        pen.write(f"Player 1 Score: {score1}  Player 2 Score: {score2}", align="center", font=("courier", 20, "normal"))
       
        pen.goto(0, 310)
        pen.write(f"High Score 1: {high_score1}  High Score 2: {high_score2}  Level: {level}", align="center", font=("courier", 20, "normal"))
          
    if head2.xcor() > 360 or head2.xcor() < -360 or head2.ycor() > 360 or head2.ycor() < -360:
        head2.goto(100, 0)
        head2.direction = "stop"
        for segment2 in segments2:
            segment2.goto(1000, 1000)
        segments2.clear()
        score2 = 0
        level = 1
        delay = default_delay
        pen.clear()
        pen.goto(0, 340)
        pen.write(f"Player 1 Score: {score1}  Player 2 Score: {score2}", align="center", font=("courier", 20, "normal"))
          
        pen.goto(0, 310)
        pen.write(f"High Score 1: {high_score1}  High Score 2: {high_score2}  Level: {level}", align="center", font=("courier", 20, "normal"))
         

    # Check for collision with the food for player 1
    if head.distance(food) < 20:
        x = random.randrange(-280, 280, 20)
        y = random.randrange(-280, 280, 20)
        food.goto(x, y)
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
        score1 += 10
        if score1 > high_score1:
            high_score1 = score1
            
        if score1 > 50 and score1 <= 100:
            delay = 0.08  # Increase speed after score exceeds 50
            level = 2
        elif score1 > 100:
            delay = 0.05
            level = 3
                
        pen.clear()
        pen.goto(0, 340)
        pen.write(f"Player 1 Score: {score1}  Player 2 Score: {score2}", align="center", font=("courier", 20, "normal"))
          
        pen.goto(0, 310)
        pen.write(f"High Score 1: {high_score1}  High Score 2: {high_score2}  Level: {level}", align="center", font=("courier", 20, "normal"))
         


    # Check for collision with the food for player 2
    if head2.distance(food) < 20:
        x = random.randrange(-280, 280, 20)
        y = random.randrange(-280, 280, 20)
        food.goto(x, y)
        new_segment2 = turtle.Turtle()
        new_segment2.speed(0)
        new_segment2.shape("square")
        new_segment2.color("grey")
        new_segment2.penup()
        segments2.append(new_segment2)
        score2 += 10
        if score2 > high_score2:
            high_score2 = score2
            
        if score2 > 50 and score2 <= 100:
            delay = 0.08  # Increase speed after score exceeds 50
            level = 2
        elif score2 > 100:
            delay = 0.05
            level = 3

        pen.clear()
        pen.goto(0, 340)
        pen.write(f"Player 1 Score: {score1}  Player 2 Score: {score2}", align="center", font=("courier", 20, "normal"))
          
        pen.goto(0, 310)
        pen.write(f"High Score 1: {high_score1}  High Score 2: {high_score2}  Level: {level}", align="center", font=("courier", 20, "normal"))
         


    # Move the end segments for player 1 in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    # Move the end segments for player 2 in reverse order
    for index in range(len(segments2) - 1, 0, -1):
        x = segments2[index - 1].xcor()
        y = segments2[index - 1].ycor()
        segments2[index].goto(x, y)
    if len(segments2) > 0:
        x = head2.xcor()
        y = head2.ycor()
        segments2[0].goto(x, y)

    move()
    move2()

    # Check for collisions with body segments for player 1
    for segment in segments:
        if segment.distance(head) < 20:
            head.goto(-100, 0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score1 = 0
            level = 1
            delay = default_delay
            pen.clear()
            pen.goto(0, 340)
            pen.write(f"Player 1 Score: {score1}  Player 2 Score: {score2}", align="center", font=("courier", 20, "normal"))
              
            pen.goto(0, 310)
            pen.write(f"High Score 1: {high_score1}  High Score 2: {high_score2}  Level: {level}", align="center", font=("courier", 20, "normal"))
             


    # Check for collisions with body segments for player 2
    for segment2 in segments2:
        if segment2.distance(head2) < 20:
            head2.goto(100, 0)
            head2.direction = "stop"
            for segment2 in segments2:
                segment2.goto(1000, 1000)
            segments2.clear()
            score2 = 0
            level = 1
            delay = default_delay
            pen.clear()
            pen.goto(0, 340)
            pen.write(f"Player 1 Score: {score1}  Player 2 Score: {score2}", align="center", font=("courier", 20, "normal"))
              
            pen.goto(0, 310)
            pen.write(f"High Score 1: {high_score1}  High Score 2: {high_score2}  Level: {level}", align="center", font=("courier", 20, "normal"))
             

    # Check for collision between the two players
    if head.distance(head2) < 20 or any(segment.distance(head2) < 20 for segment in segments) or any(segment2.distance(head) < 20 for segment2 in segments2):
        head.goto(-100, 0)
        head2.goto(100, 0)
        head.direction = head2.direction = "stop"
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        for segment2 in segments2:
            segment2.goto(1000, 1000)
        segments2.clear()
        score1 = score2 = 0
        level = 1
        delay = default_delay
        pen.clear()
        pen.goto(0, 340)
        pen.write(f"Player 1 Score: {score1}  Player 2 Score: {score2}", align="center", font=("courier", 20, "normal"))
          
        pen.goto(0, 310)
        pen.write(f"High Score 1: {high_score1}  High Score 2: {high_score2}  Level: {level}", align="center", font=("courier", 20, "normal"))
    
      # Levels

     


    time.sleep(delay)

wn.mainloop()
