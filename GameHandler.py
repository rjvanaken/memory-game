import turtle_helper
import json
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
        self.load_leaderboard()
        turtle_helper.display_leaderboard(self.leaderboard)


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
        if card_count not in count_options:
            print (f'Invalid entry. Using default value of 12')
            card_count = 12
        return card_count
    

    def shuffle_cards(self, card_count):
        img_ids = []
        # add try and except for opening file
        with open('img_ids.txt', 'r') as f:
            _list = f.readlines()
            for item in range(0, card_count):
                id = _list[item].strip('\n')
                img_ids.append(id)
        random.shuffle(img_ids)
        return img_ids

    def load_leaderboard(self):
        try: 
            with open(f"leaderboard_{self.card_count}.json", "r") as f:
                self.leaderboard = json.load(f)
        except FileNotFoundError:
            self.leaderboard = dict()             

    def card_was_flipped(self, image_id):
        self.num_flipped += 1
        if self.num_flipped == 1:
            card_1_id = image_id
            self.update_compare_list(card_1_id)
        elif self.num_flipped == 2:
            self.attempts += 1
            card_2_id = image_id
            self.update_compare_list(card_2_id)
            self.compare_cards(self.compare_list)
            self.reset_values()
            
            
    def update_compare_list(self, image_id):
        self.compare_list.append(image_id)
        return self.compare_list


    def compare_cards(self, compare_list):
        if compare_list[0] == compare_list[1]:
            self.remove_or_reset(compare_list, self.cards, True)
            self.match_count += 1
            self.check_cards(self.card_count, self.match_count)
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

    def check_cards(self, card_count, match_count):
        if match_count == card_count / 2:
            turtle_helper.display_win_message()
            self.save_score_and_update_leaderboard()


    def save_score_and_update_leaderboard(self):
        turtle_helper.set_tracer(0)
        self.leaderboard[self.user.title()] = self.attempts
        with open(f"leaderboard_{self.card_count}.json", "w") as f:
            json.dump(self.leaderboard, f)
        self.load_leaderboard()
        turtle_helper.display_leaderboard(self.leaderboard)
        turtle_helper.update_screen()
        turtle_helper.set_tracer(0)
        


        


                
            
    




