#coding:utf-8


import pickle
class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def display_info(self):
        print(f"Player Name: {self.name}, Level: {self.level}")


p1 = Player("Alice", 5)

with open("player.data", "wb") as fic:
    record = pickle.Pickler(fic)
    record.dump(p1)