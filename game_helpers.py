'''
    Rebecca Van Aken
    CS 5001, Fall, 2024
    Final Project

    This file contains helper functions for the process of initializing the
    cards on the screen
'''

from turtle_pos import positions
from Card import Card
import os

    
def create_cards(card_count, handler, config_file, card_dir):
    '''
        Function: create_cards(card_count, handler, config_file, card_dir)

        Does: initializes the cards on the screen by doing the following:
            - Reads the folder contents and writes file names to text file
            - Shuffles the card IDs to shuffle the order on screen
            - Initializes the Card class, according to the number of
            cards the user wants to play with

        Returns:
            - card_list: a list, containing the image IDs and representing
            the order in which they are displayed on the screen

        Parameters:
            - card_count: an integer, the number of cards the user chose
            to play the game with
            - handler: the instance of GameHandler which is managing the game
            - config_file: a string, representing the name of the config file.
            Unless specified by selecting "Reload Cards", by default this file
            is config.cfg
            - card_dir: a string, the path to the folder with the cards the 
            user chose to play with
    
    '''

    img_ids = handler.shuffle_cards(card_count, card_dir)
    index = 0
    card_list = []
    for index in range(0, card_count):
        card = Card(
            index, positions[index][0], positions[index][1], 
            img_ids[index], handler, config_file, card_dir)
        card_list.append(card)
        index += 1
    return card_list



def get_card_image_names(card_dir, output_file):
    '''
        Function: get_card_image_names(folder_path, output_file)

        Does: reads the image names (image IDs) from the specified card folder
        and writes each one to a text file twice

        Parameters:
            - card_dir: a string, the path to the folder with the cards the 
            user chose to play with
            - output_file: a string, the name of the file the image IDs are
            written to
    
    '''
    with open('img_ids.txt', 'w') as output_file:
        for filename in os.listdir(card_dir):
            output_file.write(filename + "\n")
            # execute this part twice since each image is used twice
            output_file.write(filename + '\n')