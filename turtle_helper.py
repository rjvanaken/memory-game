'''
    Rebecca Van Aken
    CS 5001, Fall, 2024
    Final Project

    This file contains helper functions that require the use of the turtle module for the Memory Game.

'''

import turtle
import time
from Colors import Colors
from turtle_pos import player_pos


def setup_user():
    '''
        Function: setup_user()

        Does: displays the text input for the player to enter their name

        Returns:
            - user: a string, the name of the player
    
    '''
    user = ''
    screen = turtle.Screen()
    user = screen.textinput("Name", "Enter your name:")
    return user


def setup_card_count():
    '''
        Function: setup_card_count()

        Does: displays the text input for the user to enter the number of 
        cards they would like to play the game with: 8, 10, or 12

        Returns:
            - card_count: an int, the number of cards the user would like to 
            play with: 8, 10, or 12.
    '''
    screen = turtle.Screen()
    card_count = screen.textinput(
        "Cards", 
        "Enter the number of cards you'd like to play with (8, 10, or 12):")
    return card_count

def setup_config_file():
    '''
        Function: setup_config_file()

        Does: displays the text input for the user to enter the name of the 
        configuration file the user wants the game to retrieve the names for 
        the images to use in the game

        Returns:
            - config_file: a string, the name of the configuration file to use
    '''
    screen = turtle.Screen()
    config_file = screen.textinput(
        'Card Configuration', 
        "Enter the config file name with the image directory you want to use")
    return config_file



def setup_game_space():
    '''
        Function: setup_game_space()

        Does: Sets up the program name, background color, and
        screen size

    '''

    turtle.title('Memory Game')
    screen = turtle.Screen()
    screen.bgcolor(Colors.off_white)
    screen.setup(1000, 800)
    turtle.hideturtle()

def splash_screen():
    '''
        Function: splash_screen()

        Does: Displays the splash screen when the game is first launched
        for 1.5 seconds
    
    '''
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
    '''
        Function: transition()

        Does: Creates the cover image and executes the transition to 
        reveal the game board after it's all initialized
    
    '''
    set_tracer(0)
    screen = turtle.Screen()
    # register and display the cover shape
    screen.register_shape("cover.gif")
    cover = turtle.Turtle()
    cover.penup()
    cover.shape("cover.gif")
    cover.setpos(0, 0)
    time.sleep(0.25)
    turtle.hideturtle()
    update_screen()
    set_tracer(1)
    # set the cover's speed to 8 and move it off screen for a transition
    # effect
    cover.speed(8)
    cover.setpos(1100, 0)


def setup_status_title(x, y):
    '''
        Function: setup_status_title(x, y)
    
        Does: Sets up the title "Status" for the game score tracker box

        Parameters:
            - x: a float, the X-coordinate for the text field
            - y: a float, the Y-coordinate for the test field

    '''
    status = turtle.Turtle()
    status.speed(0)
    status.penup()
    status.goto(x, y)
    status.color(Colors.primary)
    status.write("Status:", align='left', font=("Georgia", 12, "bold"))
    status.hideturtle()

def background():
    '''
        Function: background()

        Does: Sets up and displays the shape for the background, which
        contains the 4 boxes used on the screen
    
    '''
    screen = turtle.Screen()
    screen.register_shape("board_background.gif")
    background = turtle.Turtle()
    background.shape("board_background.gif")
    background.setpos(0, 0)
    turtle.hideturtle()

def create_status_tracker_obj():
    '''
        Function: create_status_tracker_obj()

        Does: Creates the Turtle object for the game status tracker

        Returns: 
            - status_tracker: a Turtle object, for the data for the 
            status tracker

    '''

    status_tracker = turtle.Turtle()
    status_tracker.hideturtle()
    status_tracker.speed(0)
    return status_tracker

def create_leaderboard_obj():
    '''
        Function: create_leaderboard_obj()

        Does: Creates the Turtle object for displaying the game leaderboard

        Returns: 
            - leaderboard_turtle: a Turtle object, for the data for the 
            leaderboard

    '''
    leaderboard_turtle = turtle.Turtle()
    leaderboard_turtle.hideturtle()
    leaderboard_turtle.speed(0)
    return leaderboard_turtle

def display_leaderboard(dic, leaderboard_turtle):
    '''
        Function: display_leaderboard(dic, leaderboard_turtle)

        Does: Displays the parts of the leaderboard on the screen

        Parameters:
            - dic: a dictionary, the dictionary to use for the leaderboard
            - leaderboard_turtle: the Turtle object for displaying the 
            leaderboard 
    
    '''
    N = 7
    i = 0
    # sort the dictionary values from lowest to highest, only including
    # the top 7 key value pairs
    sorted_dict = dict(sorted(dic.items(), 
                              key=lambda item: item[1], reverse= False)[:N])
    # clear the old leaderboard for refresh
    leaderboard_turtle.clear()
    for key, value in sorted_dict.items():
        player = f"{key} : {value}"
        leaderboard_turtle.penup()
        # obtain the x and y values from the player_pos list
        leaderboard_turtle.goto(player_pos[i][0], player_pos[i][1])
        leaderboard_turtle.color(Colors.off_black)
        leaderboard_turtle.write(player, align='left', font=(
            "Trebuchet MS", 12, "normal"))        
        leaderboard_turtle.hideturtle()
        i += 1

