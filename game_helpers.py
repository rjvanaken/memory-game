import random
from data import positions
from Card import Card

def shuffle_cards():
    img_ids = []
    with open('img_ids.txt', 'r') as f:
        _list = f.readlines()
        for item in range(len(_list)):
            id = _list[item].strip('\n')
            img_ids.append(id)
    random.shuffle(img_ids)
    return img_ids

def game_board():
    img_ids = shuffle_cards()
    index = 0
    for index in range(len(positions)):
        Card(index, positions[index][0], positions[index][1], img_ids[index])
        index += 1
    

