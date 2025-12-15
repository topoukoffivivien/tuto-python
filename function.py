#coding:utf-8


def show_inventory(*list_item):
    for item in list_item:
        print(item)


show_inventory("épée", "bouclier", "potion", "armure")
show_inventory("arc", "flèches", "cape d'invisibilité")


calculer = lambda x, y: x + y
print(calculer(25, 19))