def display_game_status(status_tracker, attempts, matches):
    '''
        Function: display_game_status(status_tracker, attempts, matches)

        Does: Displays the parts of the game status tracker on the screen
        The pluralization of the words "move" and "match" properly handled 
        to ensure they remain singular when needed

        Parameters:
            - status_tracker: a Turtle object
            - attempts: an integer, the number of attempts the player has made
            - matches: an integer, the number of matches the player has found
    
    '''
    # clear the old status_tracker for refresh
    status_tracker.clear()
    status_tracker.penup()
    status_tracker.goto(-350, -343)
    status_tracker.color(Colors.off_black)
    # correctly pluralize move and match only when necessary
    if attempts == 1 and matches == 1:
        status_tracker.write(
            f"{attempts} move  | {matches} match", 
            align='left', font=("Trebuchet MS", 12, "normal"))
    elif attempts == 1 and matches != 1:
        status_tracker.write(
            f"{attempts} move  | {matches} matches", 
            align='left', font=("Trebuchet MS", 12, "normal"))
    elif attempts != 1 and matches == 1:
        status_tracker.write(
            f"{attempts} moves | {matches} match  ", 
            align='left', font=("Trebuchet MS", 12, "normal"))
    else:
        status_tracker.write(
            f"{attempts} moves | {matches} matches", 
            align='left', font=("Trebuchet MS", 12, "normal"))

    status_tracker.hideturtle()

def create_win_msg():
    '''
        Function: create_win_msg()

        Does: Creates the Turtle object for displaying the win message

        Returns: 
            - win_msg: a Turtle object, for the win message when the user 
            wins the game

    '''
    win_msg = turtle.Turtle()
    win_msg.hideturtle()
    win_msg.speed(0)
    return win_msg

def create_enter_name_msg():
    '''
        Function: create_enter_name_msg()

        Does: Creates the Turtle object for displaying the enter name 
        message if the user doesn't enter a name when asked

        Returns: 
            - enter_name_msg: a Turtle object

    '''
    enter_name_msg = turtle.Turtle()
    enter_name_msg.hideturtle()
    enter_name_msg.speed(0)
    return enter_name_msg

def create_card_count_msg():
    '''
        Function: create_card_count_msg()

        Does: Creates the Turtle object for the displaying the error message 
        about an invalid value for number of cards

        Returns: 
            - card_count_msg: a Turtle object

    '''
    card_count_msg = turtle.Turtle()
    card_count_msg.hideturtle()
    card_count_msg.speed(0)
    return card_count_msg

def create_quit_msg():
    '''
        Function: create_quit_msg()

        Does: Creates the Turtle object for displaying the quit message
        when the user quits the game
        
        Returns: 
            - quit_msg: a Turtle object

    '''
    quit_msg = turtle.Turtle()
    quit_msg.hideturtle()
    quit_msg.speed(0)
    return quit_msg

def create_screen_blocker():
    '''
        Function: create_screen_blocker()

        Does: Creates the Turtle object for the screen blocker
        The screen blocker is a transparent image that is displayed to 
        prevent objects from being clicked during screen pauses

        Returns: 
            - card_count_msg: a Turtle object

    '''
    screen_blocker = turtle.Turtle()
    screen_blocker.hideturtle()
    screen_blocker.speed(0)
    return screen_blocker

def create_credits_screen():
    '''
        Function: create_credits_screen()

        Does: Creates the Turtle object for the credits screen
        The credits screen is displayed after the user quits the game

        Returns: 
            - credits: a Turtle object

    '''
    credits = turtle.Turtle()
    credits.hideturtle()
    credits.speed(0)
    return credits

def create_cards_loaded_msg():

    '''
        Function: create_cards_loaded_msg()

        Does: Creates the Turtle object for the cards loaded message.
        This message is displayed when new cards are loaded after 
        "Reload Cards" is clicked

        Returns: 
            - cards_loaded_msg: a Turtle object

    '''
    cards_loaded_msg = turtle.Turtle()
    cards_loaded_msg.hideturtle()
    cards_loaded_msg.speed(0)
    return cards_loaded_msg

def create_config_not_found_msg():
    '''
        Function: create_config_not_found_msg()

        Does: creates the config_not_found_msg turtle object.
        This message is displayed when the config file entered during
        "Reload Cards" cannot be found

        Returns: 
            - config_not_found_msg: a Turtle object
    '''
    config_not_found_msg = turtle.Turtle()
    config_not_found_msg.hideturtle()
    config_not_found_msg.speed(0)
    return config_not_found_msg

def create_dir_not_found_msg():
    '''
        Function: create_dir_not_found_msg()

        Does: creates the dir_not_found_msg turtle object.
        This message is displayed when the config.cfg file
        targets a folder name that does not exist

        Returns: 
            - dir_not_found_msg: a Turtle object
    '''
    dir_not_found_msg = turtle.Turtle()
    dir_not_found_msg.hideturtle()
    dir_not_found_msg.speed(0)
    return dir_not_found_msg

def create_cover():
    '''
        Function: create_cover()

        Does: creates the screen_cover turtle object. 
        screen_cover is used to block the screen at the beginning
        during one of the warning messages

        Returns: 
            - screen_cover: a turtle object
    '''
    screen_cover = turtle.Turtle()
    screen_cover.hideturtle()
    screen_cover.speed(0)
    return screen_cover

# Tracer and update functions

def set_tracer(tracer):
    '''
        Function: set_tracer(tracer)

        Does: turns tracer on or off. Purpose is to lower the use of turtle 
        commands external to this file as much as possible.
            - True: Turns tracer on
            - False: Turns tracer off

        Parameters:
            - tracer: a boolean, True or False, whether to turn
            tracer on or off
    '''
    screen = turtle.Screen()
    if tracer == True:
        screen.tracer(1)
    else: 
        screen.tracer(0)

def update_screen():
    '''
        Function: update_screen()

        Does: Calls the Turtle screen to update
        Function was created to lower the number of Turtle commands used 
        outside this file
        
    '''

    screen = turtle.Screen()
    screen.update()
