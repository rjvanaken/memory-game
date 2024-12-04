from turtle_pos import positions
from Card import Card
import os
from Config import CardFront

    
def create_cards(card_count, handler):

    img_ids = handler.shuffle_cards(card_count)
    index = 0
    card_list = []
    for index in range(0, card_count):
        card = Card(index, positions[index][0], positions[index][1], img_ids[index], handler)
        card_list.append(card)
        index += 1
    return card_list

def get_card_image_names(folder_path, output_file):
    with open('img_ids.txt', 'w') as output_file:
        for filename in os.listdir(folder_path):
            output_file.write(filename + "\n")
        # execute this part twice since each image is used twice
        for filename in os.listdir(folder_path):
            output_file.write(filename + "\n")