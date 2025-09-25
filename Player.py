import pygame
import Locations
import Objects
import Items
from resource_path import resource_path
pygame.init()
ORIGINAL_WIDTH = 1024
ORIGINAL_HEIGHT = 768
playerStand = pygame.transform.scale(pygame.image.load(resource_path('pics/playermoves/movedown/move0.png')), (64, 90))
walk_right = [pygame.transform.scale(pygame.image.load(resource_path('pics/playermoves/moveright/move0.png')), (64, 90)),
              pygame.transform.scale(pygame.image.load(resource_path('pics/playermoves/moveright/move1.png')), (64, 90))]
walk_left = [pygame.transform.scale(pygame.image.load(resource_path('pics/playermoves/moveleft/move0.png')), (64, 90)),
             pygame.transform.scale(pygame.image.load(resource_path('pics//playermoves/moveleft/move1.png')), (64, 90))]
walk_up = [pygame.transform.scale(pygame.image.load(resource_path('pics/playermoves/moveup/move0.png')), (64, 90)),
           pygame.transform.scale(pygame.image.load(resource_path('pics/playermoves/moveup/move1.png')), (64, 90)),
           pygame.transform.scale(pygame.image.load(resource_path('pics/playermoves/moveup/move0.png')), (64, 90)),
           pygame.transform.scale(pygame.image.load(resource_path('pics/playermoves/moveup/move2.png')), (64, 90))]
walk_down = [pygame.transform.scale(pygame.image.load(resource_path('pics/playermoves/movedown/move0.png')), (64, 90)),
             pygame.transform.scale(pygame.image.load(resource_path('pics/playermoves/movedown/move1.png')), (64, 90)),
             pygame.transform.scale(pygame.image.load(resource_path('pics/playermoves/movedown/move0.png')), (64, 90)),
             pygame.transform.scale(pygame.image.load(resource_path('pics/playermoves/movedown/move2.png')), (64, 90))]
