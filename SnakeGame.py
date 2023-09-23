import turtle
import time
import random


win = turtle.Screen()
win.title("Snake")
win.setup(1200, 800)
win.bgcolor("dark slate gray")
win.tracer(0)


menu = turtle.Pen()
menu.penup()
menu.speed("fastest")
menu.goto(-130, 100)
menu.color("white")
menu.write(" SNAKE GAME", font=("Arial", 30, "bold"))
menu.hideturtle()

start = turtle.Pen()
start.penup()
start.speed("fastest")
start.goto(-160, 20)
start.color("white")
start.write("- PRESS  'Y'  TO  START  NEW  GAME", font=("Arial", 14, "bold"))
start.hideturtle()

# ============= xử lí start game ==================
speed_game = 18
def star_game (speed_game):
    win.clear()
    win.setup(1200, 800)
    win.bgcolor("dark slate gray")
    win.tracer(0)
    player_name = turtle.textinput("please type your name", "Your name:")
    
    
    #border
    for i in range(-400, 400, 30):
        border = turtle.Pen()
        border.penup()
        border.speed("fastest")
        border.color("white")
        border.goto(200, i)
        border.write("|",font=("Arial", 24, "bold") )
        border.hideturtle()


    for i in range(204,600, 10):
        border = turtle.Pen()
        border.penup()
        border.speed("fastest")
        border.color("white")
        border.goto(i, 0)
        border.write("_",font=("Arial", 24, "bold") )
        border.hideturtle()
        
    name = turtle.Pen()
    name.penup()
    name.speed("fastest")
    name.color("white")
    name.goto(230, 300)
    name.write("Player:   " + player_name ,font=("Arial", 15, "bold") )
    name.hideturtle()
    
    score = 0
    score_text = turtle.Pen()
    score_text.penup()
    score_text.speed("fastest")
    score_text.goto(230, 240)
    score_text.color("white")
    score_text.write("Your Score:", font=("Arial", 15, "bold"))
    score_text.hideturtle()

    score_num = turtle.Pen()
    score_num.penup()
    score_num.speed("fastest")
    score_num.color("white")
    score_num.goto(370, 240)
    score_num.write(score,font=("Arial", 15, "bold") )
    score_num.hideturtle()
    
    snake = turtle.Pen()
    snake.penup()
    snake.shape("triangle")
    snake.color("red")

    food_1 = turtle.Pen()
    food_1.penup()
    food_1.color("yellow")
    food_1.shape("turtle")
    food_1.speed("fastest")
    food_1.goto(random.randint(-520, 130), random.randint(-360,360))
    food_1.hideturtle()

    food_2 = turtle.Pen()
    food_2.penup()
    food_2.color("red")
    food_2.shape("turtle")
    food_2.speed("fastest")
    food_2.goto(random.randint(-520, 130), random.randint(-360,360))
    food_2.hideturtle()

    foods = [food_1, food_2]
    food = random.choice(foods)
    food.goto(0,0)
    food.showturtle()

    def up():
        snake.setheading(90)

    def down():
        snake.setheading(-90)
    
    def left():
        snake.setheading(180)    

    def right():
        snake.setheading(0)
    
    win.listen()
    win.onkey(up, "Up")
    win.onkey(down, "Down")
    win.onkey(left, "Left")
    win.onkey(right, "Right")

    food_3 = turtle.Pen()
    food_3.penup()
    food_3.shape("turtle")
    food_3.speed("fastest")
    food_3.color("maroon")
    food_3.hideturtle()

    time_food_3 = 0

    snake_body = []

    
    while True:
        win.update()
        time.sleep(0.1)
    
        if snake.xcor() > 199 or snake.xcor() < -599 or snake.ycor() > 399 or snake.ycor() < -399:
            win.clear()
            win.setup(1200, 800)
            win.bgcolor("dark slate gray")
            win.tracer(0)
                
            menu = turtle.Pen()
            menu.penup()
            menu.speed("fastest")
            menu.goto(-130, 100)
            menu.color("white")
            menu.write(" GAME OVER", font=("Arial", 30, "bold"))
            menu.hideturtle()
                
            total_score_text = turtle.Pen()
            total_score_text.penup()
            total_score_text.speed("fastest")
            total_score_text.goto(-160, 20)
            total_score_text.color("white")
            total_score_text.write("- YOUR SCORE: ", font=("Arial", 14, "bold"))
            total_score_text.hideturtle()
                
            total_score_num = turtle.Pen()
            total_score_num.penup()
            total_score_num.speed("fastest")
            total_score_num.color("white")
            total_score_num.goto(30, 20)
            total_score_num.write(score,font=("Arial", 15, "bold") )
            total_score_num.hideturtle()
                
        if snake.distance(food) < 30:
            item = turtle.Pen()
            item.penup()
            item.speed("fastest")
            item.shape("circle")
            item.color("green yellow")
            if food == food_1:
                score = score + 1
                snake_body.append(item)   
            if food == food_2:
                score = score + 2
                snake_body.append(item)   
            score_num.clear()
            score_num.write(score, font=("Arial", 20, "bold"))
            food.hideturtle()
            food = random.choice(foods)
            food.goto(random.randint(-520, 130), random.randint(-360,360))
            food.showturtle()
        
        

        if random.randint(0,50) == 1:
            food_3.showturtle()
            food_3.goto(random.randint(-520, 130), random.randint(-360,360))
        time_food_3 = time_food_3 + 1
        if time_food_3 == 100:
            food_3.hideturtle()
            time_food_3 = 0
        
        if snake.distance(food_3) < 30:
            score = score - 2
            food_3.goto(random.randint(-520, 130), random.randint(-360,360))
            score_num.clear()
            score_num.write(score, font=("Arial", 20, "bold"))
        
        if len(snake_body) > 0:
            for i in range (len(snake_body) -1, 0, -1):
                snake_body[i].goto(snake_body[i-1].xcor(),snake_body[i-1].ycor())
            snake_body[0].goto(snake.xcor(), snake.ycor() )
        snake.forward(speed_game)
        
        for item in snake_body:
            if snake.distance(item) < 5:
                
                
                win.clear()
                win.setup(1200, 800)
                win.bgcolor("dark slate gray")
                win.tracer(0)
                
                menu = turtle.Pen()
                menu.penup()
                menu.speed("fastest")
                menu.goto(-130, 100)
                menu.color("white")
                menu.write(" GAME OVER", font=("Arial", 30, "bold"))
                menu.hideturtle()
                
                total_score_text = turtle.Pen()
                total_score_text.penup()
                total_score_text.speed("fastest")
                total_score_text.goto(-160, 20)
                total_score_text.color("white")
                total_score_text.write("- YOUR SCORE: ", font=("Arial", 14, "bold"))
                total_score_text.hideturtle()
                
                total_score_num = turtle.Pen()
                total_score_num.penup()
                total_score_num.speed("fastest")
                total_score_num.color("white")
                total_score_num.goto(30, 20)
                total_score_num.write(score,font=("Arial", 15, "bold") )
                total_score_num.hideturtle()
                

