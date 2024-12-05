import turtle
import turtle_helper
import game_helpers
import configparser
import os
from GameHandler import GameHandler
class Button:
    '''Class to handle the behavior of the 2 custom buttons for quitting and loading cards'''

    def __init__(self, button, x, y, handler) -> None:
        '''Constructor for the button class'''

        self.x = x
        self.y = y
        self.button = button
        self.handler = handler

        if self.button == 'quit':
            screen = turtle.Screen()
            # register quit button
            screen.register_shape('quit_button.gif')
            self.quit_button = turtle.Turtle()
            self.quit_button.penup()
            self.quit_button.shape('quit_button.gif')
            self.quit_button.setpos(x, y)

            self.quit_button.onrelease(lambda x, y: self.quit_game(x, y))

        if self.button == 'load':
            screen = turtle.Screen()
            # register quit button
            screen.register_shape('load_button.gif')
            self.quit_button = turtle.Turtle()
            self.quit_button.penup()
            self.quit_button.shape('load_button.gif')
            self.quit_button.setpos(x, y)
            self.quit_button.onrelease(lambda x, y: self.load_cards(x, y))


    def quit_game(self, x, y):
        self.handler.display_quit_message()
        turtle.bye()


    def load_cards(self, x, y):
        config_file = turtle_helper.setup_config_file()
        turtle_helper.set_tracer(False)
        self.handler.clear_cards()
        self.handler.cards = game_helpers.create_cards(self.handler.card_count, self.handler, config_file)
        self.handler.reset_values()
        self.handler.reset_game_progress()
        turtle_helper.update_screen()
        turtle_helper.set_tracer(True)