class Player(object):
    def __init__(self):
        self.tp = False
        self.textbox = False
        self.in_inv = False
        self.in_choice = False
        self.hp = 20
        self.inventory = [Items.paper]
        self.move = False
        self.x = 487
        self.y = 320
        self.width = playerStand.get_width()
        self.height = playerStand.get_height()
        self.rect = pygame.Rect(self.x, self.y, self.width - 20, self.height - 30)
        self.speed = 6
        self.interact = 0
        self.interaction_range = 10
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.playertrigger_r = pygame.Rect(537, 0, 2, 768)
        self.playertrigger_l = pygame.Rect(487, 0, 2, 768)
        self.playertrigger_u = pygame.Rect(0, 339, 1024, 2)
        self.playertrigger_d = pygame.Rect(0, 400, 1024, 2)
        self.animCount = 0
        self.walk_right = walk_right
        self.walk_left = walk_left
        self.walk_up = walk_up
        self.walk_down = walk_down
        self.playerStand = playerStand
        self.left_facing = False
        self.right_facing = False
        self.up_facing = False
        self.down_facing = False
        self.freeze = False

    def update(self, keys, objects_for_interaction, obstacles_for_movement):
        """___________________________________________________________________________
        Обновляет состояние игрока: движение, анимацию, коллизии.
        :param keys: Результат pygame.key.get_pressed()
        :param obstacles: Список или итерируемый объект с прямоугольниками препятствий (pygame.Rect).
                          В нашем случае это пока только chest_rect.
        ___________________________________________________________________________"""
        self.left = False
        self.right = False
        self.up = False
        self.down = False

        self.stopleft = False
        self.stopright = False
        self.stopup = False
        self.stopdown = False

        dx = 0
        dy = 0

        if not self.freeze:
            if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
                dx -= self.speed
                self.left = True
                self.left_facing = True
                self.right_facing = False
                self.up_facing = False
                self.down_facing = False
            elif keys[pygame.K_RIGHT]:
                dx += self.speed
                self.right = True
                self.left_facing = False
                self.right_facing = True
                self.up_facing = False
                self.down_facing = False
            if keys[pygame.K_UP]:
                dy -= self.speed
                self.up = True
                self.left_facing = False
                self.right_facing = False
                self.up_facing = True
                self.down_facing = False
            elif keys[pygame.K_DOWN]:
                dy += self.speed
                self.down = True
                self.left_facing = False
                self.right_facing = False
                self.up_facing = False
                self.down_facing = True

        if dx != 0 or dy != 0:
            self.animCount += 1
            if self.left_facing:
                if self.animCount // 5 >= len(self.walk_left):
                    self.animCount = 0
            elif self.right_facing:
                if self.animCount // 5 >= len(self.walk_right):
                    self.animCount = 0
            elif self.up_facing:
                if self.animCount // 5 >= len(self.walk_up):
                    self.animCount = 0
            elif self.down_facing:
                if self.animCount // 5 >= len(self.walk_down):
                    self.animCount = 0

        else:
            self.animCount = 0

        """___________________________________________________________________________
        Взаимодействие с объектами
        ___________________________________________________________________________"""

        self.interact = 0
        interaction_rect = self.rect.inflate(self.interaction_range * 2, self.interaction_range * 2)
        interaction_rect.center = self.rect.center
        for obj in objects_for_interaction:
            if interaction_rect.colliderect(obj.rect):
                if obj.rint:
                    if keys[pygame.K_LEFT] or keys[pygame.K_UP] or keys[pygame.K_DOWN]:
                        self.interact = 0
                        obj.inter = 0
                        obj.rint = False
                    else:
                        obj.inter = 1
                        self.interact = 1
                if obj.lint:
                    if keys[pygame.K_RIGHT] or keys[pygame.K_UP] or keys[pygame.K_DOWN]:
                        self.interact = 0
                        obj.inter = 0
                        obj.lint = False
                    else:
                        obj.inter = 1
                        self.interact = 1
                if obj.uint:
                    if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_DOWN]:
                        obj.inter = 0
                        self.interact = 0
                        obj.uint = False
                    else:
                        obj.inter = 1
                        self.interact = 1
                if obj.dint:
                    if keys[pygame.K_LEFT] or keys[pygame.K_UP] or keys[pygame.K_RIGHT]:
                        self.interact = 0
                        obj.inter = 0
                        obj.dint = False
                    else:
                        obj.inter = 1
                        self.interact = 1

        self.x += dx
        self.rect.x = self.x

        """___________________________________________________________________________
        Перемещение на первой локации по x.
        ___________________________________________________________________________"""

        if Locations.current_lc == 0:
            if self.rect.colliderect(Locations.lc00_rect) and not self.rect.colliderect(
                    Locations.lc01_rect):
                if self.rect.left < Locations.lc00_rect.left:
                    self.stopleft = True
                    self.rect.left = Locations.lc00_rect.left
                    self.x = self.rect.x
                if self.rect.right > Locations.lc00_rect.right:
                    self.stopright = True
                    self.rect.right = Locations.lc00_rect.right
                    self.x = self.rect.x
            elif self.rect.colliderect(Locations.lc00_rect) and self.rect.colliderect(
                    Locations.lc01_rect):
                if (self.rect.top < Locations.lc01_rect.top or self.rect.bottom > Locations.lc01_rect.bottom):
                    if self.rect.right > Locations.lc00_rect.right:
                        self.stopright = True
                        self.rect.right = Locations.lc00_rect.right
                        self.x = self.rect.x
            else:
                if self.rect.right > Locations.lc01_rect.right:
                    self.stopright = True
                    self.rect.right = Locations.lc01_rect.right
                    self.x = self.rect.x

        if Locations.current_lc == 1:
            if self.rect.colliderect(Locations.lc11_rect) and not self.rect.colliderect(
                    Locations.lc12_rect):
                if self.rect.left < Locations.lc11_rect.left:
                    self.stopleft = True
                    self.rect.left = Locations.lc11_rect.left
                    self.x = self.rect.x
                if self.rect.right > Locations.lc11_rect.right:
                    self.stopright = True
                    self.rect.right = Locations.lc11_rect.right
                    self.x = self.rect.x
            else:
                if self.rect.left < Locations.lc12_rect.left:
                    self.stopleft = True
                    self.rect.left = Locations.lc12_rect.left
                    self.x = self.rect.x
                if self.rect.right > Locations.lc12_rect.right:
                    self.stopright = True
                    self.rect.right = Locations.lc12_rect.right
                    self.x = self.rect.x
            if self.rect.colliderect(Locations.lc13_rect):
                if dx < 0:
                    if self.rect.left < Locations.lc13_rect.right:
                        self.stopleft = True
                        self.rect.left = Locations.lc13_rect.right
                        self.x = self.rect.x
                if dx > 0:
                    if self.rect.right > Locations.lc13_rect.left:
                        self.stopright = True
                        self.rect.right = Locations.lc13_rect.left
                        self.x = self.rect.x


        """___________________________________________________________________________
        Столкновение с объектами по x
        ___________________________________________________________________________"""

        for obstacle_rect in obstacles_for_movement:
            if self.rect.colliderect(obstacle_rect):
                if dx > 0:
                    self.stopright = True
                    self.rect.right = obstacle_rect.left
                    Objects.objects[obstacles_for_movement.index(obstacle_rect)].rint = True
                elif dx < 0:
                    self.stopleft = True
                    self.rect.left = obstacle_rect.right
                    Objects.objects[obstacles_for_movement.index(obstacle_rect)].lint = True
                self.x = self.rect.x

        self.y += dy
        self.rect.y = self.y

        """___________________________________________________________________________
        Перемещение на первой локации по y.
        ___________________________________________________________________________"""

        if Locations.current_lc == 0:
            if self.rect.colliderect(Locations.lc00_rect) and not self.rect.colliderect(
                    Locations.lc01_rect):
                if self.rect.top < Locations.lc00_rect.top:
                    self.stopup = True
                    self.rect.top = Locations.lc00_rect.top
                    self.y = self.rect.y
                if self.rect.bottom > Locations.lc00_rect.bottom:
                    self.stopdown = True
                    self.rect.bottom = Locations.lc00_rect.bottom
                    self.y = self.rect.y
            elif self.rect.colliderect(Locations.lc00_rect) and self.rect.colliderect(
                    Locations.lc01_rect):
                if self.rect.top < Locations.lc01_rect.top:
                    self.stopup = True
                    self.rect.top = Locations.lc01_rect.top
                    self.y = self.rect.y
                if self.rect.bottom > Locations.lc01_rect.bottom:
                    self.stopdown = True
                    self.rect.bottom = Locations.lc01_rect.bottom
                    self.y = self.rect.y
            else:
                if self.rect.top < Locations.lc01_rect.top:
                    self.stopup = True
                    self.rect.top = Locations.lc01_rect.top
                    self.y = self.rect.y
                if self.rect.bottom > Locations.lc01_rect.bottom:
                    self.stopdown = True
                    self.rect.bottom = Locations.lc01_rect.bottom
                    self.y = self.rect.y

        if Locations.current_lc == 1:
            if self.rect.colliderect(Locations.lc11_rect) and not self.rect.colliderect(
                    Locations.lc12_rect):
                if self.rect.top < Locations.lc11_rect.top:
                    self.stopup = True
                    self.rect.top = Locations.lc11_rect.top
                    self.y = self.rect.y
                if self.rect.bottom > Locations.lc11_rect.bottom:
                    self.stopdown = True
                    self.rect.bottom = Locations.lc11_rect.bottom
                    self.y = self.rect.y
            elif self.rect.colliderect(Locations.lc11_rect) and self.rect.colliderect(
                    Locations.lc12_rect):
                if self.rect.right > Locations.lc12_rect.right or self.rect.left < Locations.lc12_rect.left:
                    if self.rect.bottom > Locations.lc11_rect.bottom:
                        self.stopdown = True
                        self.rect.bottom = Locations.lc11_rect.bottom
                        self.y = self.rect.y
                else:
                    if self.rect.bottom > Locations.lc12_rect.bottom:
                        self.stopdown = True
                        self.rect.bottom = Locations.lc12_rect.bottom
                        self.y = self.rect.y
            else:
                if self.rect.bottom > Locations.lc12_rect.bottom:
                    self.stopdown = True
                    self.rect.bottom = Locations.lc12_rect.bottom
                    self.y = self.rect.y
            if self.rect.colliderect(Locations.lc13_rect):
                if dy < 0:
                    if self.rect.top < Locations.lc13_rect.bottom:
                        self.stopup = True
                        self.rect.top = Locations.lc13_rect.bottom
                        self.y = self.rect.y


        """___________________________________________________________________________
        Столкновение с объектами по y
        ___________________________________________________________________________"""

        for obstacle_rect in obstacles_for_movement:
            if self.rect.colliderect(obstacle_rect):
                if dy > 0:
                    self.stopdown = True
                    self.rect.bottom = obstacle_rect.top
                    Objects.objects[obstacles_for_movement.index(obstacle_rect)].dint = True
                elif dy < 0:
                    self.stopup = True
                    self.rect.top = obstacle_rect.bottom
                    Objects.objects[obstacles_for_movement.index(obstacle_rect)].uint = True
                self.y = self.rect.y

        """___________________________________________________________________________
        Перемещение камеры игрока
        ___________________________________________________________________________"""




    def draw(self, surface):
        """___________________________________________________________________________
        Отрисовывает игрока на заданной поверхности.
        :param surface: Поверхность Pygame, на которую будет отрисован игрок (в нашем случае game_surface).
        ___________________________________________________________________________"""
        current_player_image = self.playerStand

        if self.left:
            if self.stopleft != True:
                current_player_image = walk_left[self.animCount // 5 % len(walk_left)]
                self.left_facing = True
            else:
                current_player_image = walk_left[0]
            if self.up and self.stopup != True:
                current_player_image = walk_left[self.animCount // 5 % len(walk_left)]
            if self.down and self.stopdown != True:
                current_player_image = walk_left[self.animCount // 5 % len(walk_left)]

        elif self.right:
            if self.stopright != True:
                current_player_image = walk_right[self.animCount // 5 % len(walk_right)]
                self.right_facing = True
            else:
                current_player_image = walk_right[0]
            if self.up and self.stopup != True:
                current_player_image = walk_right[self.animCount // 5 % len(walk_right)]
            if self.down and self.stopdown != True:
                current_player_image = walk_right[self.animCount // 5 % len(walk_right)]

        elif self.up:
            if self.stopup != True:
                current_player_image = walk_up[self.animCount // 5 % len(walk_up)]
                self.up_facing = True
            else:
                current_player_image = walk_up[0]
            if self.right and self.stopright != True:
                current_player_image = walk_up[self.animCount // 5 % len(walk_up)]
            if self.left and self.stopleft != True:
                current_player_image = walk_up[self.animCount // 5 % len(walk_up)]

        elif self.down:
            if self.stopdown != True:
                current_player_image = walk_down[self.animCount // 5 % len(walk_down)]
                self.down_facing = True
            else:
                current_player_image = walk_down[0]
            if self.right and self.stopright != True:
                current_player_image = walk_down[self.animCount // 5 % len(walk_down)]
            if self.left and self.stopleft != True:
                current_player_image = walk_down[self.animCount // 5 % len(walk_down)]

        else:
            if self.left_facing:
                current_player_image = walk_left[0]
            elif self.right_facing:
                current_player_image = walk_right[0]
            elif self.up_facing:
                current_player_image = walk_up[0]
            elif self.down_facing:
                current_player_image = walk_down[0]
            self.animCount = 0

        surface.blit(current_player_image, (self.x - 10, self.y - 30))

player = Player()