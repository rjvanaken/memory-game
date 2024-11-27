'''
    Memory game card class
'''

import random
import turtle
import turtle_helper

class Card:
    '''
    docString
    '''

    
    def __init__(self, index, x, y, image_id):
        '''Constructor for the Card.'''

        self.index = index
        self.image_id = image_id
        self.isRevealed = False
        self.isFound = False

        screen = turtle.Screen()

        # register front back shape
        screen.register_shape(image_id)
        self.card_front = turtle.Turtle()
        self.card_front.penup()
        self.card_front.shape(image_id)
        self.card_front.setpos(x, y)
        self.card_front.speed(0)

        # register card back shape
        screen.register_shape("card_back.gif")
        self.card_back = turtle.Turtle()
        self.card_back.penup()
        self.card_back.shape("card_back.gif")
        self.card_back.setpos(x, y)
        self.card_back.speed(0)




        # click handler
        self.card_back.onclick(lambda x, y: self.flip_card(x, y))

    def flip_card(self, x, y):
        if not self.isRevealed and not self.isFound:
            self.card_back.hideturtle()
            self.isRevealed = True
            



        


    
