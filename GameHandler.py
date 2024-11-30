import turtle_helper
# from Card import Card
from data import positions
import random

class GameHandler:
    '''A class for handling the game behavior'''

    def __init__(self):
        '''Constructor for the GameHandler'''

        self.user = self.create_user()
        self.card_count = self.set_card_count()
        self.num_flipped = 0
        self.card_1_id = None
        self.card_2_id =  None
        self.cards = []
        self.compare_list = []
        self.match_count = 0
        self.attempts = 0

    def create_user(self):
        user = turtle_helper.setup_user()
        while user == '':
            turtle_helper.setup_user()
        return user

    def set_card_count(self):
        count_options = [8, 10, 12]
        # Add try and except for input
        # Add screen messages for error
        card_count = int(turtle_helper.setup_card_count())
        while card_count not in count_options:
            print (f'Must enter 8, 10, or 12. Entered: {card_count}')
            card_count = turtle_helper.setup_card_count()
        return card_count

    def shuffle_cards(self, card_count):
        img_ids = []
        with open('img_ids.txt', 'r') as f:
            _list = f.readlines()
            for item in range(0, card_count):
                id = _list[item].strip('\n')
                img_ids.append(id)
        random.shuffle(img_ids)
        return img_ids

    def card_was_flipped(self, image_id):
        self.num_flipped += 1
        
        print(f'flipped: {self.num_flipped} times')
        if self.num_flipped == 1:
            card_1_id = image_id
            self.update_compare_list(card_1_id)
            print(self.compare_list)
        elif self.num_flipped == 2:
            self.attempts += 1
            print(f'attempts: {self.attempts}')
            card_2_id = image_id
            self.update_compare_list(card_2_id)
            self.compare_cards(self.compare_list)
            print(self.compare_list)
            self.reset_values()
        else:
            return ValueError # temp
            
            
    def update_compare_list(self, image_id):
        self.compare_list.append(image_id)
        return self.compare_list


    def compare_cards(self, compare_list):
        if self.compare_list[0] == compare_list[1]:
            self.remove_or_reset(compare_list, self.cards, True)
            self.match_count += 1
        else:
            self.remove_or_reset(compare_list, self.cards, False)


    def remove_or_reset(self, compare_list, cards, isMatch):
        turtle_helper.set_tracer(False)
        for item in cards:
            if item.image_id in compare_list:
                if isMatch:
                    item.remove_card()
                else:
                    item.reset_card()
        turtle_helper.screen_delay()
        turtle_helper.update_screen()
        turtle_helper.set_tracer(True)

    def reset_values(self):
        self.num_flipped = 0
        self.card_1_id = None
        self.card_2_id =  None
        self.compare_list = []

            

        


                
            
    




