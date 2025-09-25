import pygame
import Items
from resource_path import resource_path
pygame.init()
class Objects(object):
    def __init__(self, x, y, source, desc, desc2, cap, inter, item, rint, lint, uint, dint):
        self.x = x
        self.y = y
        self.source = source
        self.rect = self.source.get_rect(topleft=(self.x, self.y))
        self.desc = desc
        self.desc2 = desc2
        self.cap = cap
        self.inter = inter
        self.item = item
        self.rint = False
        self.lint = False
        self.uint = False
        self.dint = False

    def draw(self, surface, obj):
        self.obj = obj
        surface.blit(self.obj, (self.x, self.y))


hay = Objects(283, 312, pygame.image.load(resource_path('pics/wheat.png')), '* Вы нашли зерна пшеницы!', '* Вы уже обыскали это.', 1, 0, Items.wheat, False, False, False, False)
hay_1 = Objects(501, 480, pygame.image.load(resource_path('pics/wheat_1.png')), '* Еще немного сена.', '* Еще немного сена.', 0, 0, Items.wheat, False, False, False, False)
hay_2 = Objects(693, 458, pygame.image.load(resource_path('pics/wheat_2.png')), '* Кучка сена.', '* Кучка сена.', 0, 0, Items.wheat, False, False, False, False)
carrot_box = Objects(700, 332, pygame.image.load(resource_path('pics/carrot_box.png')), '* Вы нашли морковь!', '* Вы уже обыскали это.', 1, 0, Items.carrot, False, False, False, False)
objects = [hay, hay_1, hay_2, carrot_box]
obstacles = [obj.rect for obj in objects]
for obst in obstacles:
    obst.height -= 40