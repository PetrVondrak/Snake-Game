
from turtle import *
import time
import random

# Nastavení obrazovky hry.
screen = Screen()
screen.bgcolor("green")
screen.title("Snake Game")
screen.setup(width=500, height=500)
screen._root.resizable(False, False)
screen.tracer(False)

# Hlava hada.
head = Turtle("square")
head.color("black")
head.speed(0)
head.penup()
head.goto(x=0, y=0)
head.direction = "stop"

# Části těla hada.
body_parts = []

# Jablko pro hada.
apple = Turtle("circle")
apple.color("red")
apple.penup()
apple.goto(x=120, y=120)

# Proměnné pro počítání skóre.
score = 0
highest_score = 0

# Nastavení skóre ve hře.
score_sign = Turtle("turtle")
score_sign.color("white")
score_sign.speed(0)
score_sign.penup()
score_sign.hideturtle()
score_sign.goto(x=0, y=210)


# Funkce pro zobrazení skóre ve hře.
def score_label():
    score_sign.write(f"Actual score: {score} || Highest score: {highest_score}",
                      align="center", font=("Comic Sans MS", 18))
                            
score_label()


# Funkce pohybu hada, přesun na určité souřadnice.
def snake_move():
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


# Kolize hada způsobená překliknutím klávesy pohybu.
def move_up():
    if head.direction != "down":
        head.direction = "up" 

def move_down():
    if head.direction != "up":
        head.direction = "down"        

def move_left():
    if head.direction != "right":
        head.direction = "left"        

def move_right():
    if head.direction != "left":
        head.direction = "right"        

# Ovládání pohybu hada stisknutím klávesy.
screen.listen()
screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_right, "d")
screen.onkeypress(move_left, "a")


# Hlavní cyklus hry.
while True:
    screen.update()

    # Kontrola kolize s hranou obrazovky.
    if head.xcor() > 240 or head.xcor() < -240 or head.ycor() > 240 or head.ycor() < -240:
        time.sleep(1)        
        head.goto(x=0, y=0)      
        head.direction = "stop"
        apple.goto(x=120, y=120)
        
        # Skrytí částí těla.
        for one_body_part in body_parts:
            one_body_part.goto(x=1200, y=1200)

        # Vyprázdnění listu s částmi těla (šedé čtverečky).
        body_parts.clear()

        # Vynulování skóre při kolizí s hranou obrazovky.
        score = 0       
        score_sign.clear()
        score_label()

    # Přemisťování jablka / had sní jablko.
    if head.distance(apple) < 20:
        x = random.randint(-220, 220)
        y = random.randint(-220, 200)
        apple.goto(x, y)

        # Přidávání dalších části těla.
        new_body_part = Turtle("square")
        new_body_part.color("grey")
        new_body_part.speed(0)      
        new_body_part.penup()
        body_parts.append(new_body_part)

        # Počítání skóre a nejvyššího skóre.
        score = score + 10

        if score > highest_score:
            highest_score = score

        # Výpis skóre.
        score_sign.clear()
        score_label()

    # Počítání částí těla.
    for index in range(len(body_parts) -1, 0, -1):
        x = body_parts[index -1].xcor()
        y = body_parts[index -1].ycor()
        body_parts[index].goto(x, y)

    # Přidávání dalších části těla.
    if len(body_parts) > 0:
        x = head.xcor()
        y = head.ycor()
        body_parts[0].goto(x, y)

    snake_move()
    
    # Kontrola jestli hlava nenarazila do těla.
    for one_body_part in body_parts:
        if one_body_part.distance(head) < 20:
            time.sleep(1)         
            head.goto(x=0, y=0)           
            head.direction = "stop"
            apple.goto(x=120, y=120)
            
            # Skrytí částí těla.
            for one_body_part in body_parts:
                one_body_part.goto(x=1200, y=1200)

            # Vyprázdnění listu s částmi těla (šedé čtverečky).
            body_parts.clear()

            # Nulování a výpis skóre.
            score = 0
            score_sign.clear()
            score_label()

    # Rychlost hada.           
    time.sleep(0.12)
    