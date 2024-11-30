import turtle
import time
from Config import Colors

# def splash_screen


def setup_user():
    user = ''
    screen = turtle.Screen()
    user = screen.textinput("Name", "Enter your name:")
    return user


def setup_card_count():
    screen = turtle.Screen()
    card_count = screen.textinput("Cards", "Enter the number of cards you woud like to play with (8, 10, or 12): ")
    return card_count

def setup_game_space():

    turtle.title('Memory Game')
    turtle.hideturtle()
    screen = turtle.Screen()
    screen.bgcolor(Colors.off_white)
    screen.setup(900, 900)

def setup_title():

    background()
    title = turtle.Turtle()
    title.penup()
    title.up()
    title.goto(0, 340)
    title.color(Colors.secondary)
    title.write("Boston Quest", align='center', font=("Times New Roman", 16, "bold"))
    title.hideturtle()
    subtitle = turtle.Turtle()
    subtitle.penup()
    subtitle.goto(0, 315)
    subtitle.color(Colors.off_black)
    subtitle.write("The ultimate Boston memory test", align='center', font=("Arial", 10, "normal"))
    subtitle.hideturtle()

def background():

    screen = turtle.Screen()
    screen.register_shape("giftest.gif")
    background = turtle.Turtle()
    background.shape("giftest.gif")
    background.setpos(0, 0)

def quit_button():
    screen = turtle.Screen()
    screen.register_shape('quit_button.gif')
    quit_button = turtle.Turtle()
    quit_button.penup()
    quit_button.shape('quit_button.gif')
    quit_button.setpos(87, -189)
    quit_button.speed(0)
    # quit_button.onclick(screen.bye())

def set_tracer(tracer):
    screen = turtle.Screen()
    if tracer == True:
        screen.tracer(1)
    else: 
        screen.tracer(0)

def update_screen():
    screen = turtle.Screen()
    screen.update()

def screen_delay():
    time.sleep(0.5)

        
    
    

    