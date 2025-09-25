import pygame
pygame.init()


class Items(object):
    def __init__(self, name, desc, heal, usage):
        self.name = name
        self.disc = desc
        self.heal = heal
        self.hp = 0
        self.usage = usage


paper = Items('Записка', '', 0, '* Записка от мамы: "Дорогой сын! Мы уехали на рынок. Из вкусного - банка варенья в '
                                'погребе."')
wheat = Items('Зерна пш-цы', '* Обычные пшеничные зерна', 0, '* Их не скушаешь.')
carrot = Items('Морковь', '* Обычная морковь', 4, '* Вы восстановили 4хп!')
items = [wheat, carrot]
inventory_coords = [(273, 145), (273, 255), (273, 365), (650, 145), (650, 255), (650, 365)]

