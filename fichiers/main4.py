#coding:utf-8


import pickle
class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def display_info(self):
        print(f"Player Name: {self.name}, Level: {self.level}")


with open("player.data", "rb") as fic:
    get_record = pickle.Unpickler(fic)
    p1 = get_record.load()

p1.display_info()