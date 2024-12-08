'''
    Rebecca Van Aken
    CS 5001, Fall, 2024
    Final Project

    This program runs a memory game, with 8, 10, or 12 cards to 
    play with, and a working leaderboard
'''

import turtle_helper
import game_helpers
import turtle
from GameHandler import GameHandler
from Button import Button


def play_game():
    '''
        Function: play_game()
        Does: Runs the memory game
    '''
    turtle.tracer(0)
    turtle_helper.setup_game_space()
    turtle_helper.splash_screen()
    # Initialize the handler
    handler = GameHandler()
    Button(button='quit', x=330, y=-310, handler=handler)
    Button(button='load', x=330, y=-255, handler=handler)
    card_dir = handler.set_card_path('config.cfg')
    # Initialize the cards
    handler.cards = game_helpers.create_cards(
        handler.card_count, handler, 'config.cfg', card_dir)
    turtle.tracer(0)
    turtle_helper.transition()
    turtle.tracer(1)
    turtle.Screen().mainloop()


def main():
    play_game()

if __name__ == '__main__':
    main()



# CHECK LOGIC FOR IF USER DOES NOT EXIST IN MEMORY GAME DICTIONARY
# CHECK AND SEE IF CONFIG_FILE NEEDS TO BE IN CARD CLASS