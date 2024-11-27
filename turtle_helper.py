import turtle
from Card import Card
from Config import Colors
from data import positions

def register_shapes():
    pass

def setup_game_space():

    turtle.title('Memory Game')
    turtle.hideturtle()
    screen = turtle.Screen()
    screen.bgcolor(Colors.off_white)
    screen.setup(1000, 1000)
    turtle.up()
    turtle.goto(0, 430)
    background()
    turtle.color(Colors.secondary)
    turtle.write("Boston Quest", align='center', font=("Times New Roman", 16, "bold"))
    turtle.hideturtle()


def background():
    screen = turtle.Screen()
    screen.register_shape("board_background.gif")
    background = turtle.Turtle()
    background.shape("board_background.gif")
    background.setpos(0, 0)

        
    
    

    