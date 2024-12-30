'''
    Rebecca Van Aken
    CS 5001, Fall, 2024
    Final Project

    This file contains the GameHandler class, created to handle the behavior
    of the memory game

'''

import turtle_helper
import turtle
import json
import sys
import random
import os
import time
import game_helpers
import configparser

class GameHandler:
    '''
        A class for handling the game behavior

        Attributes:
            - screen_blocker: screen blocker turtle object
            - screen_cover: screen cover turtle object
            - user: a string, the player's name
            - card_count: an integer, the number of cards to play with
            - num_flipped: an integer, the number of cards flipped in 
            the current round
            - card_1_id: a string, the image_id of the first flipped card
            - card_2_id: a string, the image_id of the second flipped card
            - cards: a list of the Card objects displayed on the game board 
            - compare_list: a list of image_ids for comparison
            - match_count: an integer, the number of matches found
            - attempts: an integer, the number of guesses the player has made
            - leaderboard_turtle: a Turtle object for displaying the 
            leaderboard
            - status_tracker: a Turtle object for displaying the game score 

        Methods:
            - __init__(): Constructor for the GameHandler
            - create_user(): Asks for the player's name
            - set_card_count(): Sets the number of cards to play with
            - shuffle_cards(card_count, card_dir): Shuffles the card image IDs
            - clear_cards(): Removes all cards from the screen
            - set_default_card_dir(cwd): Sets the default card directory
            - set_card_path(config_file): Sets the path for custom card images
            - load_leaderboard(): Loads the existing leaderboard
            - card_was_flipped(image_id): Handles card flipping logic
            - update_compare_list(image_id): Updates the comparison list
            - compare_cards(compare_list): Compares IDs for the flipped cards
            - remove_or_reset(compare_list, cards, isMatch): Resets or removes
                cards
            - reset_values(): Resets values between attempts
            - reset_game_progress(): Resets game progress
            - check_cards(card_count, match_count): Checks for game completion
            - save_score_and_update_leaderboard(): Updates the leaderboard
            - update_game_status(): Updates the displayed game score
            - display_win_msg(): Displays the win message
            - display_card_count_msg(): Displays card count message
            - display_cards_loaded_msg(): Displays cards loaded message
            - display_enter_name_msg(): Displays enter name message
            - display_config_not_found_msg(): Displays config not found message
            - display_dir_not_found_msg(): Displays directory not found message
            - display_quit_msg(): Displays quit message
            - display_credits_screen(): Displays credits screen
            - show_cover(): Displays screen cover
            - hide_cover(): Hides screen cover
            - display_screen_blocker(): Displays screen blocker
            - hide_screen_blocker(): Hides screen blocker
            - screen_delay(seconds): Pauses the game for a specified time
    
    '''

    def __init__(self):
        '''
            Constructor for the GameHandler
        
            Initializes the GameHandler object with necessary attributes and 
            sets up the initial game state.
        
            Attributes:
                - screen_blocker: screen blocker turtle object
                - screen_cover: screen cover turtle object
                - user: a string, the player's name
                - card_count: an integer, the number of cards to play with
                - num_flipped: an integer, the number of cards flipped in 
                the current round
                - card_1_id: a string, the image_id of the first flipped card
                - card_2_id: a string, the image_id of the second flipped card
                - cards: a list of the Card objects displayed on the game board 
                - compare_list: a list of image_ids for comparison
                - match_count: an integer, the number of matches found
                - attempts: an integer, the number of guesses the player has made
                - leaderboard_turtle: a Turtle object for displaying the 
                leaderboard
                - status_tracker: a Turtle object for displaying the game score 
        
            Does: Sets up the initial game state by:
                - creating necessary turtle objects, 
                - initializing attributes
                - displaying the leaderboard and game score.
                
        '''
        
        self.screen_blocker = turtle_helper.create_screen_blocker()
        self.screen_cover = turtle_helper.create_cover()
        # set the user's name and get the number of cards to play with
        self.user = self.create_user()
        self.card_count = self.set_card_count()
        self.num_flipped = 0
        self.card_1_id = None
        self.card_2_id = None
        self.cards = []
        self.compare_list = []
        self.match_count = 0
        self.attempts = 0
        # create the leaderboard and score tracker objects
        self.leaderboard_turtle = turtle_helper.create_leaderboard_obj()
        self.status_tracker = turtle_helper.create_status_tracker_obj()
        # display the background, set up the leaderboard and 
        # game score tracker
        turtle_helper.background()
        self.load_leaderboard()
        turtle_helper.setup_status_title(-420, -340)
        turtle_helper.display_leaderboard(
            self.leaderboard, self.leaderboard_turtle)
        turtle_helper.display_game_status(
            self.status_tracker, self.attempts, self.match_count)


    def create_user(self):
        '''
            Method: create_user(self):
            
            Does: Asks the player to enter their name for use in the
            leaderboard later on

            Returns: 
            - user: a string, the name of the player

        '''
        user = turtle_helper.setup_user()
        while user == '' or user == None:
            self.display_enter_name_msg()
            user = turtle_helper.setup_user()
        return user

    def set_card_count(self):
        '''
            Method: set_card_count(self)

            Does: asks how many cards the user wants to play with

            Returns: 
                - card_count: an integer, the number of cards 
                the game should be played with
        
        '''
        count_options = ['8', '10', '12']
        card_count = '0'
        card_count = turtle_helper.setup_card_count()
        # if value entered is not part of the 3 options, display message
        # requesting the user enter one of the 3 options
        while card_count not in count_options:
            self.display_card_count_msg()
            card_count = turtle_helper.setup_card_count()
        # set the string from the input to an integer
        card_count = int(card_count)
        return card_count

    def shuffle_cards(self, card_count, card_dir):
        '''
            Method: shuffle_cards(self, card_count, card_dir)

            Does:
                - Reads the card image names from the folder and writes
                to a file
                - Puts the values in a list and shuffles the order

            Parameters:
                - card_count: an integer, the number of cards to play with
                - card_dir: a string, the path to the card images

            Returns:
                - img_ids: a list, the list of shuffled card image IDs
        
        '''
        game_helpers.get_card_image_names(card_dir, 'img_ids.txt')
        img_ids = []
        # open the 'img_ids.txt' file that contains the card image IDs
        try:
            with open('img_ids.txt', 'r') as f:
                _list = f.readlines()
                for item in range(0, card_count):
                    id = _list[item].strip('\n')
                    img_ids.append(id)
            # shuffle the order of the items in the list
            random.shuffle(img_ids)
            return img_ids
        except FileNotFoundError:
            return "Image IDs file could not be found"
    
    def clear_cards(self):
        '''
            Method: clear_cards(self)

            Does: removes all of the cards from the screen
        
        '''
        # remove all of the cards from the screen and clear the list
        for card in self.cards:
            card.remove_card()
        self.cards = []

    def set_default_card_dir(self, cwd):
        '''
            Method: set_default_card_dir(self, cwd)

            Does: Sets the path of the default list of cards for whenever
            there's an issue loading a new deck of cards
            
            Parameters:
                - cwd: a string, the current working directory

            Returns:
                - card_front_path: a string, the path to the card folder
        
        '''
        card_front_path = os.path.join(cwd, 'boston_places')
        return card_front_path
        
    def set_card_path(self, config_file):
        '''
            Method: set_card_path(self, config_file)

            Does: Sets the path of the folder containing the images based
            on the folder name specified in the config_file. If folders
            or files cannot be found, loads the default folder instead
            
            Parameters:
                - config_file: a string, the name of the configuration file
                containing the folder name

            Returns:
                - card_front_path: a string, the path to the folder containing
                the images to play with
        
        '''
        # marks the cwd as having not been set yet
        cwd_set = False
        # if the config_file can be found, parse it and get current working
        # directory
        if os.path.exists(config_file):
            config = configparser.ConfigParser()
            config.read(config_file)
            cwd = os.getcwd()
            cwd_set = True
            # obtain the value from config_file and create the card path
            card_front_dir = config.get(
                'card_customization', 'card_front_dir')
            card_front_path = os.path.join(cwd, card_front_dir)
            # if the path exists, return the path
            if os.path.exists(card_front_path):
                return card_front_path
            else:
                # if current working directory was never set, get current
                # working directory
                if cwd_set == False:
                    cwd = os.getcwd()
                # set card path to the default value and show message
                # telling the user that specified directory cannot be found
                card_front_path = self.set_default_card_dir(cwd)
                self.show_cover()
                self.display_dir_not_found_msg()
                self.hide_cover()
                return card_front_path
        else:
            # if config_file path doesn't exist...
            # if cwd was never acquired, get working directory
            if cwd_set == False:
                cwd = os.getcwd()
            # set card directory to default folder and show message telling
            # the user the config file cannot be found
            card_front_path = self.set_default_card_dir(cwd)
            self.display_config_not_found_msg()
            return card_front_path
            


    def load_leaderboard(self):
        '''
            Method: load_leaderboard(self)

            Does: Loads the existing leaderboard from the leaderboard json
            file as a dictionary. If the json file doesn't exist 
            yet, an empty dictionary is created
        
        '''
        try: 
            with open(f"leaderboard_{self.card_count}.json", "r") as f:
                self.leaderboard = json.load(f)
        except FileNotFoundError:
            # create an empty dictionary if the leaderboard does not yet exist
            self.leaderboard = dict()             

    def card_was_flipped(self, image_id):
        '''
            Method: card_was_flipped(self, image_id)

            Does: Handles the logic after the card is flipped by doing 
            the following:
                - Increasing the flipped value and adding the flipped image_id
                to a list.
                - Once the flipped value is 2, it triggers the function to 
                compare the image IDs in the compare list
                - Resets the values that don't retain between rounds
            
            Parameters:
                - image_id: a string, the name of the image that was flipped
        
        '''
        self.display_screen_blocker()
        # update the flipped value
        self.num_flipped += 1
        if self.num_flipped == 1:
            card_1_id = image_id
            # modify the compare_list with the image_id
            self.update_compare_list(card_1_id)
        # if the flipped value is 2, call the compare function to compare
        # the image_ids in the compare_list
        elif self.num_flipped == 2:
            self.attempts += 1
            card_2_id = image_id
            self.screen_delay(0.75)
            self.update_compare_list(card_2_id)
            self.compare_cards(self.compare_list)
            # reset the values that should be reset after each "attempt"
            self.reset_values()
        self.hide_screen_blocker()
            
            
    def update_compare_list(self, image_id):
        '''
            Method: update_compare_list(self, image_id)

            Does: Appends the list with the image_id of the card
            that was just flipped over
            
            Parameters:
                - image_id: a string, the name of the image that was flipped

            Returns:
                - compare_list: a list, containing the image_id's of the
                cards that were flipped over
        
        '''
        self.compare_list.append(image_id)
        return self.compare_list


    def compare_cards(self, compare_list):
        '''
            Method: compare_cards(self, compare_list)

            Does: Compares the two image_ids in the compare_list to see if
            they are a match. The game status is updated, and if the cards
            are a match, they're removed from the screen. If they're not
            a match, they are flipped back over
            
            Parameters:
                - compare_list: a list, containing the image_id's of the
                cards that were flipped over
        
        '''
        # if the items in the compare_list match, remove the cards and update
        # the game status
        if compare_list[0] == compare_list[1]:
            self.remove_or_reset(compare_list, self.cards, True)
            self.match_count += 1
            self.update_game_status()
            self.check_cards(self.card_count, self.match_count)
        # if not a match, update the game status and reset the cards
        else:
            self.update_game_status()
            self.remove_or_reset(compare_list, self.cards, False)


    def remove_or_reset(self, compare_list, cards, isMatch):
        '''
            Method: remove_or_reset(self, compare_list, cards, isMatch)

            Does: If the image_ids were in the compare_list, remove the cards
            if they are a match. If not, flip them back over
            
            Parameters:
                - compare_list: a list, containing the image_id's of the
                cards that were flipped over
                - cards: a list, the list of image IDs representing the cards
                on the screen
                - isMatch: a boolean, whether or not the image_ids are a match
        
        '''
        turtle_helper.set_tracer(False)
        # for all the cards in the cards list, reset or remove them if they
        # were flipped over
        for item in cards:
            if item.image_id in compare_list:
                # if isMatch is set tp true, remove the card
                if isMatch:
                    item.remove_card()
                # is isMatch is false, reset the cards
                else:
                    item.reset_card()
        self.screen_delay(0.25)
        turtle_helper.update_screen()
        turtle_helper.set_tracer(True)

    def reset_values(self):
        '''
            Method: reset_values(self)

            Does: Resets the following values. For use in between "attempts":
                - sets flipped value to 0
                - sets the card ids for comparison to None
                - clears the compare_list
        
        '''
        self.num_flipped = 0
        self.card_1_id = None
        self.card_2_id =  None
        self.compare_list = []

    def reset_game_progress(self):
        '''
            Method: reset_game_progress(self)

            Does: resets the following values:
                - sets match_count to 0
                - sets attmepts to 0
        
        '''
        self.match_count = 0
        self.attempts = 0
        self.update_game_status()

    def check_cards(self, card_count, match_count):
        '''
            Method: check_cards(self, card_count, match_count)

            Does: checks whether or not all the cards are flipped over
            If they are, displays the win message and updates the 
            leaderboard
            
            Parameters:
                - card_count: an integer, the number of cards to play with
                - match_count: an integer, the number of matches the player
                has found
        
        '''
        # if all the cards have been matched, display win message and update
        # leaderboard
        if match_count == card_count / 2:
            self.save_score_and_update_leaderboard()
            self.display_win_msg()
            # after winning, quit the program
            self.display_credits_screen()


    def save_score_and_update_leaderboard(self):
        '''
            Method: save_score_and_update_leaderboard

            Does: Saves the score to the leaderboard, updates the json file,
            and updates the displayed leaderboard on the screen. If the user
            has a previous score in the leaderboard and it's better than the
            new score, nothing is updated
        
        '''
        turtle_helper.set_tracer(0)
        # if the user is not in the leaderboard, save the score
        if self.user.title() not in self.leaderboard:
            self.leaderboard[self.user.title()] = self.attempts
        # if the user is in the leaderboard and the new score is better than
        # a past score, update the value
        elif self.leaderboard[self.user.title()] > self.attempts:
            self.leaderboard[self.user.title()] = self.attempts
        with open(f"leaderboard_{self.card_count}.json", "w") as f:
            json.dump(self.leaderboard, f)
        self.load_leaderboard()
        # re-display the updated leaderboard
        turtle_helper.display_leaderboard(
            self.leaderboard, self.leaderboard_turtle)
        turtle_helper.update_screen()

    def update_game_status(self):
        '''
            Method: update_game_status(self)

            Does: updates the displayed values for the user's game score
        
        '''
        turtle_helper.set_tracer(0)
        # re-create and display the game scores
        turtle_helper.display_game_status(
            self.status_tracker, self.attempts, self.match_count)
        turtle_helper.update_screen()
        turtle_helper.set_tracer(1)



    # Messages and extras

    def display_win_msg(self):
        '''
            Method: display_win_msg(self)

            Does: creates and displays the message on the screen when the
            user wins the game 
        
        '''
        # create the message object 
        win_msg = turtle_helper.create_win_msg()
        screen = turtle.Screen()
        # register and display the shape
        screen.register_shape('winner.gif')
        win_msg.penup()
        win_msg.shape('winner.gif')
        win_msg.showturtle()
        win_msg.setpos(0, 0)
        screen.update()
        # pause and display for 2 seconds before hiding
        self.screen_delay(2)
        win_msg.hideturtle()
        screen.update()
        
    def display_card_count_msg(self):
        '''
            Method: display_win_msg(self)

            Does: creates and displays the message that is used when the user 
            wins the game 
        
        '''
        # create the message object 
        card_count_msg = turtle_helper.create_card_count_msg() 
        screen = turtle.Screen()
        # register and display the shape
        screen.register_shape('card_count_msg.gif')
        card_count_msg.penup()
        card_count_msg.shape('card_count_msg.gif')
        card_count_msg.showturtle()
        card_count_msg.setpos(0, 0)
        screen.update()
        # pause and display for 1.5 seconds before hiding
        self.screen_delay(1.5)
        card_count_msg.hideturtle()
        screen.update()

    def display_cards_loaded_msg(self):
        '''
            Method: display_cards_loaded_msg(self)

            Does: creates the displays the message for informing
            the user that new cards were loaded upon clicking 
            "Reload Cards"
        
        '''
        # create the message object
        cards_loaded_msg = turtle_helper.create_cards_loaded_msg()
        screen = turtle.Screen()
        # register and display the shape
        screen.register_shape('cards_loaded_msg.gif')
        cards_loaded_msg.penup()
        cards_loaded_msg.shape('cards_loaded_msg.gif')
        cards_loaded_msg.showturtle()
        cards_loaded_msg.setpos(0, 0)
        screen.update()
        # pause and display for 1.5 seconds before hiding
        self.screen_delay(1.5)
        cards_loaded_msg.hideturtle()
        screen.update()

    def display_enter_name_msg(self):
        '''
            Method: display_enter_name_msg(self)

            Does: creates and displays the message for when the user
            does not enter a name when asked
        
        '''
        # create the message object
        enter_name_msg = turtle_helper.create_enter_name_msg()
        screen = turtle.Screen()
        # register and display the shape
        screen.register_shape('enter_name_msg.gif')
        enter_name_msg.penup()
        enter_name_msg.shape('enter_name_msg.gif')
        enter_name_msg.showturtle()
        enter_name_msg.setpos(0, 0)
        screen.update()
        # pause and display for 1.5 seconds before hiding
        self.screen_delay(1.5)
        enter_name_msg.hideturtle()
        screen.update()
    
    def display_config_not_found_msg(self):
        '''
            Method: display_config_not_found_msg(self)

            Does: creates and displays the message on the screen when the
            user wins the game 
        
        '''
        # create the message object
        config_not_found_msg = turtle_helper.create_config_not_found_msg()
        screen = turtle.Screen()
        # register and display the shape
        screen.register_shape('config_not_found.gif')
        config_not_found_msg.penup()
        config_not_found_msg.shape('config_not_found.gif')
        config_not_found_msg.showturtle()
        config_not_found_msg.setpos(0, 0)
        screen.update()
        # pause and display for 1.5 seconds before hiding
        self.screen_delay(1.5)
        config_not_found_msg.hideturtle()
        screen.update()

    def display_dir_not_found_msg(self):
        '''
            Method: display_dir_not_found_msg(self)

            Does: creates and displays the message used for when the
            specified image directory could not be found
        
        '''
        # create the message object
        dir_not_found_msg = turtle_helper.create_dir_not_found_msg()
        screen = turtle.Screen()
        # register and display the shape
        screen.register_shape('directory_not_found.gif')
        dir_not_found_msg.penup()
        dir_not_found_msg.shape('directory_not_found.gif')
        dir_not_found_msg.showturtle()
        dir_not_found_msg.setpos(0, 0)
        screen.update()
        # pause and display for 1.5 seconds before hiding
        self.screen_delay(1.5)
        dir_not_found_msg.hideturtle()
        screen.update()

    def display_quit_msg(self):
        '''
            Method: display_quit_msg(self)

            Does: creates and displays the message used for when the user
            quits the game
        
        '''
        # create the message object
        quit_msg = turtle_helper.create_quit_msg()
        screen = turtle.Screen()
        # register and display the shape
        screen.register_shape("quit_msg.gif")
        quit_msg.penup()
        quit_msg.shape('quit_msg.gif')
        quit_msg.showturtle()
        quit_msg.setpos(0, 0)
        screen.update()
        # pause and display for 2 seconds
        self.screen_delay(2)
        turtle_helper.set_tracer(1)

    def display_credits_screen(self):
        '''
            Method: display_credits_screen(self)

            Does: creates and displays the credits screen for after the
            user quits the game
        
        '''
        # create the message object
        credits = turtle_helper.create_credits_screen()
        screen = turtle.Screen()
        # register and display the shape
        screen.register_shape("credits.gif")
        credits.penup()
        credits.shape('credits.gif')
        credits.showturtle()
        credits.setpos(0, 0)
        screen.update()
        # pause and display for 3 seconds before closing program
        self.screen_delay(3)
        sys.exit(0)


    def show_cover(self):
        '''
            Method: show_cover(self)

            Does: displays the screen cover to block the screen 
            when messages are displayed in the beginning before
            the game board is loaded

        '''
        # create the message object
        self.screen_cover = turtle_helper.create_cover()
        screen = turtle.Screen()
        # register and display the shape
        screen.register_shape("cover.gif")
        self.screen_cover.penup()
        self.screen_cover.shape('cover.gif')
        self.screen_cover.showturtle()
        self.screen_cover.setpos(0, 0)
        screen.update()

    def hide_cover(self):
        '''
            Method: hide_cover(self)

            Does: hides the screen cover that blocks the rest of the screen
            when some messages are displayed

        '''
        
        # hide the screen cover turtle object
        self.screen_cover.hideturtle()

    def display_screen_blocker(self):
        '''
            Method: display_screen_blocker(self)

            Does: creates and displays the blocker to block anything
            from being clicked on

        '''
        screen = turtle.Screen()
        # create the message object
        self.screen_blocker = turtle_helper.create_screen_blocker()
        # register and display the shape
        screen.register_shape('screen_blocker.gif')
        self.screen_blocker.penup()
        self.screen_blocker.shape('screen_blocker.gif')
        self.screen_blocker.showturtle()
        self.screen_blocker.setpos(0, 0)
        screen.update()
        
    def hide_screen_blocker(self):
        '''
            Method: hide_screen_blocker(self)

            Does: hides the blocker that blocks anything
            from being clicked on

        '''
        screen = turtle.Screen()
        # hide the screen blocker turtle object
        self.screen_blocker.hideturtle()
        screen.update()       

    def screen_delay(self, seconds):
        '''
            Method: screen_delay(self, seconds)

            Does: shows the screen blocker and pauses anything from 
            happening on the screen for the specified number of seconds

            Parameters:
                - seconds: an integer, the number of seconds to use for
                time.sleep

        '''
        screen = turtle.Screen()
        # display the blocker on the screen to block anything from
        # being clicked
        self.display_screen_blocker
        # pause the screen
        time.sleep(seconds)
        # hide the blocker
        self.hide_screen_blocker
        screen.update()

                
            
    