#================= xử lí setting =================
def setting():
    win.clear()
    win.setup(1200, 800)
    win.bgcolor("dark slate gray")
    win.tracer(0)
    
    setting_s = turtle.Pen()
    setting_s.penup()
    setting_s.speed("fastest")
    setting_s.goto(-130, 100)
    setting_s.color("white")
    setting_s.write("WELL COME", font=("Arial", 30, "bold"))
    setting_s.hideturtle()
    
    s1 = turtle.Pen()
    s1.penup()
    s1.speed("fastest")
    s1.goto(-130, 50)
    s1.color("white")
    s1.write("1.  DIFFICULT", font=("Arial", 14, "bold"))
    s1.hideturtle()
    
    s2 = turtle.Pen()
    s2.penup()
    s2.speed("fastest")
    s2.goto(-130, 0)
    s2.color("white")
    s2.write("2.  MEDIUM", font=("Arial", 14, "bold"))
    s2.hideturtle()
    
    s3 = turtle.Pen()
    s3.penup()
    s3.speed("fastest")
    s3.goto(-130, -50)
    s3.color("white")
    s3.write("3.  EASY", font=("Arial", 14, "bold"))
    s3.hideturtle()
    
    def dificult():
        speed_game = 18
        win.clear()
        star_game(speed_game)
    def medium():
        speed_game = 16
        star_game(speed_game)
    def easy():
        speed_game = 14
        star_game(speed_game)
    
    win.listen()
    win.onkey(dificult, "1")
    win.onkey(medium, "2")
    win.onkey(easy, "3")
    
# ===========================================            
win.listen()
win.onkey(setting, "y")

turtle.done()
