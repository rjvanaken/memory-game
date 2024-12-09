'''
    Rebecca Van Aken
    CS 5001, Fall, 2024
    Final Project
    
    This file contains the Card class, created for the cards used for
    the memory game
    
'''

import turtle
import os
class Card:
    '''A class for the cards used in the memory game'''

    def __init__(
            self, index, x, y, image_id, game_handler, card_dir):
        '''
            Constructor for the Card class.

            Creates a new Card object with the specified properties and 
            initializes its visual representation.

            Arguments:
                - index: an integer, the index for the card.
                - x: a float, the X-coordinate for the card's screen position
                - y: a float, the Y-coordinate for the card's screen position
                - image_id: a string, the name of the image file to use for 
                the front of the card
                - game_handler: a reference to the GameHandler instance 
                managing the game.
                - card_dir: a string, the path to the folder containing the
                card images

            Attributes:
                - index: an integer, the index of the card.
                - image_id: a string, the image ID of the card.
                - isRevealed: A boolean, indicating whether the card is
                flipped over or not
                - game_handler: the GameHandler instance.
                - card_front: a Turtle object for the front of the card.
                - card_back: a Turtle object for the front of the card.

            Does:
                - Initializes the Card object with attributes and sets up 
                the initial card state
                - Registers the card's front and back images
                - Sets up the Card's position and click handler

        '''


        self.index = index
        self.image_id = image_id
        self.isRevealed = False
        self.game_handler = game_handler

        screen = turtle.Screen()
        #set directory of the images and register card front shape
        os.chdir(card_dir)
        screen.register_shape(image_id)
        self.card_front = turtle.Turtle()
        self.card_front.penup()
        self.card_front.shape(image_id)
        self.card_front.setpos(x, y)

        # go back to the root directory and register card back shape
        os.chdir('..')
        screen.register_shape("card_back.gif")
        self.card_back = turtle.Turtle()
        self.card_back.penup()
        self.card_back.shape("card_back.gif")
        self.card_back.setpos(x, y)

        # click handler
        self.card_back.onclick(lambda x, y: self.flip_card(x, y))
        

    def flip_card(self, x, y):
        '''
            Method: flip_card(self, x, y)

            Does: "flips" the card over when clicked, by hiding the card_back 
            image to reveal the front of the card. If the card is already 
            flipped over, nothing happens when clicked again.

            Parameters:
                - x: a float, the X-coordinate of the respective card
                - y: a float, the Y-coordinate of the respective card 
        
        '''
        # if the card has not been flipped over, hide card and initiate
        # card flipped logic
        if not self.isRevealed:
            self.card_back.hideturtle()
            # set it to be flipped over so it cannot be clicked again
            self.isRevealed = True
            self.game_handler.card_was_flipped(self.image_id)
    
            
    def remove_card(self):
        '''
            Method: remove_card(self)

            Does: removes both the card_back and the card_front from the 
            game board

        
        '''
        self.card_back.hideturtle()
        self.card_front.hideturtle()

    def reset_card(self):
    
        '''
            Method: reset_card(self)

            Does: "flips" the card back over by showing the card_back 
            again
        
        '''
        self.card_back.showturtle()
        self.isRevealed = False

    








        


    
