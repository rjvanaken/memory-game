import turtle
import game_helpers
from Card import Card
from Config import Colors
from data import positions

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


def game_board():
    game_helpers.shuffle_cards()
    index = 0
    for index in range(len(positions)):
        Card(index, positions[index][0], positions[index][1])
        index += 1
        


        
        
            

def background():
    screen = turtle.Screen()
    screen.register_shape("bg_test.gif")
    background = turtle.Turtle()
    background.shape("bg_test.gif")
    background.setpos(0, 0)

        
    
    

    