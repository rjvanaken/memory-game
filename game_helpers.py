import random

def shuffle_cards():
    img_ids = []
    with open('img_ids.txt', 'r') as f:
        _list = f.readlines()
        for item in range(len(_list)):
            _list[item].strip()
            img_ids.append(_list[item])
    random.shuffle(img_ids)
    with open('img_ids.txt', 'w') as f:
        f.writelines(img_ids)
    

    # TODO: Maybe when this is called a cool shuffle animation is done?
    # except first time