import turtle_helper
import turtle
import json
import random
import os
import time
import game_helpers
import configparser

class GameHandler:
    '''A class for handling the game behavior'''

    def __init__(self):
        '''Constructor for the GameHandler'''
        
        self.screen_blocker = turtle_helper.create_screen_blocker()
        self.screen_cover = turtle_helper.create_cover()
        self.user = self.create_user()
        self.card_count = self.set_card_count()
        self.num_flipped = 0
        self.card_1_id = None
        self.card_2_id = None
        self.cards = []
        self.compare_list = []
        self.match_count = 0
        self.attempts = 0
        self.leaderboard_turtle = turtle_helper.create_leaderboard_obj()
        self.status_tracker = turtle_helper.create_status_tracker_obj()
        turtle_helper.background()
        self.load_leaderboard()
        turtle_helper.setup_status_title(-420, -340)
        turtle_helper.display_leaderboard(
            self.leaderboard, self.leaderboard_turtle)
        turtle_helper.display_game_status(
            self.status_tracker, self.attempts, self.match_count)


    def create_user(self):
        user = turtle_helper.setup_user()
        while user == '' or user == None:
            self.display_enter_name_msg()
            user = turtle_helper.setup_user()
        return user

    def set_card_count(self):
        count_options = ['8', '10', '12']
        card_count = '0'
        card_count = turtle_helper.setup_card_count()
        while card_count not in count_options:
            self.display_card_count_msg()
            card_count = turtle_helper.setup_card_count()
        card_count = int(card_count)
        return card_count

    def shuffle_cards(self, card_count, card_dir):
        game_helpers.get_card_image_names(card_dir, 'img_ids.txt')
        img_ids = []
        # TODO: add try and except for opening file
        with open('img_ids.txt', 'r') as f:
            _list = f.readlines()
            for item in range(0, card_count):
                id = _list[item].strip('\n')
                img_ids.append(id)
        random.shuffle(img_ids)
        return img_ids
    
    def clear_cards(self):
        for card in self.cards:
            card.remove_card()
        self.cards = []

    def set_default_card_dir(self, cwd):
        card_front_path = os.path.join(cwd, 'boston_places')
        return card_front_path
        
    def set_card_path(self, config_file):
        cwd_set = False
        if os.path.exists(config_file):
            config = configparser.ConfigParser()
            config.read(config_file)
            cwd = os.getcwd()
            cwd_set = True
            card_front_dir = config.get(
                'card_customization', 'card_front_dir')
            card_front_path = os.path.join(cwd, card_front_dir)
            if os.path.exists(card_front_path):
                return card_front_path
            else:
                if cwd_set == False:
                    cwd = os.getcwd()
                card_front_path = self.set_default_card_dir(cwd)
                self.show_cover()
                self.display_dir_not_found_msg()
                self.hide_cover()
                return card_front_path
        else:
            if cwd_set == False:
                cwd = os.getcwd()
            card_front_path = self.set_default_card_dir(cwd)
            self.display_config_not_found_msg()
            return card_front_path
            


    def load_leaderboard(self):
        try: 
            with open(f"leaderboard_{self.card_count}.json", "r") as f:
                self.leaderboard = json.load(f)
        except FileNotFoundError:
            self.leaderboard = dict()             

    def card_was_flipped(self, image_id):
        self.display_screen_blocker()
        self.num_flipped += 1
        if self.num_flipped == 1:
            card_1_id = image_id
            self.update_compare_list(card_1_id)
        elif self.num_flipped == 2:
            self.attempts += 1
            card_2_id = image_id
            self.screen_delay(0.75)
            self.update_compare_list(card_2_id)
            self.compare_cards(self.compare_list)
            self.reset_values()
        self.hide_screen_blocker()
            
            
    def update_compare_list(self, image_id):
        self.compare_list.append(image_id)
        return self.compare_list


    def compare_cards(self, compare_list):
        if compare_list[0] == compare_list[1]:
            self.remove_or_reset(compare_list, self.cards, True)
            self.match_count += 1
            self.update_game_status()
            self.check_cards(self.card_count, self.match_count)
        else:
            self.update_game_status()
            self.remove_or_reset(compare_list, self.cards, False)


    def remove_or_reset(self, compare_list, cards, isMatch):
        turtle_helper.set_tracer(False)
        for item in cards:
            if item.image_id in compare_list:
                if isMatch:
                    item.remove_card()
                else:
                    item.reset_card()
        self.screen_delay(0.25)
        turtle_helper.update_screen()
        turtle_helper.set_tracer(True)

    def reset_values(self):
        self.num_flipped = 0
        self.card_1_id = None
        self.card_2_id =  None
        self.compare_list = []

    def reset_game_progress(self):
        self.match_count = 0
        self.attempts = 0
        self.update_game_status()

    def check_cards(self, card_count, match_count):
        if match_count == card_count / 2:
            self.display_win_msg()
            self.save_score_and_update_leaderboard()


    def save_score_and_update_leaderboard(self):
        turtle_helper.set_tracer(0)
        if self.leaderboard[
            self.user.title()] > self.attempts or self.user.title(
            ) not in self.leaderboard:
            self.leaderboard[self.user.title()] = self.attempts
            with open(f"leaderboard_{self.card_count}.json", "w") as f:
                json.dump(self.leaderboard, f)
        self.load_leaderboard()
        turtle_helper.display_leaderboard(
            self.leaderboard, self.leaderboard_turtle)
        turtle_helper.update_screen()

    def update_game_status(self):
        turtle_helper.set_tracer(0)
        turtle_helper.display_game_status(
            self.status_tracker, self.attempts, self.match_count)
        turtle_helper.update_screen()
        turtle_helper.set_tracer(1)



    # Messages and extras

    def display_win_msg(self):
        win_msg = turtle_helper.create_win_msg()
        screen = turtle.Screen()
        screen.register_shape('winner.gif')
        win_msg.penup()
        win_msg.shape('winner.gif')
        win_msg.showturtle()
        win_msg.setpos(0, 0)
        screen.update()
        self.screen_delay(2)
        win_msg.hideturtle()
        screen.update()
        
    def display_card_count_msg(self):
        card_count_msg = turtle_helper.create_card_count_msg() 
        screen = turtle.Screen()
        screen.register_shape('card_count_msg.gif')
        card_count_msg.penup()
        card_count_msg.shape('card_count_msg.gif')
        card_count_msg.showturtle()
        card_count_msg.setpos(0, 0)
        screen.update()
        self.screen_delay(1.5)
        card_count_msg.hideturtle()
        screen.update()

    def display_cards_loaded_msg(self):
        cards_loaded_msg = turtle_helper.create_cards_loaded_msg()
        screen = turtle.Screen()
        screen.register_shape('cards_loaded_msg.gif')
        cards_loaded_msg.penup()
        cards_loaded_msg.shape('cards_loaded_msg.gif')
        cards_loaded_msg.showturtle()
        cards_loaded_msg.setpos(0, 0)
        screen.update()
        self.screen_delay(1.5)
        cards_loaded_msg.hideturtle()
        screen.update()

    def display_enter_name_msg(self):
        enter_name_msg = turtle_helper.create_enter_name_msg()
        screen = turtle.Screen()
        screen.register_shape('enter_name_msg.gif')
        enter_name_msg.penup()
        enter_name_msg.shape('enter_name_msg.gif')
        enter_name_msg.showturtle()
        enter_name_msg.setpos(0, 0)
        screen.update()
        self.screen_delay(1.5)
        enter_name_msg.hideturtle()
        screen.update()
    
    def display_config_not_found_msg(self):
        config_not_found_msg = turtle_helper.create_config_not_found_msg()
        screen = turtle.Screen()
        screen.register_shape('config_not_found.gif')
        config_not_found_msg.penup()
        config_not_found_msg.shape('config_not_found.gif')
        config_not_found_msg.showturtle()
        config_not_found_msg.setpos(0, 0)
        screen.update()
        self.screen_delay(1.5)
        config_not_found_msg.hideturtle()
        screen.update()

    def display_dir_not_found_msg(self):
        dir_not_found_msg = turtle_helper.create_dir_not_found_msg()
        screen = turtle.Screen()
        screen.register_shape('directory_not_found.gif')
        dir_not_found_msg.penup()
        dir_not_found_msg.shape('directory_not_found.gif')
        dir_not_found_msg.showturtle()
        dir_not_found_msg.setpos(0, 0)
        screen.update()
        self.screen_delay(1.5)
        dir_not_found_msg.hideturtle()
        screen.update()

    def display_quit_msg(self):
        quit_msg = turtle_helper.create_quit_msg()
        screen = turtle.Screen()
        screen.register_shape("quit_msg.gif")
        quit_msg.penup()
        quit_msg.shape('quit_msg.gif')
        quit_msg.showturtle()
        quit_msg.setpos(0, 0)
        screen.update()
        self.screen_delay(2)
        turtle_helper.set_tracer(1)

    def display_credits_screen(self):
        credits = turtle_helper.create_credits_screen()
        screen = turtle.Screen()
        screen.register_shape("credits.gif")
        credits.penup()
        credits.shape('credits.gif')
        credits.showturtle()
        credits.setpos(0, 0)
        screen.update()
        self.screen_delay(3)
        turtle_helper.set_tracer(1)

        

    def show_cover(self):
        self.screen_cover = turtle_helper.create_cover()
        screen = turtle.Screen()
        screen.register_shape("cover.gif")
        self.screen_cover.penup()
        self.screen_cover.shape('cover.gif')
        self.screen_cover.showturtle()
        self.screen_cover.setpos(0, 0)
        screen.update()

    def hide_cover(self):
        self.screen_cover.hideturtle()

    def display_screen_blocker(self):
        screen = turtle.Screen()
        self.screen_blocker = turtle_helper.create_screen_blocker()
        screen.register_shape('screen_blocker.gif')
        self.screen_blocker.penup()
        self.screen_blocker.shape('screen_blocker.gif')
        self.screen_blocker.showturtle()
        self.screen_blocker.setpos(0, 0)
        screen.update()
        
    def hide_screen_blocker(self):
        screen = turtle.Screen()
        self.screen_blocker.hideturtle()
        screen.update()       

    def screen_delay(self, seconds):
        screen = turtle.Screen()
        self.display_screen_blocker
        time.sleep(seconds)
        self.hide_screen_blocker
        screen.update()

                
            
    




