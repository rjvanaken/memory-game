import turtle
import time
from Config import Colors
from data import player_pos

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

def display_leaderboard(dic, x, y):
    N = 5
    i = 0
    sorted_dict = dict(sorted(dic.items(), key=lambda item: item[1], reverse= True)[:N])
    for key, value in sorted_dict.items():
        player = f"{key} : {value}"
        print(player)
        leaderboard_turtle = turtle.Turtle()
        leaderboard_turtle.penup()
        leaderboard_turtle.goto(player_pos[i][0], player_pos[i][1])
        leaderboard_turtle.color(Colors.off_black)
        leaderboard_turtle.write(player, align='left', font=("Arial", 12, "normal"))        
        leaderboard_turtle.hideturtle()
        i += 1



def quit_button():
    screen = turtle.Screen()
    screen.register_shape('quit_button.gif')
    quit_button = turtle.Turtle()
    quit_button.penup()
    quit_button.shape('quit_button.gif')
    quit_button.setpos(87, -189)
    # quit_button.onclick(screen.bye())

def display_win_message():
    pass
    screen = turtle.Screen()
    screen.register_shape('winner.gif')
    win_msg = turtle.Turtle()
    win_msg.penup()
    win_msg.shape('winner.gif')
    win_msg.setpos(0, 0)
    print('You win!')

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
    time.sleep(0.25)

        
    
    

    