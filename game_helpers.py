import random
import turtle_helper
from data import positions
from Card import Card

    
def create_cards(card_count, handler):

    img_ids = handler.shuffle_cards(card_count)
    index = 0
    card_list = []
    for index in range(0, card_count):
        card = Card(index, positions[index][0], positions[index][1], img_ids[index], handler)
        card_list.append(card)
        index += 1
    return card_list
