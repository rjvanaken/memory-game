'''
    Memory game card class
'''

import turtle
import os
class Card:
    '''
    docString
    '''

    
    def __init__(self, index, x, y, image_id, game_handler):
        '''Constructor for the Card.'''

        self.index = index
        self.image_id = image_id
        self.isRevealed = False
        self.game_handler = game_handler

        screen = turtle.Screen()

        # register front back shape
        card_dir = self.game_handler.set_card_path()
        os.chdir(card_dir)
        screen.register_shape(image_id)
        self.card_front = turtle.Turtle()
        self.card_front.penup()
        self.card_front.shape(image_id)
        self.card_front.setpos(x, y)

        # register card back shape
        os.chdir('..')
        screen.register_shape("card_back.gif")
        self.card_back = turtle.Turtle()
        self.card_back.penup()
        self.card_back.shape("card_back.gif")
        self.card_back.setpos(x, y)

        # click handler
        self.card_back.onclick(lambda x, y: self.flip_card(x, y))
        

    def flip_card(self, x, y):
        if not self.isRevealed:
            self.card_back.hideturtle()
            self.isRevealed = True
            image_id = self.image_id
            self.game_handler.card_was_flipped(image_id)

            
    def remove_card(self):
        self.card_back.hideturtle()
        self.card_front.hideturtle()

    def reset_card(self):
        self.card_back.showturtle()
        self.isRevealed = False








        


    
