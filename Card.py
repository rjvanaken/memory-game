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

    
    def __init__(self, index, x, y, isRevealed=False):
        '''Constructor for the Card.
        state boolean and imageID passed through'''
        self.index = index
        screen = turtle.Screen()
        screen.register_shape("memory_card_class.gif")
        self.card = turtle.Turtle()
        self.card.penup()
        self.card.goto(x, y)
        self.card.shape("memory_card_class.gif")
        self.card.setpos(x, y)
        self.card.speed(0)
        self.isRevealed = isRevealed


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

    def hide_card(self):
        image_id = 'background.png'



    # def get_card_index(self, index):
        


# maybe pull the image ID from the shuffled list. Pass in a parameter, like the given index, and get the id so it can be referenced in comparison with the other one opened

    
