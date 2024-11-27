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

    
    def __init__(self, index, x, y):
        '''Constructor for the Card.'''

        self.index = index
        self.isRevealed = False
        self.isFound = False

        screen = turtle.Screen()

        # temporary - register front card temp
        screen.register_shape("default.gif")
        self.card_front = turtle.Turtle()
        self.card_front.penup()
        self.card_front.shape("default.gif")
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
            






    # def set_image_id(self, index, isRevealed):
    #     if isRevealed is False:
    #         image_id = 'background.png'
    #         return image_id
    #     else:
    #         image_id = self.get_image_id(self, index)

    # def get_image_id(self, index):
    #     with open ('img_ids.txt', 'r') as f:
    #         ids = f.readlines()
    #         for item in range(len(ids)):
    #             ids[item].strip()
    #         image_id = ids[index] 
    #     return image_id
        



    # def get_card_index(self, index):
        


# maybe pull the image ID from the shuffled list. Pass in a parameter, like the given index, and get the id so it can be referenced in comparison with the other one opened

    
