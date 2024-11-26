'''
    Memory game card class
'''

import random
import turtle
import turtle_helper
from data import positions

class Card:
    '''
    
    
    '''
    '''
    NOTES:
    Memory game card piece:
        - Established through turtle shape "memory-card-class.gif"
        - Position values also passed through (x, y)
        - Boolean to determine which side shows:
            - True: Image shows
            - False: Back shows
        - Each instance assigned a random number (1-16) upon hitting play again or reset
            - Each number, from 1-16, matches with one of the 8 different card images
                - Dictionary will hold matched values
        - When a card is clicked, i += 1
            - Once i == 2, if image IDs do not match, reset i to 0 and flip the last 2 flipped images back over (leaving any matched untouched)
        - "Flip" animation to flip the card over when clicked
            - When clicked, image will change size, "anchor point" center, to 0%, 100%, then to -100%, 100% and bool is changed
            
        '''
    # GREG:
    # list of image names (16)
    # take it from list and apply it
    # does a imgid = b imgid
        # only operating on data within the class is cleaner
    
    def __init__(self, index, x, y):
        '''Constructor for the Card.
        state boolean and imageID passed through'''
        self.index = index
        self.x = x
        self.y = y
        screen = turtle.Screen()
        screen.register_shape("memory_card_class.gif")
        self.card = turtle.Turtle()
        self.card.shape("memory_card_class.gif")
        self.card.speed(0)
        self.card.penup()
        self.card.setpos(x, y)
        # self.isRevealed = isRevealed


        # Register shape and create card background turtle
        
                                # # Register shape and create the card front turtle
                                # screen = turtle.Screen()
                                # screen.register_shape("default.gif")
                                # self.card_front = turtle.Turtle()
                                # self.card_front.shape("default.gif")
        
                                # # click handler
                                # if self.isRevealed is False:
                                #     self.card.onclick(self.reveal_card)
                                #     self.isRevealed = True
                                #     # TODO: Add something that will prevent it from doing this again after clicking when it's already flipped over
                                # else:
                                #     self.card_front.onclick(self.hide_card)
                                #     self.isRevealed = False
    
        # hide turtle object
        self.card.hideturtle()





    def get_x_pos(self, index):
        x_position = positions[index][0]
        return x_position
    

    def get_y_pos(self, index):
        y_position = positions[index][1]
        return y_position
        



    def set_image_id(self, index, isRevealed):
        if isRevealed is False:
            image_id = 'background.png'
            return image_id
        else:
            image_id = self.get_image_id(self, index)

    def get_image_id(self, index):
        with open ('img_ids.txt', 'r') as f:
            ids = f.readlines()
            for item in range(len(ids)):
                ids[item].strip()
            image_id = ids[index] 
        return image_id
        
    def reveal_card(self):
        pass
        # turtle.tracer(0)
        # # self.card.speed(3)
        # self.card.shapesize(0, 0)
        # # self.card.speed(0)
        # self.card_front.shapesize(1, 1)
        # turtle.update()

    def hide_card(self):
        image_id = 'background.png'



    # def get_card_index(self, index):
        


# maybe pull the image ID from the shuffled list. Pass in a parameter, like the given index, and get the id so it can be referenced in comparison with the other one opened

    
