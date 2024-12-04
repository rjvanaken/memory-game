import turtle
import time
from Config import Colors
from turtle_pos import player_pos


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
    screen = turtle.Screen()
    screen.bgcolor(Colors.off_white)
    screen.setup(1000, 800)
    turtle.hideturtle()

def splash_screen():
    set_tracer(0)
    screen = turtle.Screen()
    screen.register_shape("splash_cover.gif")
    splash = turtle.Turtle()
    splash.penup()
    splash.shape("splash_cover.gif")
    splash.setpos(0, 0)
    turtle.hideturtle()
    update_screen()
    time.sleep(1.5)
    splash.hideturtle()
    screen.update()

def transition():
    set_tracer(0)
    screen = turtle.Screen()
    screen.register_shape("cover.gif")
    cover = turtle.Turtle()
    cover.penup()
    cover.shape("cover.gif")
    cover.setpos(0, 0)
    time.sleep(0.25)
    turtle.hideturtle()
    update_screen()
    set_tracer(1)
    cover.speed(8)
    cover.setpos(1100, 0)






def setup_title():

    screen = turtle.Screen()
    screen.register_shape("BostonQuest.gif")
    title = turtle.Turtle()
    title.penup()
    title.shape("BostonQuest.gif")
    title.setpos(0, 340)
    turtle.hideturtle()

def setup_status_title(x, y):
    status = turtle.Turtle()
    status.speed(0)
    status.penup()
    status.goto(x, y)
    status.color(Colors.primary)
    status.write("Status:", align='left', font=("Georgia", 12, "bold"))
    status.hideturtle()

def background():

    screen = turtle.Screen()
    screen.register_shape("board_background.gif")
    background = turtle.Turtle()
    background.shape("board_background.gif")
    background.setpos(0, 0)
    turtle.hideturtle()

def create_status_tracker_obj():
    status_tracker = turtle.Turtle()
    status_tracker.hideturtle()
    status_tracker.speed(0)
    return status_tracker

def create_leaderboard_obj():
    leaderboard_turtle = turtle.Turtle()
    leaderboard_turtle.hideturtle()
    leaderboard_turtle.speed(0)
    return leaderboard_turtle

def display_leaderboard(dic, leaderboard_turtle):
    N = 7
    i = 0
    sorted_dict = dict(sorted(dic.items(), key=lambda item: item[1], reverse= False)[:N])
    leaderboard_turtle.clear()
    for key, value in sorted_dict.items():
        player = f"{key} : {value}"
        leaderboard_turtle.penup()
        leaderboard_turtle.goto(player_pos[i][0], player_pos[i][1])
        leaderboard_turtle.color(Colors.off_black)
        leaderboard_turtle.write(player, align='left', font=("Trebuchet MS", 12, "normal"))        
        leaderboard_turtle.hideturtle()
        i += 1

def display_game_status(status_tracker, attempts, matches):
    status_tracker.clear()
    status_tracker.penup()
    status_tracker.goto(-350, -343)
    status_tracker.color(Colors.off_black)
    if attempts == 1 and matches == 1:
        status_tracker.write(f"{attempts} move  | {matches} match", align='left', font=("Trebuchet MS", 12, "normal"))
    elif attempts == 1 and matches != 1:
        status_tracker.write(f"{attempts} move  | {matches} matches", align='left', font=("Trebuchet MS", 12, "normal"))
    elif attempts != 1 and matches == 1:
        status_tracker.write(f"{attempts} moves | {matches} match  ", align='left', font=("Trebuchet MS", 12, "normal"))
    else:
        status_tracker.write(f"{attempts} moves | {matches} matches", align='left', font=("Trebuchet MS", 12, "normal"))

    status_tracker.hideturtle()

def create_leaderboard_obj():
    leaderboard_turtle = turtle.Turtle()
    leaderboard_turtle.hideturtle()
    leaderboard_turtle.speed(0)
    return leaderboard_turtle


def create_win_message():
    win_msg = turtle.Turtle()
    win_msg.hideturtle()
    win_msg.speed(0)
    return win_msg

def create_card_count_message():
    card_count_msg = turtle.Turtle()
    card_count_msg.hideturtle()
    card_count_msg.speed(0)
    return card_count_msg

def create_quit_message():
    quit_msg = turtle.Turtle()
    quit_msg.hideturtle()
    quit_msg.speed(0)
    return quit_msg

def create_screen_blocker():
    screen_blocker = turtle.Turtle()
    screen_blocker.hideturtle()
    screen_blocker.speed(0)
    return screen_blocker


def set_tracer(tracer):
    screen = turtle.Screen()
    if tracer == True:
        screen.tracer(1)
    else: 
        screen.tracer(0)

def update_screen():
    screen = turtle.Screen()
    screen.update()


        
    
    

    