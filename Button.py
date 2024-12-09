'''
    Rebecca Van Aken
    CS 5001, Fall, 2024
    Final Project
'''

import turtle
import turtle_helper
import game_helpers

class Button:
    '''
        Class to handle the display and behavior of the 2 custom buttons 
        for quitting and loading cards
        
        Attributes:
            - x: a float, the X-coordinate of the button
            - y: a float, the Y-coordinate of the button
            - button: a string, the specific button
            - handler: the GameHandler instance
            - quit_button: a Turtle object for the "Quit Game" button
            - load_button: a Turtle object for the "Reload Cards" button
        
        Methods:
            - __init__(self, button, x, y, handler): Constructor for the Button class
            - quit_game(): Handles the logic for quitting the game
            - load_cards(): Handles the logic for reloading cards
    
    '''

    def __init__(self, button, x, y, handler):
        '''
            Constructor for the button class

            Creates a new Button object with the specified properties and 
            initializes its visual representation

            Arguments:
                - button: a string, the specific button ('quit' or 'load')
                - x: a float, X-coordinate of the button
                - y: a float, Y-coordinate of the button
                - handler: a reference to the GameHandler instance 
                managing the game

            Attributes:
                - x: a float, the X-coordinate of the button
                - y: a float, the Y-coordinate of the button
                - button: a string, the specific button
                - handler: the GameHandler instance
                - quit_button: a Turtle object for the "Quit Game" button
                - load_button: a Turtle object for the "Reload Cards" button

            Does:
                - Initializes the Button object with attributes and sets up 
                the initial button state
                - Creates and positions the appropriate button (quit or load) 
                on the screen
                - Configures the button's click handler
        
        '''

        self.x = x
        self.y = y
        self.button = button
        self.handler = handler

        # if the button is the "Quit Game" button:
        if self.button == 'quit':
            screen = turtle.Screen()
            # register the button shape
            screen.register_shape('quit_button.gif')
            self.quit_button = turtle.Turtle()
            self.quit_button.penup()
            self.quit_button.shape('quit_button.gif')
            self.quit_button.setpos(x, y)
            # on release of the button, execute quit_game
            self.quit_button.onrelease(lambda x, y: self.quit_game(x, y))
        # if the button is the "Reload Cards" button:
        if self.button == 'load':
            screen = turtle.Screen()
            # register the button shape
            screen.register_shape('load_button.gif')
            self.load_button = turtle.Turtle()
            self.load_button.penup()
            self.load_button.shape('load_button.gif')
            self.load_button.setpos(x, y)
            # on release of the button, execute load_cards
            self.load_button.onrelease(lambda x, y: self.load_cards(x, y))


    def quit_game(self, x, y):
        '''
            Method: quit_game(self, x, y)

            Does: Closes the program. Called when the "Quit Game" button is 
            clicked

            Parameters:
                - x: the X-coordinate of the "Quit Game" button
                - y: the Y-coordinate of the "Quit Game" button 

        '''
        # display the message telling the user they chose to quit
        self.handler.display_quit_msg()
        self.handler.display_credits_screen()
        turtle.bye()


    def load_cards(self, x, y):
        '''
            Method: load_cards(self, x, y)

            Does: Reloads the cards based on the config file and resets the 
            game values. Called when the "Reload Cards" button is clicked

            Parameters:
                - x: the X-coordinate of the "Reload Cards" button
                - y: the Y-coordinate of the "Reload Cards" button 

        '''
        # Ask the user for the name of the configuration file
        config_file = turtle_helper.setup_config_file()
        turtle_helper.set_tracer(False)
        # clear the old cards from the screen
        self.handler.clear_cards()
        card_dir = self.handler.set_card_path(config_file)
        # regenerate the cards based on the entered config file
        self.handler.cards = game_helpers.create_cards(self.handler.card_count, self.handler, config_file, card_dir)
        # reset any recorded values and the game progress
        self.handler.reset_values()
        self.handler.reset_game_progress()
        turtle_helper.update_screen()
        self.handler.display_cards_loaded_msg()
        turtle_helper.set_tracer(True)

