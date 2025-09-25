import pygame
from resource_path import resource_path

class NPC(object):
    def __init__(self, hp, dialog, sprites, current_sprite):
        self.hp = hp
        self.dialog = dialog
        self.sprites = sprites
        self.current_sprite = current_sprite

    def draw(self, surface, sprite, x, y):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.rect = self.sprites[self.current_sprite].get_rect(topleft=(self.x, self.y))
        surface.blit(self.sprite, (self.x, self.y))

tim = NPC(20, ['* ', '* ', '* Как'], [pygame.image.load(resource_path('pics/tim_1_room.png'))], 0)
tim_dlg = ['* Хм? Кого занесло в эту глушь?', '* На вид ты выглядишь как ребенок, однако по росту выше здешних жителей.', '* Как тебя зовут?']
